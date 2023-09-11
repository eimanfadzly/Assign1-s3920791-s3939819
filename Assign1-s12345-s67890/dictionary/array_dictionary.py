import bisect

from .base_dictionary import BaseDictionary
from .word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        self.word_frequencies = [] # Initialize an empty list to store word frequencies


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        Build the Array-based dictionary from a list of WordFrequency objects.

        Args:
            words_frequencies (list of WordFrequency): List of WordFrequency objects containing words and their frequencies.
        """
        for word_frequency in words_frequencies:
            # Append each word_frequency to the data structure
            self.word_frequencies.append(word_frequency)

    def search(self, word: str) -> int:
        """
        Search for a word in the Array-based dictionary and return its frequency if found.

        Args:
            word (str): The word to search for.

        Returns:
            int: The frequency of the word if found, 0 otherwise.
        """
        for word_frequency in self.word_frequencies:
            if word_frequency.word == word:
                return word_frequency.frequency
        return 0
        
    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        Add a word with its frequency to the Array-based dictionary.

        Args:
            word_frequency (WordFrequency): WordFrequency object containing the word and its frequency.

        Returns:
            bool: True if the word was successfully added, False if it already exists in the dictionary.
        """
        for wf in self.word_frequencies:
            if wf.word == word_frequency.word:
                return False  # Word already exists
        self.word_frequencies.append(word_frequency)
        return True

    def delete_word(self, word: str) -> bool:
        """
        Delete a word from the Array-based dictionary.

        Args:
            word (str): The word to be deleted.

        Returns:
            bool: True if the word was successfully deleted, False if it doesn't exist in the dictionary.
        """
        for wf in self.word_frequencies:
            if wf.word == word:
                self.word_frequencies.remove(wf)
                return True
        return False  # Word not found


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        Get a list of WordFrequency objects that are autocompletions of the given prefix.

        Args:
            prefix_word (str): The prefix for which to find autocompletions.

        Returns:
            list of WordFrequency: List of WordFrequency objects representing autocompletions, sorted by frequency.
        """
        matching_words = [wf for wf in self.word_frequencies if wf.word.startswith(prefix_word)]
        sorted_words = sorted(matching_words, key=lambda wf: wf.frequency, reverse=True)
        return sorted_words[:3]  # Return the top 3