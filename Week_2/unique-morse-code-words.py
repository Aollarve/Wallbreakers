class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = {}
        for word in words:
            morse_word = ""
            for letter in word:
                 morse_word = morse_word + morse_code[ord(letter)-97]
            if morse_word not in d:
                d[morse_word] = 1
        return len(d.keys())