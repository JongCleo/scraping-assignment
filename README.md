## Assignment

The site we’d like to scrape: https://www.officialusa.com

Write a scraper that searches for `input name` & `location`, covering the following outcomes:

- find results
- no results found
- error

## Research

I poked around the network tab on the officialusa site and found the `/names/<name>` endpoint which looks like our main entry point. Some observations:

- it returns HTML (instead of JSON, hence the need for scraping which makes sense)
- Location filtering appears to happen entirely on the client side and it has facets for state and city.
- spaces between the first and last name are represented as hyphens (on opposed to being url-encoded) which means we should escape it when it's naturally occurring like compound last names ex. "bankman-fraud".
- the name is expected to be in the strict format "first last" but will produce results with middle names and suffixes. See "Walter Karl Baade JR" under https://www.officialusa.com/names/Walter-Baade/ The query for names/Walter-Karl-Baade-JR yields no results.

What's uncertain is what happens when there are multiple pages of results. I tried the champion of generic asian names "kevin nguyen" but yielded no results. The max number of results I could find

## Approach

main.py

- parses and sanitzes arguments and calls the scraper

scraper.py

- method to open selenium browser
- method to attempt location filtering
- robustness: retries/timeouts, rotate user agent etc.
- error handling

utils.py

- helpers to santize inputs

While it's less elegant for the consumer, I'll split the location argument (ie. they will have to specify the state and city separately). I'm also making the assumption that we're not using lat, long or zipcodes.

## Todos

- [x] architecture/approach (45 mins)
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
python main.py --name <name> --city <city>  --state <state>
```

Replace `city` `state` and `name` with the desired values for the arguments.

To run the Selenium testing suite:

```
python -m selenium
```
