# Michigan Preventive Care Explorer

## Project Overview

This project analyzes estimated routine healthcare checkup prevalence across Michigan counties using publicly available data from the CDC PLACES program.

**Research question:** How does the estimated percentage of adults who visited a doctor for a routine checkup within the past year vary across Michigan counties?

The project demonstrates how Python can be used to analyze public health data, generate visualizations, and run a reproducible computational workflow on a high-performance computing cluster.

## Data Source

The dataset comes from the Centers for Disease Control and Prevention (CDC), PLACES: Local Data for Better Health, County Data, 2025 release.

Dataset: https://data.cdc.gov/d/swc5-untb

The analysis uses 2023 estimates for the measure `CHECKUP`, which describes routine doctor checkups within the past year among adults.

The analysis filters the dataset using:

- `StateAbbr == "MI"`
- `MeasureId == "CHECKUP"`
- `Data_Value_Type == "Age-adjusted prevalence"`

The full original CSV is excluded from GitHub because of its size. To reproduce the analysis, download the county-level CSV from the CDC link above and save it as `data/places_county_2025.csv`.

These are modeled county-level estimates, not individual patient records.

## Python Environment

The project uses Python 3.12 and the following packages:

- pandas for data analysis
- matplotlib for visualization
- pytest for automated testing

On a system with Mamba installed, create the environment using:

```bash
mamba env create -p ~/michigan-preventive-care-env -f environment.yml
```

Run the program using the Python interpreter from that environment:

```bash
~/michigan-preventive-care-env/bin/python src/analyze.py
```

## Running the Analysis

From the project root, run:

```bash
python src/analyze.py
```

The program reads the CDC dataset, filters for Michigan routine-checkup estimates, calculates the mean county estimate, and generates two output files:

- `results/michigan_checkups.csv` — county names and prevalence estimates
- `results/top_10_counties.png` — bar chart of the 10 highest county estimates

## Testing and Continuous Integration

The project uses pytest to test:

1. Filtering for the correct state, measure, and estimate type
2. Removing missing prevalence estimates
3. Sorting county names alphabetically

Run tests using:

```bash
python -m pytest -v
```

All three tests passed locally and on the University of Michigan Great Lakes cluster.

GitHub Actions automatically runs the tests on pushes and pull requests using Python 3.12. The workflow is stored in `.github/workflows/tests.yml`.

## Great Lakes HPC Execution

The analysis was submitted to the University of Michigan Great Lakes cluster as a single-threaded SLURM batch job.

The batch script is `run_job.sh`.

The script requests one CPU, 2 GB of memory, and a maximum runtime of 10 minutes.

After creating the environment on Great Lakes, submit the job from the project directory using:

```bash
sbatch run_job.sh
```

**Job ID:** 65782743

Evidence files:

- `results/job_id.txt`
- `results/slurm-accounting.txt`
- `logs/checkups-65782743.out`
- `logs/checkups-65782743.err`

The SLURM accounting record documents the job's completion status, elapsed time, and resource usage.

## Results and Interpretation

The analysis includes 83 Michigan counties.

The mean of the county-level age-adjusted routine-checkup estimates is approximately **77.42%**.

The highest estimates include Macomb and Ottawa counties at 79.7%, followed by Wayne County at 79.5%.

The lowest estimates include Lenawee County at 75.8%, Oceana County at 75.9%, and Jackson County at 76.1%.

These findings show geographic variation in modeled routine-checkup prevalence across Michigan counties.

The reported mean is an unweighted average of county estimates, not a population-weighted statewide prevalence estimate.

Because the estimates are modeled and descriptive, the results do not establish causes of county differences or indicate that one county has a better healthcare system overall.

## Limitations

CDC PLACES estimates are generated using statistical models and survey-based data rather than directly observing every adult in each county.

The analysis examines one preventive healthcare measure and does not account for uncertainty intervals, socioeconomic conditions, healthcare availability, or other factors that may influence routine checkup rates.

The findings should not be interpreted as causal relationships.

## References and AI Assistance

- Centers for Disease Control and Prevention. *PLACES: Local Data for Better Health.* https://www.cdc.gov/places/
- CDC PLACES County Data, 2025 release. https://data.cdc.gov/d/swc5-untb

**AI assistance disclosure:** 
I used ChatGPT (OpenAI, GPT-6) as an AI assistant while developing this project.

AI assistance included:

Project planning: Helping select a manageable public health research question and identifying CDC PLACES as an appropriate public dataset.

Python development: Assisting with the structure and implementation of src/analyze.py, including data filtering, calculating the average county estimate, and generating the visualization.

Testing: Helping develop three pytest tests to verify filtering, missing-value handling, and alphabetical sorting.

GitHub Actions: Providing guidance and YAML code for automatically running pytest on repository pushes and pull requests.

HPC setup: Assisting with the SLURM batch script, Mamba environment configuration, file transfers, and Great Lakes troubleshooting.

Documentation: Helping organize and draft the README, including the methodology, results, limitations, and reproducibility instructions.

My contributions and verification:

I selected the preventive healthcare topic, downloaded the CDC dataset, created and organized the project files, executed the analysis locally, and inspected the generated outputs. I ran the pytest tests locally and on Great Lakes, verified that GitHub Actions passed, and submitted the analysis through SLURM. I also reviewed the project documentation and addressed errors encountered during setup.

I used AI assistance as a development and learning resource. I am responsible for understanding the submitted code, checking the results, and ensuring that the final project meets the assignment requirements.

AI tool: OpenAI ChatGPT (GPT-6), accessed November 9, 2026.