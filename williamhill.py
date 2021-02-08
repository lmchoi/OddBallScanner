from request import Request
from odds import Odds
from typing import List

WILLIAM_HILL_URL = "https://sports.williamhill.com/betting/en-gb/basketball#"


class WilliamHillService:
    def getOdds(self, req) -> List[Odds]:
        driver = req.get(WILLIAM_HILL_URL)
        moneyLineElements = driver.find_elements_by_xpath(
            '//span[@data-market-group="Money Line"]')
        return list(map(lambda ml: Odds(ml.get_attribute('data-player'), ml.get_attribute('data-odds')), moneyLineElements))
