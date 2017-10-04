from src.classes.BlockChainValidator import BlockChainValidator

block_chain_validator = BlockChainValidator()


class BlockMiner:
    def find_proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while not block_chain_validator.validate_proof(last_proof, proof):
            proof = proof + 1
        return proof
