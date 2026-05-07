# Schedule Movement Analyzer

## What this tool does

The Schedule Movement Analyzer is a beginner-friendly Python tool that compares original schedule milestone dates against updated schedule milestone dates.

It reads a CSV schedule file, calculates how much each milestone moved, and writes a new CSV file with additional analysis columns.

The tool calculates:

- Calendar days moved
- Workdays moved, excluding weekends and example company holidays
- Movement direction: delayed, accelerated, or unchanged
- Variance category: no change, minor, moderate, or major

Before running the analysis, the script also validates the input file for:

- Required input columns
- Blank values in the schedule date fields
- Invalid date formats in the schedule date fields

If the input file has an issue, the script shows a friendly error message instead of a long pandas traceback.

## Why I built it

Project controls teams often need to compare schedule updates over time and quickly identify which milestones moved, how far they moved, and which changes are most important.

I built this project as part of my AI-assisted workflow automation portfolio focused on project controls, Smartsheet, Primavera P6, schedule analysis, and operational reporting.

The goal is to show how a small Python script can turn a manual review process into a repeatable reporting workflow.

## Example input

The tool reads a CSV file from:

```text
data/sample_schedule.csv
```

The input file includes one row per project milestone.

| Project ID | Project Name | Milestone ID | Milestone Name | Original Schedule Date | New Schedule Date |
| --- | --- | --- | --- | --- | --- |
| 26-100001 | Clubhouse Refresh | MS-001 | Design Complete | 10/10/2025 | 10/17/2025 |
| 26-100002 | Pool Deck Repairs | MS-002 | Permit Submitted | 11/24/2025 | 12/01/2025 |
| 26-100003 | Roof Replacement | MS-003 | Contract Award | 12/22/2025 | 12/19/2025 |

## Example output

The tool writes the analyzed results to:

```text
output/schedule_movement_results.csv
```

The output keeps the original schedule data and adds analysis columns.

| Project ID | Milestone Name | Original Schedule Date | New Schedule Date | Calendar Days Moved | Workdays Moved | Movement Direction | Variance Category |
| --- | --- | --- | --- | ---: | ---: | --- | --- |
| 26-100001 | Design Complete | 10/10/2025 | 10/17/2025 | 7 | 5 | Delayed | Moderate |
| 26-100002 | Permit Submitted | 11/24/2025 | 12/01/2025 | 7 | 3 | Delayed | Moderate |
| 26-100003 | Contract Award | 12/22/2025 | 12/19/2025 | -3 | -1 | Accelerated | Minor |

## How to run it

Install the required Python package:

```powershell
pip install -r requirements.txt
```

Run the analyzer from the project root:

```powershell
python src/analyze_schedule_movement.py
```

After the script runs, open the output file:

```text
output/schedule_movement_results.csv
```

## How to run tests

This project includes a small test file for the core workday movement calculation.

Run the tests from the project root:

```powershell
python -m unittest discover -s tests
```

The tests cover:

- Unchanged dates
- Delayed dates
- Accelerated dates
- Weekend handling
- Holiday handling

## Business use case

In a project controls environment, schedule updates are often reviewed weekly or monthly. A project manager, scheduler, or analyst may need to know which milestones moved, whether they moved earlier or later, and which changes are large enough to require attention.

This tool could support:

- Weekly schedule update reviews
- Project manager reporting
- Stakeholder communication
- Schedule variance tracking
- Early identification of major milestone shifts

For example, a project controls analyst could export milestone dates from a scheduling system, run this tool, and quickly identify delayed milestones that should be discussed in a status meeting.

## What I used ChatGPT for

I used ChatGPT as a learning partner while building this project. It helped me:

- Break the problem into small steps
- Think through beginner-friendly Python structure
- Explain pandas concepts in plain language
- Improve naming, comments, and documentation
- Connect the script to a realistic project controls use case

## What I will use Codex for

I will use Codex to continue improving the project directly in the codebase. Planned Codex-assisted work includes:

- Refining input validation as the project grows
- Moving holidays into a separate configuration file
- Adding command-line options for custom input and output files
- Writing simple tests for the workday calculation logic
- Keeping the README and code comments clear as the project grows

## Future improvements

Future versions of this project could include:

- A separate holiday calendar file
- Summary metrics by project
- A filtered report showing only major schedule movement
- Excel output for easier business review
- Charts or visual summaries of milestone movement
- Unit tests for date calculation rules
- Support for user-selected input files
