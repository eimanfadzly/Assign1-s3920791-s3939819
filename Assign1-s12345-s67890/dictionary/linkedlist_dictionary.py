from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        self.head = None


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word_frequency in words_frequencies:
            self.add_word_frequency(word_frequency)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        cur_node = self.head
        while cur_node:
            if cur_node.word_frequency.word == word:
                return cur_node.word_frequency.frequency
            cur_node = cur_node.next

        # Return 0 when word not found
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        new_node = ListNode(word_frequency)

        # When the linked list is empty
        if not self.head:
            self.head = new_node
            return True
        # Else
        else:
            cur_node = self.head
            while cur_node.next:
                # When word already exists, return False
                if cur_node.word_frequency.word == word_frequency.word:
                    return False
                cur_node = cur_node.next
            cur_node.next = new_node

        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # When the linked list is empty
        if not self.head:
            return False
        
        # When the head node hold the word to be deleted
        if self.head.word_frequency.word == word:
            self.head = self.head.next
            return True

        # Iterate through the linked list to find the node that holds the word to be deleted
        prev_node = self.head
        cur_node = self.head.next

        while cur_node:
            if cur_node.word_frequency.word == word:
                prev_node.next = cur_node.next
                return True
            prev_node = cur_node
            cur_node = cur_node.next

        # Return false when word not found
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # Initialize a list to contain the result
        results = []

        # Iterate through the linked list
        cur_node = self.head
        while cur_node:
            if cur_node.word_frequency.word.startswith(word):
                results.append(cur_node.word_frequency)
            cur_node = cur_node.next

        # Sort the results in decreasing order based on their frequency
        results.sort(key=lambda x: x.frequency, reverse=True)

        return results[:3]



