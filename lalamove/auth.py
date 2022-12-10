from lalamove.models.internal_types import Optional
from .config import Config
import hashlib, hmac

def signRequest(config: Config, method: str, path: str, timestamp: int, body: Optional[str]) -> str:
    rawSignature = str(timestamp) + '\r\n' + method + '\r\n' + path +  '\r\n\r\n'
    if body:
        rawSignature += body
    
    signature = hmac.new(bytes(config.privateKey, 'utf-8'), bytes(rawSignature, 'utf-8'), hashlib.sha256).hexdigest()
    return signature

