from .config import Config

class Base:
    config: Config

    def __init__(self, config: Config) -> None:
        self.config = config

    def getConfig(self) -> Config:
        return self.config

