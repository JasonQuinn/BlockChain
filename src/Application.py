from uuid import uuid4

from flask import Flask, Response, request

from classes.dto.BlockChain import BlockChain
from src.classes.BlockMiner import BlockMiner
from src.classes.JsonEncoder import JsonEncoder

app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')
# Create the chain
blockChain = BlockChain()
block_miner = BlockMiner()


@app.route('/mine', methods=['GET'])
def mine():
    new_proof = block_miner.find_proof_of_work(blockChain.last_block.proof)

    blockChain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    new_block = blockChain.new_block(new_proof)

    new_block_json = JsonEncoder().encode(new_block),
    return Response(new_block_json, mimetype='text/json', status=201)


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockChain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': F'Transaction will be added to Block {index}'}
    return Response(JsonEncoder().encode(response), status=201)


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'block': blockChain.chain,
        'length': len(blockChain.chain)
    }
    response_string = JsonEncoder().encode(response)
    return Response(response_string, mimetype='text/json')


if __name__ == '__main__':
    app.run()
