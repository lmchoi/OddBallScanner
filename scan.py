from request import Request
from williamhill import WilliamHillService

req = Request()
williamHillService = WilliamHillService()
odds = williamHillService.getOdds(req)
print(odds)


