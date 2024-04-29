print("first line")
n=int(input())
l=[12,34,"hello",4]
print(l)
try:
    print(l[2])
    a=n/0
    print(k)
except ZeroDivisionError:
    print("exception occured due to divison of zero")
except Indexoutofbound:
    print("list index out of bound")
except NameError:
    print("name was not defined")
except:
    print("exception occured")   
else:
    print("no ecexption was raised")
finally:
   print ("final block")
print("executed smoothly")
