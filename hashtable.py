class HashTable:
    '''
        https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
    '''
    
    ## number of elements that have been inserted
    self.size = 0
    ## side of the internal array
    self.capacity = INITIAL_CAPACITY
    # the internal array used to store the inserted values based on the provided key
    self.bucket = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        # for each character in the key
        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)

            hashsum += (idx + len(key)) ** ord(c)
            # perform modulus to keep  hashsum in range [0, self.capacity - 1]

            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        # 1. Increment size
        self.size += 1
        # 2. Compute index of key
        index = self.hash(key)
        # 3. Go to the node corresponding to the hash
        node = self.bucket[index]

        if node is None:
            # Create node, add it, return
            self.bucket[index] = node
            return
        # 4. Collision ! Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next
        
        # Add a new node at the end of the list with provided key/value

        prev.next = Node(key, value)

    def find(self, key):
        # 1. Compute index for the provided key using hash function
        index = self.hash(key)
        # 2. Go to the bucket for that index
        node = self.bucket[index]
        # 3. Traverse the linked list at this node
        while node is not None and key != node.key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None

        if node is None:
            # Not found !
            return None
        else:
            # Found - return the data value
            return node.value

    def remove(self, key):
        # 1. Compute hash for the key to determine index.
        index = self.hash(key)
        # 2. Iterate linked list of nodes. Continue until end of list or until key is found.
        node = self.bucket[index]
        while node is not None and key != node.key:
            node = node.next
        # 3. If the key is not found, return None

        if node is None:
            # Not Found
            return None
        else:
            # 4. Otherwise, remove the node from the linked list and return the node value.
            self.size -= 1
            result = node.value
            # Delete this element from the linked list

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            
            return result

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None