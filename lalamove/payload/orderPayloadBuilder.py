from .orderPayload import OrderPayload
from lalamove.models.internal_types import Union, List, Optional
from lalamove.models.sender import Sender
from lalamove.models.recipient import Recipient

class OrderPayloadBuilder:
    __quotationId: Union[str, None]

    __sender: Union[Sender, None]

    __recipients: Union[List[Recipient], None]

    __isPODEnabled: Optional[bool]

    __isRecipientSMSEnabled: Optional[bool]

    __partner: Optional[str]

    __metadata: Optional[dict]

    @staticmethod
    def orderPayload() -> None:
        return OrderPayloadBuilder()

    def withQuotationID(self, quotationId: str) -> None:
        self.__quotationId = quotationId
        return self

    def withSender(self, sender: Sender) -> None:
        self.__sender = sender
        return self

    def withRecipients(self, recipients: List[Recipient]) -> None:
        self.__recipients = recipients
        return self

    def withIsPODEnabled(self, isPodEnabled: bool) -> None:
        self.__isPODEnabled = isPodEnabled
        return self

    def withIsRecipientSmsEnabled(self, isRecipientSMSEnabled: bool) -> None:
        self.__isRecipientSMSEnabled = isRecipientSMSEnabled
        return self

    def withPartner(self, partner: str) -> None:
        self.__partner = partner
        return self

    def withMetadata(self, metadata: object) -> None:
        self.__metadata = metadata
        return self

    def build(self) -> OrderPayload:
        return OrderPayload(self)
