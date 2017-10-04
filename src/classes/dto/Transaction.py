from src.classes.dto.Serializable import Serializable


class Transaction(Serializable):
    def __init__(self, sender, recipient, amount):
        super().__init__()
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
