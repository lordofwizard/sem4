class Hashing:
    def __init__(self):
        self.size = int(input("Enter Size of Hash Table : "))
        self.HashTable = list(0 for i in range(self.size))
        self.num_of_elements = 0
        self.comparisons = 0

    def isTableFull(self):
        if self.num_of_elements == self.size:
            return True
        else:
            return False

    def hashFunction(self,elem):
        return elem % self.size

    def insertElement_Linear(self,elem):
        if self.isTableFull():
            print("Hash Table Full")
            return False
        occupiedStatus = False
        position  = self.hashFunction(elem)
        if self.HashTable[position] == 0:
                      self.HashTable[position] = elem
            print("Telephone Number " + str(elem) + " at -> " + str(position))
            occupiedStatus = True
            self.num_of_elements += 1
        else:
            print("Collision :(")
            print(f'{str(elem)} at index {str(position)}')
            position = self.LinearProbing(elem,position)
            self.HashTable[position] = elem
            occupiedStatus = True
            self.num_of_elements += 1
        return occupiedStatus

    def insert
