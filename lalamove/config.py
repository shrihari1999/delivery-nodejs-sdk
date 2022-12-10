class Config:
    publicKey: str
    privateKey: str
    env: str
    host: str

    def __init__(self, publicKey: str, privateKey: str, env: str = "sandbox") -> None:
        self.publicKey = publicKey
        self.privateKey = privateKey
        self.env = env
        if env == "production":
            self.host = "rest.lalamove.com"
        else:
            self.host = "rest.sandbox.lalamove.com"
