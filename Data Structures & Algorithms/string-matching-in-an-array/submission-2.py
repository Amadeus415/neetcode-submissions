class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        output = set()
        
        for word in words:
            other_words = []
            #array without current word
            other_words = [w for w in words if w != word]

            #loop through other words
            for w in other_words:
                if word in w:
                    output.add(word)

                

        return list(output)

            