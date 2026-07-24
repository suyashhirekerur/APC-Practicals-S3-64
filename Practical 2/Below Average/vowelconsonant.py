# Write a PYTHON program to check entered character is vowel or consonant.

ch = input("Enter a character: ")
vowels = "aeiouAEIOU"

for i in vowels:
    if ch == i:
        print(ch, "is a vowel")
        break
else:
    print(ch, "is a consonant")