"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    
    """to find a word from the words.txt text file.
    >>> wf = WordFinder('words.txt')
    3 words read

    >>> wf.random() in ('cat','dog')
    >>> wf.random() in ('porcupine')
    >>> wf.random() -> dog
    True
    """
    def __init__(self, path):
            #one word per line
            #read the dictionary, references from
            #https://python.org
        dict_file = open(path)

        self.words =  self.parse(dict_file)
        print(f'{len(self.words)} words read')
    
    #bonus with __repr__
    def __repr__(self):
        """show representation"""
        return f'WordFinder path = {self.path}'

    def parse(self, dict_file):
        """to parse the dictionary onto the word list"""
        #to write the file
        return[w.strip() for w in dict_file]
    #define a random function    
    def random(self):
        """return random word."""
        return random.choice(self.words)
    
class SpecialWordFinder:
    """subclass that uses wordFinder but change needed parts
    so it can work. Try to do this so as little code as needed
    is duplicated"""

    def parse(self, dict_file):
        """parse dictionary onto the list of words without
        special characters like blanks"""

        return[w.strip() for w in dict_file
            if w.strip() and not w.startswith("#")]