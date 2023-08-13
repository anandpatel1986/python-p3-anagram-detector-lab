class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, list_anagram):
        sorted_word = sorted([ letters for letters in self.word])
        matched_anagrams = []
        for anagram in list_anagram:
            sorted_anagram = sorted([letters for letters in anagram])
            if sorted_anagram == sorted_word:
                matched_anagrams.append(anagram)
        return matched_anagrams
    
