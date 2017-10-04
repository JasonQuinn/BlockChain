import time

from src.classes.dto.Block import Block
from src.classes.BlockChainValidator import BlockChainValidator
from src.classes.dto.Transaction import Transaction


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        # Creat 1st block
        self.new_block(100, 1)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new Block and adds it to the chain
        :param proof:
        :param previous_hash:
        :return:
        """
        block = Block(len(self.chain) + 1, proof, self.new_transactions, str(time.time()),
                      previous_hash or self.last_block.hash())
        self.new_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions
        :param sender:
        :param recipient:
        :param amount:
        :return:int
        """
        self.new_transactions.append(Transaction(sender, recipient, amount))
        return self.last_block.index + 1

    @property
    def last_block(self):
        """
        Returns the last Block in the chain
        """
        return self.chain[-1]

    def find_proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while not BlockChainValidator.valid_proof(last_proof, proof):
            proof = proof + 1
        return proof
