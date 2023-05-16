''' 1. COUNTING VOWELS '''

def countVowels(s):
    vowels = 0
    for i in s:
        if i in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            vowels = vowels + 1
    return vowels

print(countVowels("Walking"))

''' 2. STRING STABILITY '''

def isStable(s):
    half1count = 0
    half2count = 0
    vowelsList = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    half1 = s[:len(s) // 2]
    half2 = s[len(s) - len(s) // 2:]
    for i in half1:
        if i in vowelsList:
            half1count = half1count + 1
    for i in half2:
        if i in vowelsList:
            half2count = half2count + 1
    if half1count == half2count:
        return True
    else: 
        return False

print(isStable("ababa"))

# Make vowel list
# half1 is the first half of the word
# half2 is the second half of the word
# If a vowel is present in half1, add one to the vowel count of the first half
# If a vowel is present in half2, add one to the vowel count of the second half
# Compare both hal1 and half2

''' 3. DETECTING DOUBLE LETTERS IN WORDS '''

def hasDoubleLetters(s):
    for i in range(len(s)-1):
        s = s.lower()
        letter1 = s[i]
        letter2 = s[i+1]
        if letter1 == letter2:
            return True
    return False

print(hasDoubleLetters("Miss"))

''' 4. INTERLEAVING WORDS '''

def interleave(word1, word2):
    new_word = ''                                                   # variable is a string
    shortest_word_length = min(len(word1), len(word2))              # gets the minimum of the words' length
    for i in range(shortest_word_length):
        new_word = new_word + word1[i]
        new_word = new_word + word2[i]
    if shortest_word_length < len(word1):
        new_word = new_word + word1[shortest_word_length:]
    else: 
        new_word = new_word + word2[shortest_word_length:]
    return new_word
    
print(interleave("yab", "aaaaaaa"))

# def interleave(word1, word2):                                                 
#    shortest_word_length = min(len(word1), len(word2))
#    return shortest_word_length
# print(interleave("abcdefg", "abc"))

# Start with word1 and print the first letter of  word1 [position 0]
# Print the first letter of word2 next to the first letter of word1
# Get the next letter of word1 [position 1] and add that to the total new word


''' 5. LONGEST COMMON PREFIX '''

def lcp(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    output = ""
    a = 0
    b = 0
    while(a <= n1 - 1 and b <= n2 - 1):
        if (s1[a] != s2[b]):
            break
        output = output + (s1[a])

        a = a + 1
        b = b + 1
    return (output)
 
print(lcp("hello", "help"))

''' 6. CATCOURSES SPREADSHEETS '''
def find(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i 
    return -1

def extractLastName(full_name, email):
    last_name = " "
    check1 = find(email, "@")
    check2 = email[1:check1]
    length = len(check2) + 1
    count = 0
    for i in range(len(full_name)):
        if full_name[i] == " ":
            check3 = full_name[i+1:len(full_name)]
            if length == len(check3):
                return(full_name[i+1:len(full_name)])
    for i in range(len(full_name)):
        if full_name[i] == " ":
            last_space = i 
    last_name = full_name[last_space + 1:]
    return last_name
    
print(extractLastName("Steve Jobs", "@sjobsucmerced.edu"))









