# CS 303E Quiz 5C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Entrance Roads
def entranceRoads(roads, cities):
    result = {}
    for i in roads:
        c = list(i)
        if c[0] not in cities and c[1] in cities:
            result[i] = True
        else:
            result[i] = False
    return result


# Problem 2: Recursive Duplicate Before Vowels ​
def dupeBeforeVowels(s):
    # MAKE SURE YOUR SOLUTION IS RECURSIVE AND DOES NOT CREATE A HELPER FUNCTION]
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    if len(s) == 0:
        return ""
    else:
        i = len(s)-1
        if s[i] in vowels:
            vowel = s[i]
            prev = s[i-1]
            s = s[0:(i)]
            return dupeBeforeVowels(s) + prev + vowel
        else: 
            current = s[i]
            s = s[0:i]
            return dupeBeforeVowels(s) + current
        


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    #print(entranceRoads({('Austin', 'Houston'), ('Houston', 'Austin'), ('Dallas', 'Austin'), ('San Antonio', 'El Paso'), ('Dallas', 'Houston'), ('Galveston', 'Houston')}, {'Houston', 'Austin'}))
    #print(entranceRoads({('Austin', 'Houston'), ('Houston', 'Austin'), ('Dallas', 'Austin')}, set()))
    #print(entranceRoads({('swamp', 'jungle'), ('desert', 'tundra'), ('coast', 'plains')}, {'jungle', 'plains', 'sea', 'tundra'}))


    # print(dupeBeforeVowels('CS303E is really fun!'))
    # print(dupeBeforeVowels('Hello World!'))
    #print(dupeBeforeVowels('feeling tired'))



    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT