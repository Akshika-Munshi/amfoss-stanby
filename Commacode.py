fruits=[]
def Takelist():
    a=str(input("Enter element value "))
    fruits.append(a)
N=int(input("Enter list length "))
for i in range (0,N):
    Takelist()
#print(fruits)

for i in range(0,(N-1)):
    print(str(fruits[i])+",",end=" ")
print("and "+ str(fruits[-1]))