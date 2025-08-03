# Simple prototype for AmbarCoin blockchain (PoS-like simulation)

class Block:
    def __init__(self, index, previous_hash, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        import hashlib
        block_string = str(self.index) + self.previous_hash + str(self.transactions) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", [])
        self.chain.append(genesis_block)

    def latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_hash = self.latest_block().hash
        new_block = Block(len(self.chain), previous_hash, transactions)
        self.chain.append(new_block)
        return new_block

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block(["Tx1: AmbarCoin transfer from A to B"])
    blockchain.add_block(["Tx2: AmbarCoin transfer from C to D"])

    for block in blockchain.chain:
        print(f"Block {block.index} with hash: {block.hash}")
