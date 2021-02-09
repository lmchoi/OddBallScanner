# from selenium.webdriver.support.relative_locator import with_tag_name
from request import Request
from odds import Odds
from contract import Contract
from typing import List
import time
SMARKETS_URL = "https://smarkets.com/listing/sport/basketball/nba"


class SmarketsService:
    def extractContract(self, contract_element):
        name = contract_element.find_element_by_class_name(
            'contract-label').text
        buy_price = contract_element.find_element_by_css_selector(
            "span.price.buy").text
        sell_price = contract_element.find_element_by_css_selector(
            "span.price.sell").text
        return Contract(name, buy_price, sell_price)

    def extractContractFromTuple(self, name_buy_sell_tup):
        return Contract(name_buy_sell_tup[0].text, name_buy_sell_tup[1].text, name_buy_sell_tup[2].text)

    def getContracts(self, req) -> List[Contract]:
        driver = req.get(SMARKETS_URL)
        time.sleep(2)
        name_elements = driver.find_elements_by_class_name('contract-label')
        buy_elements = driver.find_elements_by_css_selector("span.price.buy")
        sell_elements = driver.find_elements_by_css_selector("span.price.sell")
        
        # TODO check length
        contract_tuples = zip(name_elements, buy_elements, sell_elements)

        return list(map(lambda tup: self.extractContractFromTuple(tup), contract_tuples))
