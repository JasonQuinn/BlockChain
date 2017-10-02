from flask import Flask, jsonify

from classes.BlockChain import BlockChain

app = Flask(__name__)

blockChain = BlockChain()


@app.route('/mine', methods=['GET'])
def mine():
    new_proof = blockChain.find_proof_of_work(blockChain.last_block['proof'])
    new_block = blockChain.new_block(new_proof)

    return jsonify(new_block)


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'block': blockChain.chain,
        'length': len(blockChain.chain)
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
