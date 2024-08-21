#determine a vowel

def vowel(character):
    vow=['a','e','i','o','u']
    if character in vow:
        print("the character is a vowel")
    else:
        print("the character is a consonant")

a=input("enter a character from a-z: ")
vowel(a)