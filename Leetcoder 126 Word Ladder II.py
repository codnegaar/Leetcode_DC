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


class Solution:
  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordSet = set(wordList)
    if endWord not in wordList:
      return []

    # {"hit": ["hot"], "hot": ["dot", "lot"], ...}
    graph: Dict[str, List[str]] = collections.defaultdict(list)

    # Build graph from beginWord -> endWord
    if not self._bfs(beginWord, endWord, wordSet, graph):
      return []

    ans = []

    self._dfs(graph, beginWord, endWord, [beginWord], ans)
    return ans

  def _bfs(self, beginWord: str, endWord: str, wordSet: Set[str], graph: Dict[str, List[str]]) -> bool:
    currentLevelWords = {beginWord}

    while currentLevelWords:
      for word in currentLevelWords:
        wordSet.discard(word)
      nextLevelWords = set()
      reachEndWord = False
      for parent in currentLevelWords:
        for child in self._getChildren(parent, wordSet):
          if child in wordSet:
            nextLevelWords.add(child)
            graph[parent].append(child)
          if child == endWord:
            reachEndWord = True
      if reachEndWord:
        return True
      currentLevelWords = nextLevelWords

    return False

  def _getChildren(self, parent: str, wordSet: Set[str]) -> List[str]:
    children = []
    s = list(parent)

    for i, cache in enumerate(s):
      for c in string.ascii_lowercase:
        if c == cache:
          continue
        s[i] = c
        child = ''.join(s)
        if child in wordSet:
          children.append(child)
      s[i] = cache

    return children

  def _dfs(self, graph: Dict[str, List[str]], word: str, endWord: str, path: List[str], ans: List[List[str]]) -> None:
    if word == endWord:
      ans.append(path.copy())
      return

    for child in graph.get(word, []):
      path.append(child)
      self._dfs(graph, child, endWord, path, ans)
      path.pop()
