from .orderPayload import OrderPayload
from lalamove.models.internal_types import Union, List, Optional
from lalamove.models.sender import Sender
from lalamove.models.recipient import Recipient

class OrderPayloadBuilder:
    quotationId: Union[str, None]

    sender: Union[Sender, None]

    recipients: Union[List[Recipient], None]

    isPODEnabled: Optional[bool]

    isRecipientSMSEnabled: Optional[bool]

    partner: Optional[str]

    metadata: Optional[dict]

    @staticmethod
    def orderPayload() -> None:
        return OrderPayloadBuilder()

    def withQuotationID(self, quotationId: str) -> None:
        self.quotationId = quotationId
        return self

    def withSender(self, sender: Sender) -> None:
        self.sender = sender
        return self

    def withRecipients(self, recipients: List[Recipient]) -> None:
        self.recipients = recipients
        return self

    def withIsPODEnabled(self, isPodEnabled: bool) -> None:
        self.isPODEnabled = isPodEnabled
        return self

    def withIsRecipientSmsEnabled(self, isRecipientSMSEnabled: bool) -> None:
        self.isRecipientSMSEnabled = isRecipientSMSEnabled
        return self

    def withPartner(self, partner: str) -> None:
        self.partner = partner
        return self

    def withMetadata(self, metadata: object) -> None:
        self.metadata = metadata
        return self

    def build(self) -> OrderPayload:
        return OrderPayload(self)
