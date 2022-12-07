import argparse

from scraper import Scraper
from utils import format_city, format_state

parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, default="", help="city name")
parser.add_argument(
    "--state", type=str, default="", help="supports full and abbreviated forms"
)
parser.add_argument("--name", type=str, required=True, help="full name of the person")
args = parser.parse_args()

state = format_state(args.state)
city = format_city(args.city)

scraper = Scraper(city, state, args.name)
results = scraper.get_results()
print(results)
