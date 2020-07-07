class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # needs a capacity, will determine the size of the array
        self.capacity = capacity # the numbers of buckets 
        # needs a storage to store each value
        self.storage = [None] * capacity
        # needs a size which will determine the number of the buckets that have been insert
        self.usage = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # turn the key in to a string and get its bytes
        str_key = str(key).encode()
        # start from an arbitrary large prime
        hash_value = 5381
        # loop over the str_key extracting the byte(b)
        for b in str_key:
            hash_value = ((hash_value <<5)+hash_value)+ b
            hash_value &= 0xffffffff # clamp to 32 bits
        return hash_value 


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # the hash_index creates our index value based to the key
        index = self.hash_index(key)
        # we create a new Linked List
        ht = HashTableEntry(key, value)
        # we are corresponding to the addressing node in our index
        node = self.storage[index]
        # if the node exists already,we check the next node.
        if node is not None:
            self.storage[index] = ht
            self.storage[index].next = node
        # Otherwise we need to put the thing here.
        else:
            self.storage[index] = ht


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        """
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None:
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return node
        """
        """
        # determine the index
        # iterate to the end of the list or find the key 
        # if the key is not found return None
        # otherwise remove the node from the list and return the value of the node
        index = self.hash_index(key)
        node = self.storage[index]
        prev = None
        while node is None and node.key !=key:
            prev = node
            node =node.next
        # either node is the node we looking for or none
        if node is None:
            # the key is not there
            return None
        else:
            # key is there
            self.size -=1
            total = node.value
            # delete it from the list
            if prev is None:
                node = None
            else:
                prev.next = prev.next .next
            return total
        """

        # Your code here
        # define index
        index = self.hash_index(key)
        # set the addressing node in our hash
        node = self.storage[index]
        # set prev to None
        prev = None
        # if the list is empty there is no item to iterate
        # and so we print the warning statement that list is empty
        if self.storage[index] is None:
            print("Warning list is empty")
            return
        else:
            if node.next is None:
                self.storage[index] = None
                self.usage -= 1
            else:
                while node.key != key:
                    prev = node
                    node = node.next
                prev.next = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None:
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return node
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
