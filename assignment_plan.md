# Assignment 1 Plan

## Goal
Build one program that can analyze both Mastodon and BlueSky NDJSON files on SPARTAN, count all language codes found in the `lang` / `langs` data, and run correctly under 1 node/1 core, 1 node/8 cores, and 2 nodes/8 cores.

## Strategy
1. Start with data inspection on `*-small.ndjson` and `*-medium.ndjson`.
2. Implement a serial line-by-line parser first.
3. Make the parser robust against malformed JSON, missing language fields, `null`, and unexpected data shapes.
4. Parallelize with MPI using `mpi4py`.
5. Use SLURM scripts to run the same program with the required node/core configurations.
6. Benchmark only after the serial and parallel outputs match on small/medium files.
7. Collect timings, counts, and notes for the report.

## Technical Approach
- Use `jq` only for inspection and debugging, not for the final counting program.
- Use Python `json` plus `collections.Counter` for the serial counter.
- Use `mpi4py` for process ranks, file slicing, and global reduction.
- Use shell scripts for `sbatch` submission and repeatable runs.
- Prefer a single program with arguments for dataset path and runtime mode.

## Parallelization Plan
- Split the NDJSON file into byte ranges, one per MPI rank.
- Let each rank seek to its slice, skip any partial first line, and stop at the slice boundary.
- Count languages locally on each rank.
- Merge local counts on the root process.
- Time only the job execution, not queueing.

## Concrete Checklist
- [ ] Write a serial Python script that streams NDJSON line by line.
- [ ] Add safe handling for malformed JSON, missing fields, `null`, and empty values.
- [ ] Confirm the serial script matches expected counts on the small files.
- [ ] Add support for posts containing multiple languages.
- [ ] Refactor into a single program that works for both Mastodon and BlueSky.
- [ ] Implement MPI file splitting by byte range with `mpi4py`.
- [ ] Test the MPI version on small and medium files with 1 rank and multiple ranks.
- [ ] Create SLURM submission scripts for 1x1, 1x8, and 2x8 resource settings.
- [ ] Measure runtime inside the job and save logs for each benchmark.
- [ ] Run the final benchmarks on the large files only after the implementation is stable.
- [ ] Prepare final tables, one performance graph, and the report text.
- [ ] Write the LLM disclosure section if any AI assistance was used.

## Report Notes To Collect
- Exact command used to launch the program.
- Resource settings for each SLURM run.
- Runtime for each benchmark.
- Final language frequency tables for Mastodon and BlueSky.
- Brief explanation of Amdahl’s law in the context of the measured speedup.
- Notes on any malformed records or cleanup decisions.
