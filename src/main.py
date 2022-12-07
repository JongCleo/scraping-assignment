import argparse

from scraper import Scraper
from utils import format_city, format_state

parser = argparse.ArgumentParser()
parser.add_argument("city", help="city name")
parser.add_argument("state", help="supports full and abbreviated forms")
parser.add_argument("name", help="full name of the person")
args = parser.parse_args()

if not args.name:
    print("Name cannot be empty")
    exit(1)

state = format_state(args.state)
city = format_city(args.city)

scraper = Scraper(city, state, args.name)
results = scraper.get_results()
print(results)
