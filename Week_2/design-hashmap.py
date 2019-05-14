class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list_keys = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key <= len(self.list_keys)-1:
            self.list_keys[key] = value
        else:
            while(len(self.list_keys)-1 != key):
                self.list_keys.append("")
            self.list_keys[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key > len(self.list_keys)-1:
            return -1
        elif self.list_keys[key] == "":
            return -1
        else:
            return self.list_keys[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key <= len(self.list_keys)-1:
            self.list_keys[key] = ""
        