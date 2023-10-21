# RAM Monitoring Application

A simple RAM monitoring application that collects RAM statistics from a Linux system and provides an API to retrieve the data. It stores the total, free, and used values related to the RAM in MB per minute in an SQLite database.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Collecting RAM Statistics](#collecting-ram-statistics)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- `pip` package manager

### Installation

1. Clone the repository:

    `git clone https://github.com/mlk-dev/ram_stats.git`

2. Navigate to the project directory:

    `cd ram-monitor`

3. Install the project dependencies:

    `pip install -r requirements.txt`


## Usage

### Collecting RAM Statistics

You can start collecting RAM statistics by running the `ram_monitor.py` script:

    `python backend/ram_monitor.py`


This script will periodically collect RAM statistics and store them in the SQLite database.

### API Endpoints

- The FastAPI application provides an API to retrieve RAM statistics.
- To access the API, run the FastAPI server:

    `uvicorn api.main:app --host 0.0.0.0 --port 8000`

    You can access the API at

    `http://localhost:8000/ram_stats/`.

- To retrieve the last `n` RAM statistics records in JSON format, use the following endpoint:

    `GET /ram_stats/?n=10` (Replace `10` with the desired number of records)

## Testing

To run tests, use the following command:

    `pytest`

Please ensure that you have set up the project and dependencies as mentioned in the Installation section before running tests.

## Project Structure

The project directory structure is organized as follows:


    ├── api
        ├── main.py
    ├── backend
        └── ram_monitor.py
    ├── db
        ├── database.py
        └── ram_stats.db
    ├── tests
        ├── api_test.py
        └── backend_test.py
    ├── requirements.txt
    └── README.md
