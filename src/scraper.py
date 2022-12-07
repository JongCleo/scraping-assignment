from dataclasses import dataclass
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver


@dataclass
class Person:
    name: str
    location: str
    description: str
    address_details: str
    phones: List[str]
    emails: List[str]


class Scraper:
    def __init__(self, name: str, city: str, state: str):
        self.name = name
        self.city = city
        self.state = state
        # TODO: apply dependency inversion, current implementation couples selenium-isms with scraping logic
        self.driver = webdriver.Chrome()
        self.driver.execute_cdp_cmd(
            "Network.setUserAgentOverride", {"userAgent": self._get_random_user_agent()}
        )

    def _get_random_user_agent(self) -> str:
        return ""

    def get_results(self) -> List[Person]:
        # TODO: why would this not work? what exceptions should I be catching?
        self.driver.get(f"https://www.officialusa.com/names/{name}")

        if self.driver.title.lower() == "page not found" or "404" in self.driver.title:
            return []

        # if there's a valid city or state, filter by it (change page state)
        if self.city or self.state:
            pass

        # load page state into bs4 and process into Person data class

        return []
