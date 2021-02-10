'''WilliamHillService'''

from typing import List
from odds import Odds


WILLIAM_HILL_URL = "https://sports.williamhill.com/betting/en-gb/basketball#"


class WilliamHillService:
    '''interact with WH page'''

    def get_odds(self, req) -> List[Odds]:
        '''get odds'''
        driver = req.get(WILLIAM_HILL_URL)
        money_line_elements = driver.find_elements_by_xpath(
            '//span[@data-market-group="Money Line"]')
        return list(map(lambda ml: Odds(ml.get_attribute('data-player'), ml.get_attribute('data-odds')), money_line_elements))
