# Schedule Movement Analyzer

## What this tool does

The Schedule Movement Analyzer is a beginner-friendly Python tool that compares original schedule milestone dates against updated schedule milestone dates.

It calculates how much each milestone moved, whether the milestone was delayed or accelerated, and how severe the schedule variance is.

## Why I built it

Project controls teams often need to compare schedule updates over time and quickly identify which milestones moved, how far they moved, and which changes are most important.

In a real business setting, this kind of tool could help with:

- Weekly schedule update reviews
- Project manager reporting
- Stakeholder communication
- Schedule variance tracking
- Early identification of major milestone shifts

This project is part of my AI-assisted workflow automation portfolio focused on project controls, Smartsheet, Primavera P6, schedule analysis, and operational reporting.

## Example input

The tool reads a CSV file from:

```text
data/sample_schedule.csv