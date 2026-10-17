x= int(input("Ënter your first number:"))
y= int(input("Ënter your second number:"))

all_x = id (x)
all_y = id (y)


print ("allocation of first number:", all_x)
print ("allocation of second number:", all_y)

hex_x =hex(x)
hex_y =hex(y)

print ("hex value of x:" , hex_x)
print ("hex value of y:" , hex_y)

print (x+y)
print (x*y)
if x>y :
    print (x-y)
    print (x//y)
if x<y :
    print(y-x)
    print(y//x)