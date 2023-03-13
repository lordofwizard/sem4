#create a abstract data type that implements the set concept.
# Add new element 
# To create ADT that implement the "set" concept.
# a. Add (newElement) -Place a value into the set
# b. Remove (element) Remove the value
# c. Contains (element) Return true if element is in collection
# d. Size () Return number of values in collection Iterator () Return an iterator used to loop
# over collection
# e. Intersection of two sets
# f. Union of two sets
# g. Difference between two sets
# h.Subset

def create_set():
    my_set = []
    choice = 'y'
    while(choice[0] == 'y'):
        print("\n Enter the number: ")
        num = int(input())
        my_set.append(num)
        print("\n Do you want to enter more number? (y/n)")
        choice = input()
    return my_set

def add_element()
