import argparse

from .scraper import Scraper
from .utils import format_city, format_name, format_state

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
results = scraper.get_results()
print(results)
