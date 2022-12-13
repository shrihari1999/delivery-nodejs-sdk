# import Quotation from "./quotation"
# import Order from "./order"
# import Driver from "./driver"
from .market import Market
from .city import City
from .config import Config

class Client:
    Config: Config

    # Quotation: Quotation

    # Order: Order

    # Driver: Driver

    Market: Market

    City: City

    def __init__(self, config: Config) -> None:
        self.Config = config
        # self.Quotation = Quotation(config)
        # self.Order = Order(config)
        # self.Driver = Driver(config)
        self.Market = Market(config)
        self.City = City(config)

