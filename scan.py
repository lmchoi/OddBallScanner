from request import Request
from williamhill import WilliamHillService
from smarkets import SmarketsService
from oddschecker import OddsCheckerService


def print_element_in_list(l):
    for e in l:
        print(e)


def divide_into_pairs(l):
    n = 2
    for i in range(0, len(l), n):
        yield l[i:i + n]


def find_arbs(game):
    odds = game[0]
    contract = game[1]
    print(game)
    print(odds[0])
    print(odds[1])
    print(contract[0])
    print(contract[1])

req = Request()
williamHillService = WilliamHillService()
smarketsService = SmarketsService()

odds = williamHillService.get_odds(req)
game_odds = list(divide_into_pairs(odds))

# https://docs.python.org/3/tutorial/datastructures.html#dictionaries use dictionaries to store odds/contracts for faster retrieval

contracts = smarketsService.getContracts(req)

game_contracts = list(divide_into_pairs(contracts))
list(map(lambda g: find_arbs(g), zip(game_odds, game_contracts)))

# oddscheckerService = OddsCheckerService()
# odds = oddscheckerService.getOdds(req)
