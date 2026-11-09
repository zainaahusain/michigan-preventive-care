# AI Assistance Documentation
# Tool: OpenAI ChatGPT (GPT-6)
# Date: November 9, 2026
# ChatGPT assisted with planning and implementing the data analysis,
# including filtering CDC PLACES records, computing summary statistics,
# and creating a visualization.
# I ran the code, reviewed the outputs, and verified its behavior
# using automated tests and a Great Lakes SLURM batch job.

from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "places_county_2025.csv"
RESULTS_DIR = PROJECT_DIR / "results"


def select_michigan_checkups(data):
    """Select Michigan county routine-checkup estimates."""
    selected = data[
        (data["StateAbbr"] == "MI")
        & (data["MeasureId"] == "CHECKUP")
        & (data["Data_Value_Type"] == "Age-adjusted prevalence")
    ].copy()

    selected["Data_Value"] = pd.to_numeric(
        selected["Data_Value"], errors="coerce"
    )

    selected = selected.dropna(subset=["Data_Value"])

    return selected[["LocationName", "Data_Value"]].sort_values(
        "LocationName"
    )


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    print("Reading CDC PLACES data...")
    data = pd.read_csv(DATA_FILE, low_memory=False)

    counties = select_michigan_checkups(data)

    if counties.empty:
        raise ValueError("No Michigan routine-checkup estimates found.")

    average = counties["Data_Value"].mean()

    print(f"Counties analyzed: {len(counties)}")
    print(f"Average county estimate: {average:.2f}%")

    counties.to_csv(
        RESULTS_DIR / "michigan_checkups.csv",
        index=False
    )

    top_ten = counties.nlargest(10, "Data_Value")
    top_ten = top_ten.sort_values("Data_Value")

    plt.figure(figsize=(10, 6))
    plt.barh(top_ten["LocationName"], top_ten["Data_Value"])
    plt.xlabel("Age-adjusted prevalence (%)")
    plt.ylabel("Michigan county")
    plt.title("Routine Checkups in Michigan Counties (2023 Estimates)")
    plt.xlim(0, 100)
    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "top_10_counties.png",
        dpi=150
    )
    plt.close()

    print("Results saved in the results folder.")


if __name__ == "__main__":
    main()
