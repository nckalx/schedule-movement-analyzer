from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


# Find the main project folder.
# This lets the script work even if we run it from a different location.
BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "sample_schedule.csv"
OUTPUT_FILE = BASE_DIR / "output" / "schedule_movement_results.csv"


# Example company holidays.
# We can expand this later or move it to a separate CSV/config file.
HOLIDAYS = {
    datetime.strptime(date_text, "%m/%d/%Y").date()
    for date_text in [
        "11/27/2025",
        "11/28/2025",
        "12/25/2025",
        "12/26/2025",
        "01/01/2026",
        "01/02/2026",
        "01/19/2026",
        "02/16/2026",
    ]
}


def count_workdays_moved(original_date, new_date):
    """
    Count the number of workdays a milestone moved.

    Positive number = milestone moved later.
    Negative number = milestone moved earlier.
    Zero = no movement.

    This excludes the original date and includes the new date,
    similar to a schedule variance calculation.
    """
    if original_date == new_date:
        return 0

    moved_later = new_date > original_date

    if moved_later:
        start_date = original_date + timedelta(days=1)
        end_date = new_date
        direction = 1
    else:
        start_date = new_date + timedelta(days=1)
        end_date = original_date
        direction = -1

    workday_count = 0
    current_date = start_date

    while current_date <= end_date:
        is_weekday = current_date.weekday() < 5
        is_holiday = current_date in HOLIDAYS

        if is_weekday and not is_holiday:
            workday_count += 1

        current_date += timedelta(days=1)

    return workday_count * direction


def get_movement_direction(calendar_days_moved):
    """Return a simple direction label."""
    if calendar_days_moved > 0:
        return "Delayed"
    if calendar_days_moved < 0:
        return "Accelerated"
    return "Unchanged"


def get_variance_category(workdays_moved):
    """Return a simple schedule variance category."""
    absolute_value = abs(workdays_moved)

    if absolute_value == 0:
        return "No Change"
    if absolute_value <= 2:
        return "Minor"
    if absolute_value <= 5:
        return "Moderate"
    return "Major"


def main():
    print(f"Reading schedule data from: {INPUT_FILE}")

    schedule_df = pd.read_csv(INPUT_FILE)

    schedule_df["Original Schedule Date"] = pd.to_datetime(
        schedule_df["Original Schedule Date"],
        format="%m/%d/%Y",
    )

    schedule_df["New Schedule Date"] = pd.to_datetime(
        schedule_df["New Schedule Date"],
        format="%m/%d/%Y",
    )

    schedule_df["Calendar Days Moved"] = (
        schedule_df["New Schedule Date"] - schedule_df["Original Schedule Date"]
    ).dt.days

    schedule_df["Workdays Moved"] = schedule_df.apply(
        lambda row: count_workdays_moved(
            row["Original Schedule Date"].date(),
            row["New Schedule Date"].date(),
        ),
        axis=1,
    )

    schedule_df["Movement Direction"] = schedule_df["Calendar Days Moved"].apply(
        get_movement_direction
    )

    schedule_df["Variance Category"] = schedule_df["Workdays Moved"].apply(
        get_variance_category
    )

    # Convert dates back to MM/DD/YYYY for easier reading in Excel.
    schedule_df["Original Schedule Date"] = schedule_df[
        "Original Schedule Date"
    ].dt.strftime("%m/%d/%Y")

    schedule_df["New Schedule Date"] = schedule_df["New Schedule Date"].dt.strftime(
        "%m/%d/%Y"
    )

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    schedule_df.to_csv(OUTPUT_FILE, index=False)

    total_milestones = len(schedule_df)
    delayed_milestones = (schedule_df["Movement Direction"] == "Delayed").sum()
    accelerated_milestones = (
        schedule_df["Movement Direction"] == "Accelerated"
    ).sum()
    unchanged_milestones = (schedule_df["Movement Direction"] == "Unchanged").sum()
    major_variances = (schedule_df["Variance Category"] == "Major").sum()

    print("Analysis complete.")
    print()
    print("Summary:")
    print(f"Total milestones analyzed: {total_milestones}")
    print(f"Delayed milestones: {delayed_milestones}")
    print(f"Accelerated milestones: {accelerated_milestones}")
    print(f"Unchanged milestones: {unchanged_milestones}")
    print(f"Major variances: {major_variances}")
    print()
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
