#To find max and min :-
word = input()
l = list(word)
l = list(map(int, l))
print("max_digit", max(l))
print("min_digit", min(l))

#divisble by 5:-
def Totalnumbersdivisbleby(li):
    n=len(li)
    result=0
    for i in range(n):
        if li[i]%5==0:
             result=result+1
    return result     
li=list(map(int,input().split()))
result=Totalnumbersdivisbleby(li)
print("Total numbers divisble by 5 are:",result)
