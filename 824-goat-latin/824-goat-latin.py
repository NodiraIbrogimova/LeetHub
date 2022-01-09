class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        '''
        1. Check for vowel or consonant
            if vowel: add 'senma' to the end of that word
            else: add word[0] + ma to the end of the word
        2. at each step count the number of 'a's. Add count times a at the end of each word
        '''
        sentence = sentence.split(" ")
        vowels = ('a', 'e', 'i', 'o', 'u')
        count = 1
        for i in range(len(sentence)):
            first_char= sentence[i][0].lower()
            suffix = ''
            if first_char not in vowels:
                suffix = sentence[i][0]
                sentence[i] = '' + sentence[i][1:]
            suffix += ('ma' + count*'a')
            sentence[i] += suffix
            count += 1
        return " ".join(sentence)
        
        