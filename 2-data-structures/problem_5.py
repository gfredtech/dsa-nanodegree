import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return f'data: {self.data}\nhash: {self.hash}\ntimestamp: {self.timestamp}\nprev_hash: {self.previous_hash}'


class Node:
    def __init__(self, data, prev_hash):
        self.block = Block(datetime.utcnow(), data, prev_hash)
        self.next = None
        self.tail = None


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if data is None:
            return

        if self.head is None:
            genesis_hash = hashlib.sha256()
            genesis_hash.update("GENESIS".encode('utf-8'))
            self.head = Node(data, genesis_hash.hexdigest())
            self.tail = self.head

        else:
            self.tail.next = Node(data, self.tail.block.hash)
            self.tail = self.tail.next

    def traverse(self):
        if self.head is None:
            print("Empty block chain\n")
        else:
            curr_node = self.head
            while curr_node:
                print(curr_node.block)
                print()
                curr_node = curr_node.next


if __name__ == '__main__':
    # Test 1
    blockChain = BlockChain()
    blockChain.add("A")
    blockChain.add("B")
    blockChain.add("C")
    blockChain.add("D")
    blockChain.traverse()

    # Test 2
    block_chain = BlockChain()
    block_chain.traverse()  # expected output: Block Chain is empty

    # Test 3
    block_chain = BlockChain()

    block_chain.add(None)
    block_chain.add("1 block")
    block_chain.add(None)

    block_chain.traverse()  # expected output: prints 1 block only
