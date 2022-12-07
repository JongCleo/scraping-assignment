## Assignment

The site we’d like to scrape: https://www.officialusa.com

Write a scraper that searches for `input name` & `location`, covering the following outcomes:

- find results
- no results found
- error

## Todos

- [] architecture/approach (30 mins)
- [] write main.py (1 hr)
- [] write README (10 mins)
- [] selenium tests (30 mins)

## Setup

You will need to have python3 and pip installed on your system.

First, clone this repo andrun the following command:

```
python3 -m venv venv
```

Next, activate the virtual environment by running the following command:

```
source venv/bin/activate
```

Next, install the necessary packages:

```
pip install requirements.txt
```

To run main.py with the location and name arguments:

```
python main.py --location <location> --name <name>
```

Replace `location` and `name` with the desired values for the arguments.

To run the Selenium testing suite:

```
python -m selenium
```
