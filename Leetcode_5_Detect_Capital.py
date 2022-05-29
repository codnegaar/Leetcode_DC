class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.isupper()==True:    # if all is caps
            return True
        elif word.islower()==True:  # all lower case
            return True
        elif word[0].isupper() and word[1:].islower() ==True:  # if first char is caps
            return True
        else:                       # other location has caps char
            return False
 
        
