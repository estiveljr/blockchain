from hashlib import sha256
from datetime import datetime


class block():
    def __init__(self, index, data):
        super().__init__()

        self.index = int(index)
        self.data = str(data)
        self.timestamp = datetime.now().__str__()
        self.hash = self.__generate_hash(self.index,self.data)

    def __generate_hash(self,index,data):
        hash_content = (str(index) + str(data)).encode('utf-8')
        hash = sha256(hash_content)
        return hash


class blockchain():
    def __init__(self,dificulty):
        super().__init__()
        self.index = 0
        self.dificulty = dificulty
        self.genesis_block = block(index=0,data="i'm the beginning")
        self.blocks = [self.genesis_block]

    def add_block(self,data):
        self.index += 1 
        self.blocks.append(block(self.index,data=data))
        

    def validate(self):
        return 0
    

if __name__ == '__main__':
    bl = blockchain(10)
    bl.add_block('segundo bloco')


for b in bl.blocks:
    print(b.index)