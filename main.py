import argparse
from dataclasses import asdict

from src.scraper import Scraper
from src.utils import format_city, format_name, format_state

parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, default="", help="city name")
parser.add_argument(
    "--state", type=str, default="", help="supports full and abbreviated forms"
)
parser.add_argument("--name", type=str, required=True, help="full name of the person")
args = parser.parse_args()

state = format_state(args.state)
city = format_city(args.city)
name = format_name(args.name)

scraper = Scraper(name, city, state)
raw_results = scraper.get_raw_results()

if raw_results:
    results = scraper.get_parsed_results(raw_results)
    for result in results:
        result.dump = ""
        print(asdict(result))
else:
    print("No results found")
