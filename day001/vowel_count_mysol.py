def getCount(inputStr):
    num_vowels = 0
    # your code here
    
    #put vowels into an array
    vowels = ('a','e','i','o','u')
    
    #loop through the characters in input string
    for ch in inputStr:
    
        #if character in vowels, increment counter
        if ch in vowels:
            num_vowels += 1 
    
    return num_vowels


res = getCount('abedu')
print(res)