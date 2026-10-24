class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.array = [None] * 10

    def hash(self, key):
        total = 0
        for letter in key:
            total = total + ord(letter)
        return total % 10

    def put(self, key, value):
        index = self.hash(key)
        new_node = Node(key, value)
        if self.array[index] == None:
            self.array[index] = new_node
        else:
            new_node.next = self.array[index]
            self.array[index] = new_node

    def get(self, key):
        index = self.hash(key)
        current = self.array[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        

main = HashTable()
print(main.hash("cat"))
print(main.hash("act"))
main.put("cat",123)
main.put("act",456)
print(main.get("cat"))
print(main.get("act"))



