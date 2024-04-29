#To check palindrome:-
def palindromestring(word):
    if word == word[::-1]:
        print("palindrome")
    else:
        print("not palimdrome")

word=input()
print(word)
print(palindromestring(word))
