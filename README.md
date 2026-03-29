# COMP90024 Assignment 1

This repository contains the work for the Cluster and Cloud Computing assignment on parallel language counting for Mastodon and BlueSky NDJSON datasets.

## Goal

Build a single program that can:

- read Mastodon and BlueSky posts from NDJSON files
- count language codes found in each post
- handle missing, null, and unusual values safely
- run in parallel with `mpi4py`
- be submitted and benchmarked on SPARTAN with SLURM

## Contents

- `test_json.py` - local JSON parsing and counting experiments
- `test_mpi4py.py` - MPI testing script
- `assignment_plan.md` - working plan and checklist
- `ai_log.md` - log of AI-assisted work
- `.gitignore` - repository ignore rules

## Notes

The large dataset files are not meant for development. Use the small and medium NDJSON files for testing, and the large files only for the final benchmark runs.
