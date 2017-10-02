import hashlib
import json
import time


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
        block = {
            'index': len(self.chain) + 1,
            'proof': proof,
            'transactions': self.new_transactions,
            'timetamp': str(time.time()),
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
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
        self.new_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Hashes a Block
        :rtype: str
        :param block:
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

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
        while not self.valid_proof(last_proof, proof):
            proof = proof + 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        merged_proofs = ('%s %s' % (last_proof, proof)).encode()
        guess_hash = hashlib.sha256(merged_proofs).hexdigest()
        return guess_hash[:4] == '0000'
