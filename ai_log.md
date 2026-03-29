# AI Usage Log

## Entry 1

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Help plan the Cluster and Cloud Computing Assignment 1 workflow and create a concrete checklist.
- Prompt summary: Asked for a practical plan covering jq, mpi4py, shell/SLURM usage, parallelization strategy, benchmarking, and report preparation.
- Outcome: Produced a structured implementation plan and checklist focused on serial validation first, then MPI parallelization, then SLURM benchmarking on SPARTAN.

## Entry 2

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Save the plan and create an AI log file.
- Prompt summary: Asked to persist the plan in the workspace and create a log for AI assistance used during the assignment.
- Outcome: Created `assignment_plan.md` and this log file.

## Entry 3

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Explain the assignment plan in more detail.
- Prompt summary: Asked for a practical workflow covering data inspection, serial parsing, mpi4py parallelization, SLURM submission, benchmarking, and report writing.
- Outcome: Produced a step-by-step implementation plan and checklist.

## Entry 4

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Resolve the missing `jq` import.
- Prompt summary: Reported `ModuleNotFoundError: No module named 'jq'` when running a test script.
- Outcome: Installed `jq` into the active Conda environment and adjusted the smoke test.

## Entry 5

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Explain what `jq` is and how to use it.
- Prompt summary: Asked for a plain-language explanation of `jq`, how to use it with NDJSON, and common commands for the assignment.
- Outcome: Documented `jq` as a JSON command-line filter and showed inspection/counting examples.

## Entry 6

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Show how to use `jq` from Python.
- Prompt summary: Asked how to invoke `jq` in Python and how it fits into the NDJSON workflow.
- Outcome: Explained `jq.compile(...).input(...).first()` and `all()` usage.

## Entry 7

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Debug BlueSky language extraction.
- Prompt summary: Shared a BlueSky record and asked why the language lookup returned an empty set.
- Outcome: Identified the correct path as `record.langs` and explained the nested BlueSky schema.

## Entry 8

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Explain why use `jq` at all.
- Prompt summary: Asked whether `jq` is necessary or whether Python `json` is enough.
- Outcome: Clarified that `jq` is useful for inspection/debugging, while Python `json` is the better choice for the final program.

## Entry 9

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Explain the `test_json.py` parser.
- Prompt summary: Asked for an in-depth explanation of the helper functions and why `record` was used as a variable name.
- Outcome: Explained NDJSON line-by-line parsing, the role of `Counter`, and the BlueSky `record.langs` path.

## Entry 10

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Add Mastodon support.
- Prompt summary: Asked to make the parser work for Mastodon using `doc.language` as well as BlueSky.
- Outcome: Updated the helper to support both JSON layouts and verified it on both sample files.

## Entry 11

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Switch from unique values to frequency counts.
- Prompt summary: Asked whether `Counter` or `dict` is better for counting language appearances.
- Outcome: Reworked the code to use `Counter` and explained why it is the simpler choice for this task.

## Entry 12

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Handle null values explicitly.
- Prompt summary: Asked what happens to `null` language values and then requested that nulls be counted too.
- Outcome: Changed the parser to distinguish missing fields from explicit nulls and count nulls as their own bucket.

## Entry 13

- Date: 2026-03-28
- Model: GPT-5.4 mini
- Task: Simplify the parser.
- Prompt summary: Asked for the simplest method to read both Mastodon and BlueSky lines.
- Outcome: Collapsed the code into a single line-by-line counting loop using `Counter`.

## Entry 14

- Date: 2026-03-29
- Model: GPT-5.4 mini
- Task: Inspect missing and weird entries.
- Prompt summary: Asked to count everything, then asked to see the missing entries and separate outlier categories.
- Outcome: Added buckets for missing, null, empty, and weird values and printed example records for inspection.

## Entry 15

- Date: 2026-03-29
- Model: GPT-5.4 mini
- Task: Update the AI log itself.
- Prompt summary: Asked to add all conversations to the AI log.
- Outcome: Appended a chronological summary of the discussion topics to this file.
