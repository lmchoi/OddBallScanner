from request import Request
from odds import Odds
from typing import List

ODDSCHECKER_URL = "https://www.oddschecker.com/basketball/nba"
# //p[contains(@class, "fixtures-bet-name")]
# //div[@id="fixtures"]//span[contains(@class, "odds") and contains(@class, "add-to-bet-basket")]
class OddsCheckerService:
    def getOdds(self, req) -> List[Odds]:
        driver = req.get(ODDSCHECKER_URL)
        fixtures_element = driver.find_element_by_id('fixtures')
        name_elements = fixtures_element.find_elements_by_css_selector('p.fixtures-bet-name')
        odds_elements = fixtures_element.find_elements_by_css_selector('span.odds.add-to-bet-basket')
        
        # TODO check length
        odds_tuples = zip(name_elements, odds_elements)

        return list(map(lambda ot: Odds(ot[0].text, ot[1].text), odds_tuples))
