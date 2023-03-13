class Contact:
    def __init__(self, username, phone_number):
        self.username = username
        self.phone_number = phone_number

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return ((ord(key[0])-65)+(len(key)-1)) % 10
    
    def linear_probing(self, key, i):
        return (self.hash_function(key) + i) % self.size
    
    def insert(self, contact):
        i = 0
        while i < self.size:
            index = self.linear_probing(contact.username, i)
            if not self.table[index]:
                self.table[index] = contact
                return
            i += 1
        raise Exception("HashTable is full.")
    
    def search(self, username):
        i = 0
        while i < self.size:
            index = self.linear_probing(username, i)
            if self.table[index] and self.table[index].username == username:
                return self.table[index].phone_number
            i += 1
        return None

contact_db = HashTable(1000)

contact_db.insert(Contact("Advait", 1234567890))
contact_db.insert(Contact("Indrawadan", 2345678901))
contact_db.insert(Contact("Nikhil", 3456789012))

print(contact_db.search("Advait"))
print(contact_db.search("Indrawadan"))
print(contact_db.search("Nikhil"))
print(contact_db.search("Nitin"))
