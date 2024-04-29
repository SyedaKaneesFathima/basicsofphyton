print("firts line")
list=[12,34,"hello",4]
print(list)

try:
    a=20/0

except:
    print("exception occured")
try:
    print(list[2])
except:
    print("list index out of bound")
else:
    print("no ecexption was raised")
finally:
   print ("final block")
print("executed smoothly")

