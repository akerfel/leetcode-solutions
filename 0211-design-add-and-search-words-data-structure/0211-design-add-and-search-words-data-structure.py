class Node:
    def __init__(self):
        self.children = {} # {character, node}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word) -> bool:
        return self.searchHelper(word, self.root)
        
    def searchHelper(self, word: str, cur) -> bool:
        for i, c in enumerate(word):
            if c == '.':
                for childNode in cur.children.values():
                    if self.searchHelper(word[i+1:], childNode):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
            cur = cur.children[c]
        return cur.isWord
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)