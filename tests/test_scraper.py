# import scraper from scraper.py
# import format_city, format_name, format_state from utils.py
from src.scraper import Scraper


def test_valid_name_no_location(scraper):
    scraper.name = "Aissatou-Ba"
    scraper.city = ""
    scraper.state = ""
    results = scraper.get_parsed_results(scraper.get_raw_results())
    assert len(results) > 0


def test_valid_name_valid_city(scraper):
    scraper.name = "Aissatou-Ba"
    scraper.city = "Columbus"
    scraper.state = ""
    results = scraper.get_parsed_results(scraper.get_raw_results())
    assert len(results) > 0


def test_valid_name_valid_state(scraper):
    scraper.name = "Aissatou-Ba"
    scraper.city = ""
    scraper.state = "New York"
    results = scraper.get_parsed_results(scraper.get_raw_results())
    assert len(results) > 0


def test_valid_name_valid_city_and_state(scraper):
    scraper.name = "Aissatou-Ba"
    scraper.city = "Memphis"
    scraper.state = "Tennessee"
    results = scraper.get_parsed_results(scraper.get_raw_results())
    assert len(results) > 0


# Failed and No Results
def test_invalid_name(scraper):
    scraper.name = "kajsdhsada"
    scraper.city = ""
    scraper.state = ""
    results = scraper.get_raw_results()
    assert results == ""


def test_valid_name_invalid_city(scraper):
    scraper.name = "Aissatou-Ba"
    scraper.city = "kajsdhajksdh"
    scraper.state = ""
    results = scraper.get_raw_results()
    assert results == ""


def test_valid_name_invalid_state(scraper):
    scraper.name = "Aissatou-Ba"
    scraper.city = ""
    scraper.state = "kajsdhajksdh"

    results = scraper.get_raw_results()
    assert results == ""
