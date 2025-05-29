class Trie(object):

    def __init__(self):
        self.Trie = []

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.Trie.append(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return True if word in self.Trie else False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        for x in self.Trie:
            if x[:len(prefix)]==prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)