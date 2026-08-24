class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        q = deque()
        visit = set()
        wordList = set(wordList)

        def children(word):
            res = []
            for i in range(len(word)):
                # 26 characters 
                for j in range(26):
                    curr = word[:i] + chr(ord('a')+j) + word[i+1:]
                    if curr in wordList:
                        res.append(curr)
            return res

        q.append([beginWord,1])
        while q:
            word, turns = q.popleft()
            if word == endWord:
                return turns
            
            for child in children(word):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns+1])
        
        return 0


        