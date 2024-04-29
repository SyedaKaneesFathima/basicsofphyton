#upper case &lowercase:-
word=input()
print(word)
upr, lwr,spl = 0, 0, 0
for i in range(len(word)):
	if word[i] >= 'A' and word[i] <= 'Z':
		upr += 1
	elif word[i] >= 'a' and word[i] <= 'z':
		lwr += 1
	else:
		spl += 1
 
print("UpperCase : ",upr)
print("LowerCase : ",lwr)
print("SpecialCase : ",spl)
