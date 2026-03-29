import os

import mpi4py.MPI as MPI


def test_mpi4py():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()  # rank = the process ID (0, 1, 2, ...)
    size = (
        comm.Get_size()
    )  # size = total number of processes (e.g., 4 if you run with mpirun -n 4)
    print(f"Hello from process {rank} out of {size} processes.")


def test_mpi4py_sum():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Each process will have a local value equal to its rank
    local_value = rank

    # Reduce all local values to a global sum at the root process (rank 0)
    global_sum = comm.reduce(local_value, op=MPI.SUM, root=0)

    if rank == 0:
        print(f"The total sum of ranks is: {global_sum}")


def test_mpi4py_json_split(path="comp90024_assignment1_spartan/bluesky-medium.ndjson"):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    file_size = os.path.getsize(path)
    # print("File size:", file_size, "bytes")
    chunk_size = file_size // size
    # print("Chunk size:", chunk_size, "bytes")
    start_byte = rank * chunk_size
    end_byte = file_size if rank == size - 1 else (rank + 1) * chunk_size

    if rank == 0:
        print(f"Started reading file '{path}' with {size} processes.")
        print(f"File size: {file_size} bytes, Chunk size: {chunk_size} bytes \n")
    print(f"Process {rank} will read bytes {start_byte} to {end_byte}")

    with open(path, "r", encoding="utf-8") as f:
        f.seek(start_byte)  # Move to the start of the assigned chunk
        if rank != 0:
            f.readline()  # Skip partial line for non-root processes

        i = 1
        while f.tell() < end_byte:
            line = f.readline()
            if not line:
                break
            print(f"Process {rank} read line {i}, end byte {f.tell()}")
            i += 1


if __name__ == "__main__":
    # test_mpi4py()
    test_mpi4py_sum()
    # test_mpi4py_json_split("comp90024_assignment1_spartan/mastodon-medium.ndjson")
