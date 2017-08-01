#Implement a function which does run-length encoding. This means that, given a string, it replaces
#repeated characters with the number of times they are repeated and the character.

#For example: runlength_encode("aabbbcaa") should return "2a3b1c2a".

def runlength_encode(text):

final_char = ""
count_char = 1

    for index, char in enumerate(text):
        
        if index == 0:
            pass
        elif char == text[index-1]:
           count_char += 1
        elif index == len(text)-1:
            final_char += str(count_char) + text[index-1]
        else: 
          final_char += str(count_char) + text[index-1]
          count_char = 1
     
    return final_char
 
runlength_encode("aabbbcaa")

O(n * ?)

# TOTAL TECHNOLOGY FAILURE V_V