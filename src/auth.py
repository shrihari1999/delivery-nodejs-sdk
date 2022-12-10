from config import Config
import hashlib, hmac

def signRequest(config: Config, method: str, path: str, timestamp: int, body: str) -> str:
    rawSignature = str(timestamp) + '\r\n' + method + '\r\n' + path +  '\r\n\r\n'
    if body:
        rawSignature += body
    
    signature = hmac.new(bytes(config.privateKey, 'utf-8'), bytes(rawSignature, 'utf-8'), hashlib.sha256).hexdigest()
    return signature

