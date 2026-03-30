import json
import os
import sys
from collections import Counter

import mpi4py.MPI as MPI
from langs_from_post import extract_languages

def local_count() -> Counter:
    """Counts languages in the assigned chunk of the file."""
    with open(path, "r", encoding="utf-8") as f:
        f.seek(start_byte)  # Move to the start of the assigned chunk
        if rank != 0:
            f.readline()  # Skip partial line for non-root processes

        local_count = Counter()  # Begin counting languages
        while f.tell() < end_byte:
            line = f.readline()
            if not line:  # EOF
                break

            try:
                post = json.loads(line)
                local_count.update(extract_languages(post))
            except json.JSONDecodeError:
                continue
    
    print(f"Process {rank} counted languages: {local_count}", file=sys.stderr)

    return local_count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Please provide the path to the NDJSON file as a command-line argument.")
        sys.exit(1)

    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Calculate byte ranges for each process
    file_size = os.path.getsize(path)
    chunk_size = file_size // size
    start_byte = rank * chunk_size
    end_byte = file_size if rank == size - 1 else (rank + 1) * chunk_size

    comm.Barrier()  # Synchronize before starting the timer
    start_time = MPI.Wtime()

    local_langs = local_count()
    global_langs = comm.reduce(local_langs, op=MPI.SUM, root=0)

    comm.Barrier()
    end_time = MPI.Wtime()

    if rank == 0:
        # Sort by number of occurrences in descending order and convert to list 
        global_langs = list(sorted(global_langs.items(), key=lambda elem: elem[1], reverse=True))

        print(f"Total language counts: {global_langs}", file=sys.stderr)

        print("Language | Frequency")
        print("---------|----------")
        for lang, n in global_langs:
            print(str(lang).ljust(9) + f"| {n}")
            
        print(f"Execution time: {end_time - start_time:f} seconds")
