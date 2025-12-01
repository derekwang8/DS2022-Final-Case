# 1) Executive Summary

## Problem:
Coaches and analysts in competitive Wushu often lack a simple way to explore athlete performance data. Accessing structured information—such as scoring distributions, top-performing countries, and event breakdowns—typically require full database setups.

## Solution:
This project provides a lightweight, containerized analytics API built using Flask, SQLite, and Docker. The system automatically loads the IWUF WWC17 competition dataset from CSV, creates a SQL database, and exposes two clean API endpoints for quick data exploration:

/athletes — browse athlete rows

/summary — view computed statistics (averages, top countries, total athletes)

The entire system runs from a single Docker command, ensuring portability and reproducibility.

# 2) System Overview
## Course Concepts Used

SQL database integration (SQLite, schema creation, SQL queries)

ETL pipeline (CSV → SQLite)

Flask API development

Containerization with Docker

Reproducible environment & deployment

## Data / Models / Services


### Dataset:

File: assets/WWC17.csv

Rows: 216 athletes

Columns include: Name, Country, Overall Score, A/B/C Scores, Event, Gender, Region

License: MIT License

### Tech Stack:

Python 3.11

Flask 3.0

SQLite

Docker (Python 3.11-slim base image)

# 3) How to Run (Local)
## Docker
### Build
docker build -t wushu-api .

### Run
docker run --rm -p 8080:8080 wushu-api

## Example Requests

### Health Check:

http://localhost:8080/health


### First 5 athletes:

http://localhost:8080/athletes

### Summary analytics:

http://localhost:8080/summary

# 4) Design Decisions
## Why SQLite?

Zero-configuration

Fits perfectly inside Docker

Ideal for small to medium datasets like WWC17

Fast and reliable for read-heavy analytics

## Why Flask?

Lightweight

Easy to containerize

Clean routing for simple APIs

## Tradeoffs

SQLite is not built for large concurrency

The API is read-only (no POST/PUT) to keep scope simple

Statistical summary uses basic SQL (no advanced analytics)

## Security / Privacy

No secrets included

.env.example provided

SQL queries use parameterized inputs

Dataset contains no private PII

## Ops Considerations

Logging via default Flask logger

API is stateless; rebuilding docker image resets DB

Extremely small resource footprint (<50MB image)

# 5) Results & Evaluation
## Sample Output — /athletes
[
  {
    "Name": "Zhizhao Chang",
    "Country": "CHN",
    "Overall_Score": 9.7,
    "Rank": 1,
    "A_Score": 5.0,
    "B_Score": 2.7,
    "C_Score": 2.0,
    "Time": 1.40,
    "PlaceCat": "Gold",
    "Region": "China",
    "Event": "Changquan (Longfist)",
    "Gender": "M",
    "B_Score_Cat": "Superior",
    "A_Ded_Cnt": 0,
    "Nandu_Miss": 0,
    "Nandu_Total": 9,
    "Nandu_Completed": "100%"
  }
]

## Sample Output — /summary
{
  "total_athletes": 216,
  "average_scores": {
    "overall": 9.453,
    "A": 4.917,
    "B": 2.536,
    "C": 2.0
  },
  "top_countries": [
    {"Country": "CHN", "count": 28},
    {"Country": "JPN", "count": 22},
    {"Country": "MAS", "count": 20},
    {"Country": "VIE", "count": 18},
    {"Country": "INA", "count": 16}
  ]
}

## Validation

### A simple smoke test verifies that the database contains rows:

python -m pytest

# 6) What’s Next

## Potential improvements:

Add /search?name=... for fuzzy athlete lookups

Add /event-stats?event=Changquan

Add /country/<name> breakdowns

# 7) Links (Required)

GitHub Repo: https://github.com/derekwang8/DS2022-Final-Case
Public Cloud URL (optional): https://wushu-api.onrender.com
## Available API endpoints:

### Health Check
https://wushu-api.onrender.com/health

### Summary Statistics
https://wushu-api.onrender.com/summary

### Athlete List
https://wushu-api.onrender.com/athletes