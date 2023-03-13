from os import system, name


class Set:
    def __init__(self, data=None):
        self.data = {}
        if data != None: 
            if len(data) != len(set(data)):
                data = set(data)
            for d in data:
                self.data[d] = d
    def insert(self, i):
        if i in self.data.keys():
            return 'Already in set'
        self.data[i] = i
    def remove(self, i):
        if i not in self.data.keys():
            return 'Not in set'
        self.data.pop(i)
    def size(self):
        return len(self.data.keys())
    def contains(self, i):
        if i in self.data.keys():
            return True
        return False
    def union(self, otherSet):
        setData = list(set(self.data.keys()) | set(otherSet.data.keys()))
        unionSet = Set(setData)
        return unionSet
    def intersection(self, otherSet):
        setData = list(set(self.data.keys()) & set(otherSet.data.keys()))
        intersectionSet = Set(setData)
        return intersectionSet
    def difference(self, otherSet):
        setData = list(set(self.data.keys()) ^ set(otherSet.data.keys()))
        differenceSet = Set(setData)
        return differenceSet
    def subset(self, otherSet):
        if set(self.data.keys()) < set(otherSet.data.keys()):
            return True
        return False
    def __repr__(self):
      return '['+', '.join(str(x) for x in self.data.keys())+']'

print("\t \t Assignment No 2: Abstract Set Class")
print("\t \t Created by Advait Pandharpurkar")

A = Set([1,2,3,4,5,6])
B = Set([4,5,6,7,8,9])
while True:
    print("Main Menu")
    print("1. Add an element to set")
    print("2. Remove an element from the set")
    print("3. Size of a set")
    print("4. Union of the sets")
    print("5. Intersectino of the sets")
    print("6. Subset of the set")
    choice = int(input("Your choice => "))
    if choice == 1:
        print("A = ",A)
        print("Enter elem ot be added :- ")
        num = int(input())
        A.insert(num)
    if choice == 2:
        print("A = ",A)
        print("Enter elem to be removed :- ")
        num = int(input())
        A.remove(num)
    if choice == 3:
        print("Size of set A = ",A.size())
    if choice == 4:
        print("Set A = ",A)
        print("Set B = ",B)
        print("Union = ", A.union(B))
    if choice == 5:
        print("Set A = ",A)
        print("Set B = ",B)
        print("Intersection = ", A.intersection(B))
    if choice == 6:
        if A.subset(B) == True:
            print("Yes it's subset")
        else:
            print("It's not subset")
    if choice == 7:
        print("Exiting :) ")
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        break
    print("\n",'*' * 50, "\n")
