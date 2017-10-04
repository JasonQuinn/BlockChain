import hashlib


class BlockChainValidator:
    @staticmethod
    def validate_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        merged_proofs = ('%s %s' % (last_proof, proof)).encode()
        guess_hash = hashlib.sha256(merged_proofs).hexdigest()
        return guess_hash[:4] == '0000'
