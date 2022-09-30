from collections import defaultdict
import sys

input = sys.stdin.readline
class TrieNode:
    def __init__(self):
        self.word= False
        self.children=defaultdict(TrieNode)

    def __str__(self):
        return "word= {} children={}".format(self.word ,self.children)

class Trie:
    def __init__(self):
        self.root=TrieNode()
        self.available=True

    def insert(self,word):
        node=self.root
        for char in word:
            node =node.children[char]
            # if node.word==True:
            #     self.available=False
                # print("여기",char,word,node,node.children)
        node.word=True
    def dfs(self,now):
        # print(now)
        if now.word==True and len(now.children)>=1:
            # print("여기",self.available)
            self.available=False
            # print("여기",self.available)
            return
        for i in now.children:
            self.dfs(now.children[i])

    def search(self):
        node=self.root
        if node.word==True and len(node.children)>=1:
            self.avaliable=False
            return
        for i in node.children:
            self.dfs(node.children[i])
    def __str__(self):
        return "{} ".format(self.root)

for _ in range(int(input())):
    n= int(input())
    trie= Trie()
    for i in range(n):
        tmp=input().rstrip()
        trie.insert(tmp)
    trie.search()
    # print()
    # print(trie)
    if trie.available:
        print("YES")
    else:
        print("NO")