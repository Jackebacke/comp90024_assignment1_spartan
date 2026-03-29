import json
import os
from collections import Counter

import mpi4py.MPI as MPI
from langs_from_post import extract_languages

PATH = "comp90024_assignment1_spartan/bluesky-medium.ndjson"

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Calculate byte ranges for each process
file_size = os.path.getsize(PATH)
chunk_size = file_size // size
start_byte = rank * chunk_size
end_byte = file_size if rank == size - 1 else (rank + 1) * chunk_size


def local_count() -> Counter:
    """Counts languages in the assigned chunk of the file."""
    with open(PATH, "r", encoding="utf-8") as f:
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

    print(f"Process {rank} counted languages: {local_count}")
    return local_count


if __name__ == "__main__":
    local_langs = local_count()
    global_langs = comm.reduce(local_langs, op=MPI.SUM, root=0)

    if rank == 0:
        print(f"Total language counts: {global_langs}")
