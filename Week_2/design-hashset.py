class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list_of_values = []

    def add(self, key: int) -> None:
        if key <= len(self.list_of_values)-1:
            self.list_of_values[key] = True
        else:
            while(len(self.list_of_values)-1 != key):
                self.list_of_values.append(False)
            self.list_of_values[key] = True
                
    def remove(self, key: int) -> None:
        if key <= len(self.list_of_values)-1:
            self.list_of_values[key] = False    

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key > len(self.list_of_values)-1:
            return False
        else:
            return self.list_of_values[key]
        