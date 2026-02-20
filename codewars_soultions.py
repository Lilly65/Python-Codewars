#Solution: Even or Odd
def even_or_odd(number):
    return "Odd" if number % 2 else "Even"

#Solution: Convert a Number to a String
def number_to_string(num):
    return str(num)

# Solution: Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# Solution: Vowel Count
# This solution is actually slower because of the time it takes to 
# set up the hashtable and the length of the vowel string being so short.
# It is, however, how I solved the problem.
def get_count(sentence):
    vowels = {"a":1,"e":2,"i":3,"o":4,"u":5,"A":1,"E":2,"I":3,"O":4,"U":5}
    vowelcount = 0
    
    for ch in sentence:
        if ch in vowels:
            vowelcount += 1
            
    return vowelcount