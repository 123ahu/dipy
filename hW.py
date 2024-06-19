# Program used to check for consonants and vowels
word_letter = input("Enter word/letter:")
vowels = "aeiouAEIOU"
for char in word_letter:
    if char in vowels:
        print(char, "is a vowel")
    else:
        print(char, "is not a vowel")
