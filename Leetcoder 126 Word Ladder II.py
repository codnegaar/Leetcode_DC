'''
126. Word Ladder II
 
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord,
or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
        Explanation: There are 2 shortest transformation sequences:
        "hit" -> "hot" -> "dot" -> "dog" -> "cog"
        "hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
        Output: []
        Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:
        1 <= beginWord.length <= 5
        endWord.length == beginWord.length
        1 <= wordList.length <= 500
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique.
        The sum of all shortest transformation sequences does not exceed 105.


'''
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        def createAdjacencyList(wordList):
            adj = defaultdict(set)
            d = defaultdict(set)
            for word in wordList:
                for i in range(len(word)):
                    derived = word[:i] + "*" + word[i+1:]
                    for neighbor in d[derived]:
                        adj[word].add(neighbor)
                        adj[neighbor].add(word)
                    d[derived].add(word)
            return adj
        
        def edgesOnShortestPaths(adj, beginWord, endWord):
            frontier = [beginWord]
            edges = defaultdict(list)
            edges[beginWord] = []
            while endWord not in frontier:
                nextfrontier = set(neighbor
                    for word in frontier
                    for neighbor in adj[word]
                    if neighbor not in edges
                )
                if not nextfrontier:  # endNode is not reachable
                    return
                for word in frontier:
                    for neighbor in adj[word]:
                        if neighbor in nextfrontier:
                            edges[neighbor].append(word)
                frontier = nextfrontier
            return edges
        
        def generatePaths(edges, word):
            if not edges[word]:
                yield [word]
            else:
                for neighbor in edges[word]:
                    for path in generatePaths(edges, neighbor):
                        yield path + [word]
            

        if endWord not in wordList:  # shortcut exit
            return []
        adj = createAdjacencyList([beginWord] + wordList)
        edges = edgesOnShortestPaths(adj, beginWord, endWord)
        if not edges:  # endNode is not reachable
            return []
        return list(generatePaths(edges, endWord))
