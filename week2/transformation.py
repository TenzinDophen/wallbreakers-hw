class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        setOfTransform = set() 
        for word in words:
            result = ""
            for char in word:
                num = ord(char) - ord("a")
                result += arr[num]
            setOfTransform.add(result)
            
        return len(setOfTransform)