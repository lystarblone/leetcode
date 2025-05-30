from random import choice 
class RandomizedSet(object):

    def __init__(self):
        self.data = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            self.data.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            self.data.pop(self.data.index(val))
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()