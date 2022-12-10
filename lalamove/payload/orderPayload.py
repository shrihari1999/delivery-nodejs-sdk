from lalamove.models.internal_types import Union, List, Optional
from lalamove.models.sender import Sender
from lalamove.models.recipient import Recipient

class OrderPayload:
    __quotationId: Union[str, None]

    __sender: Union[Sender, None]

    __recipients: Union[List[Recipient], None]

    __isPODEnabled: Optional[bool]

    __isRecipientSMSEnabled: Optional[bool]

    __partner: Optional[str]

    __metadata: Optional[dict]

    def __init__(self, opb):
        if opb.quotationId is None:
            raise Exception("QuotationID cannot be empty")
        
        if opb.sender is None:
            raise Exception("Sender cannot be empty")
        
        if opb.recipients is None:
            raise Exception("recipients cannot be empty")
        
        self.__quotationId = opb.quotationId
        self.__sender = opb.sender
        self.__recipients = opb.recipients
        self.__isPODEnabled = opb.isPODEnabled
        self.__isRecipientSMSEnabled = opb.isRecipientSMSEnabled
        self.__partner = opb.partner
        self.__metadata = opb.metadata

