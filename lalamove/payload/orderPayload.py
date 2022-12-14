from lalamove.models.internal_types import Union, List, Optional
from lalamove.models.sender import Sender
from lalamove.models.recipient import Recipient

class OrderPayload:
    quotationId: Union[str, None]

    sender: Union[Sender, None]

    recipients: Union[List[Recipient], None]

    isPODEnabled: Optional[bool]

    isRecipientSMSEnabled: Optional[bool]

    partner: Optional[str]

    metadata: Optional[dict]

    def __init__(self, opb):
        if opb.quotationId is None:
            raise Exception("QuotationID cannot be empty")
        
        if opb.sender is None:
            raise Exception("Sender cannot be empty")
        
        if opb.recipients is None:
            raise Exception("recipients cannot be empty")
        
        self.quotationId = opb.quotationId
        self.sender = opb.sender
        self.recipients = opb.recipients
        
        if getattr(opb, 'isPODEnabled', None) is not None:
            self.isPODEnabled = opb.isPODEnabled
        
        if getattr(opb, 'isRecipientSMSEnabled', None) is not None:
            self.isRecipientSMSEnabled = opb.isRecipientSMSEnabled
        
        if getattr(opb, 'partner', None) is not None:
            self.partner = opb.partner
        
        if getattr(opb, 'metadata', None) is not None:
            self.metadata = opb.metadata

