import hashlib
import json
from time import time
from hash import generateHash

class BlockChain():
    def __init__(self):
        self.chain = []
        

    def addBlock(self, newBlock):
        # Check if length of chain is 0 and call createGenesisBlock() method
        
            # Set newBlock.index to 1
            
        # Set cureenthash of last block as previous hash     
        newBlock.previousHash = ""
        newBlock.currentHash = newBlock.calculateHash()
        self.chain.append(newBlock)
    
    # Create a method createGenesisBlock
    
        # Create a new block using Block class with index 0, current time, empty transaction and no previous hash
        
        # Append the block tot the chain
        
        
        
class Block:
    def __init__(self, index, timestamp, transaction, previousHash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
        self.isValid = None
       
    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp

        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transaction)
        return generateHash(blockString)

       
