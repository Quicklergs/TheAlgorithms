"""
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words. A basic Trie however has O(n^2) space complexity
making it impractical in practice. It however provides O(max(search_string, length of longest word)) 
lookup time making it an optimal approach when space is not an issue.
"""


class TrieNode:
    def __init__(self):
        self.nodes = dict()  # Mapping from char to TrieNode
        self.is_leaf = False

    def insert_many(self, words: [str]):
        """
        Inserts a list of words into the Trie
        :param words: list of string words
        :return: None
        """
        for word in words:
            self.insert(word)

    def insert(self, word: str):
        """
        Inserts a word into the Trie
        :param word: word to be inserted
        :return: None
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def find(self, word: str) -> bool:
        """
        Tries to find word in a Trie
        :param word: word to look for
        :return: Returns True if word is found, False otherwise
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def get_words_starting_with(self, prefix: str) -> [str]:
        """
        return a list of all words that start with the given prefix.
        are followed by a certain prefix.
    
        long-url: https://www.geeksforgeeks.org/prefix-matching-python-using-pytrie-module/
        :param prefix: the prefix to be matched
        :return: List of prefix-matched words.
        
        >>> get_words_starting_with("a")
        apple all

        """


        def get_trie_for_prefix(t: TrieNode, prefix: str):

            '''
            Different search function that returns the sub trie
            instead of True or False
            :param t: self
            :param prefix: prefix to be searched
            :return: a new sub-trie
            
            '''
            curr = t
            for char in prefix:
                if char not in curr.nodes:
                    return False
                    
                curr = curr.nodes[char]
            return curr

        def depth_first_search(root: TrieNode, s: str, prefix: str, lst):
            """Returns a list with prefixes and their TrieNode"""
            for i in root.nodes:
                if root.is_leaf:
                    lst.append((prefix + s, root.nodes[i]))
                else:
                    dfs(root.nodes[i], s + i, prefix, lst)
            return lst

        sub_trie= get_trie_for_prefix(self, prefix)
        if sub_trie==False:
            return False
        else:
            print_words(sub_trie, prefix)




    def delete(self, word: str):
        """
        Deletes a word in a Trie
        :param word: word to delete
        :return: None
        """

        def _delete(curr: TrieNode, word: str, index: int):
            if index == len(word):
                # If word does not exist
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0
            char = word[index]
            char_node = curr.nodes.get(char)
            # If char not in current trie node
            if not char_node:
                return False
            # Flag to check if node can be deleted
            delete_curr = _delete(char_node, word, index + 1)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            return delete_curr

        _delete(self, word, 0)


def print_words(node: TrieNode, word: str):
    """
    Prints all the words in a Trie
    :param node: root node of Trie
    :param word: Word variable should be empty at start
    :return: None
    """
    if node.is_leaf:
        print(word, end=" ")

    for key, value in node.nodes.items():
        print_words(value, word + key)


def test_trie():
    words = "banana bananas bandana band apple all beast".split()
    root = TrieNode()
    root.insert_many(words)
    
    # print_words(root, "")
    assert all(root.find(word) for word in words)
    assert root.find("banana")
    assert not root.find("bandanas")
    assert not root.find("apps")
    assert root.find("apple")
    assert root.find("all")
    root.delete("all")
    assert not root.find("all")
    root.delete("banana")
    assert not root.find("banana")
    assert root.find("bananas")
    root.get_words_starting_with("ban")
    return True


def print_results(msg: str, passes: bool) -> None:
    print(str(msg), "works!" if passes else "doesn't work :(")


def pytests():
    assert test_trie()
    import doctest
    doctest.testmod()


def main():
    """
    >>> pytests()
    """
    print_results("Testing trie functionality", test_trie())


if __name__ == "__main__":
    main()
