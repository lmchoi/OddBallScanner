from request import Request
from williamhill import WilliamHillService
from smarkets import SmarketsService
from oddschecker import OddsCheckerService

req = Request()
# williamHillService = WilliamHillService()
# smarketsService = SmarketsService()

# williamHillOdds = williamHillService.getOdds(req)
# print(williamHillOdds)

# contracts = smarketsService.getContracts(req)
# print(contracts)

oddscheckerService = OddsCheckerService()
odds = oddscheckerService.getOdds(req)

for o in odds:
    print(o)    
