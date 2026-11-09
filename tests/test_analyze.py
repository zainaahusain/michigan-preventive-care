import pandas as pd

from src.analyze import select_michigan_checkups


def test_selects_only_michigan_checkups():
    """Only Michigan routine-checkup rows should remain."""
    sample = pd.DataFrame({
        "StateAbbr": ["MI", "MI", "OH", "MI"],
        "MeasureId": ["CHECKUP", "DIABETES", "CHECKUP", "CHECKUP"],
        "Data_Value_Type": [
            "Age-adjusted prevalence",
            "Age-adjusted prevalence",
            "Age-adjusted prevalence",
            "Crude prevalence",
        ],
        "LocationName": [
            "Wayne", "Wayne", "Franklin", "Kent"
        ],
        "Data_Value": [79.5, 12.0, 80.0, 78.0],
    })

    result = select_michigan_checkups(sample)

    assert len(result) == 1
    assert result.iloc[0]["LocationName"] == "Wayne"
    assert result.iloc[0]["Data_Value"] == 79.5


def test_missing_estimates_are_removed():
    """Missing estimates should not appear in results."""
    sample = pd.DataFrame({
        "StateAbbr": ["MI", "MI"],
        "MeasureId": ["CHECKUP", "CHECKUP"],
        "Data_Value_Type": [
            "Age-adjusted prevalence",
            "Age-adjusted prevalence",
        ],
        "LocationName": ["Wayne", "Kent"],
        "Data_Value": [79.5, None],
    })

    result = select_michigan_checkups(sample)

    assert len(result) == 1
    assert result.iloc[0]["LocationName"] == "Wayne"


def test_counties_are_sorted_alphabetically():
    """Output counties should be sorted by name."""
    sample = pd.DataFrame({
        "StateAbbr": ["MI", "MI"],
        "MeasureId": ["CHECKUP", "CHECKUP"],
        "Data_Value_Type": [
            "Age-adjusted prevalence",
            "Age-adjusted prevalence",
        ],
        "LocationName": ["Wayne", "Alcona"],
        "Data_Value": [79.5, 77.0],
    })

    result = select_michigan_checkups(sample)

    assert result["LocationName"].tolist() == [
        "Alcona", "Wayne"
    ]
