from dataclasses import dataclass
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from .utils import log_error, log_info


@dataclass
class Person:
    name: str
    location: str
    description: str
    address_details: List[str]
    phones: List[str]
    emails: List[str]
    dump: str


class Scraper:
    def __init__(self, name: str, city: str, state: str):
        self.name = name
        self.city = city
        self.state = state
        # TODO: apply dependency inversion, current implementation couples selenium-isms with scraping logic

        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.execute_cdp_cmd(
            "Network.setUserAgentOverride",
            {"userAgent": self._generate_random_user_agent()},
        )
        log_info("Scraper initialized")

    def _generate_random_user_agent(self) -> str:

        return ""

    def _apply_location_filters(self) -> None:
        if self.state:
            ul = self.driver.find_element(
                By.XPATH, "//span[contains(text(), 'by State')]/following-sibling::ul"
            )
            ul.find_element(
                By.XPATH, f"//label[contains(text(), '{self.state}')]"
            ).click()
        if self.city:
            ul = self.driver.find_element(
                By.XPATH, "//span[contains(text(), 'by City')]/following-sibling::ul"
            )
            ul.find_element(
                By.XPATH, f"//label[contains(text(), '{self.city}')]"
            ).click()

    def get_raw_results(self) -> str:
        try:
            self.driver.get(f"https://www.officialusa.com/names/{self.name}")
        except Exception as e:
            log_error(f"Request failed, try again later:{e}")
            return ""

        if "page not found" in self.driver.title.lower() or "404" in self.driver.title:
            log_error(f"{self.name} is not a valid name")
            return ""

        if self.city or self.state:
            try:
                self._apply_location_filters()
            except Exception as e:
                log_error(f"Error applying location filters:{e}")
                return ""

        return self.driver.page_source

    def get_parsed_results(self, source: str) -> List[Person]:
        soup = BeautifulSoup(source, "html.parser")
        results = []

        for result in soup.find_all("div", itemprop="Person"):
            if "display: none;" in result.attrs.get("style"):
                continue
            name = (
                result.find("div", class_="detail-block__main-item-name")
                .find("h2")
                .text
            )
            try:
                location = (
                    result.find("div", class_="detail-block__main-item-name")
                    .find("span", itemprop="address")
                    .text
                )
            except AttributeError:
                location = ""

            try:

                description = (
                    result.find("div", class_="detail-block__main-item-content")
                    .find("p")
                    .text
                )
            except AttributeError:
                description = ""

            try:
                address_details = [
                    address_details.text
                    for address_details in result.find(
                        "div", class_="detail-block__main-item-block-title"
                    )
                    .parent.find_next_sibling("ul")
                    .find_all("li")
                ]
            except AttributeError:
                address_details = []

            try:

                phones = [
                    phone.text
                    for phone in result.find_all("span", itemprop="telephone")
                ]
            except AttributeError:
                phones = []

            try:
                emails = [
                    email.text for email in result.find_all("span", itemprop="email")
                ]
            except AttributeError:
                emails = []
            dump = result.prettify()
            results.append(
                Person(
                    name, location, description, address_details, phones, emails, dump
                )
            )
        return results
