from request import Request
from williamhill import WilliamHillService
from smarkets import SmarketsService

req = Request()
williamHillService = WilliamHillService()
smarketsService = SmarketsService()

williamHillOdds = williamHillService.getOdds(req)
print(williamHillOdds)

contracts = smarketsService.getContracts(req)
print(contracts)


