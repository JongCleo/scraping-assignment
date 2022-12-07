import pytest

from src.scraper import Scraper


@pytest.fixture(scope="session")
def scraper():
    scraper = Scraper(
        "",
        "",
        "",
    )
    return scraper
