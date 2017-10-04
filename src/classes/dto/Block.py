import hashlib

from src.classes.JsonEncoder import JsonEncoder
from src.classes.dto.Serializable import Serializable


class Block(Serializable):
    def __init__(self, index, proof, transactions, timetamp, previous_hash):
        super().__init__()
        self.previous_hash = previous_hash
        self.timetamp = timetamp
        self.index = index
        self.proof = proof
        self.transactions = transactions

    def hash(self):
        """
        Hashes a Block
        :rtype: str
        :param block:
        """
        block_string = JsonEncoder().encode(self)
        return hashlib.sha256(block_string.encode()).hexdigest()
