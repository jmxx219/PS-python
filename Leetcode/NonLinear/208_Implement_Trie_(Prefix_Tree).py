import collections


# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


class Trie2:

    def __init__(self):
        self.trie = {}
    def insert(self, word: str) -> None:
        currTrie = self.trie
        for char in word:
            if char not in currTrie:
                currTrie[char] = {}
            currTrie = currTrie[char]
            print(self.trie)
        currTrie["done"] = True
        print(self.trie)


    def search(self, word: str) -> bool:
        currTrie = self.trie

        for char in word:
            if char in currTrie:
                currTrie = currTrie[char]
            else:
                return False
        return "done" in currTrie

    def startsWith(self, prefix: str) -> bool:
        currTrie = self.trie

        for char in prefix:
            if char in currTrie:
                currTrie = currTrie[char]
            else:
                return False
        return True


if __name__ == "__main__":
    trie = Trie2()
    trie.insert("apple")
