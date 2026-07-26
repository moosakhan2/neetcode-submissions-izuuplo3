class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.endofWord = True
                

    def search(self, word: str) -> bool:
        def DFS(curr, i):
            
            if i == len(word):
                return curr.endofWord
            
            for char in curr.children:
                if word[i] == '.':
                    for newChar in curr.children:
                        if(DFS(curr.children[newChar],i+1)):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    return(DFS(curr.children[word[i]], i+1))

            
            return False
        
        return(DFS(self.root, 0))
            

            

            







        
