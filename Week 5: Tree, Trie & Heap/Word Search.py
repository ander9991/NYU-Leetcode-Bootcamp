class TrieNode:
    def __init__(self, word = None):
        self.chars = {}
        self.word = word


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        cur = self.root
        self.m = len(board)
        self.n = len(board[0])

        for word in words:
            cur = self.root
            for char in word:
                if char not in cur.chars:
                    cur.chars[char] = TrieNode()
                cur = cur.chars[char]
            cur.word = word
        
        output = []
        def backtracking(i, j, parent):
            letter = board[i][j]
            cur = parent.chars[letter]
            if cur.word:
                output.append(cur.word)
                cur.word = None
            board[i][j] = '#'

            moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]
            for move in moves:
                sr = i + move[0]
                sc = j + move[1]
                if sr < 0 or sr >= self.m or sc < 0 or sc >= self.n:
                    continue
                if board[sr][sc] not in cur.chars:
                    continue
                backtracking(sr, sc, cur)
            board[i][j] = letter
            if not cur.chars:
                del parent.chars[letter]
        cur = self.root

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in cur.chars:
                    backtracking(i, j, cur)
        return output
