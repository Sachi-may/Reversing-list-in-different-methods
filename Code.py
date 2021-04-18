class sachi:
    def __init__(self,list):
        self.list=list

    def method1(self):
        c0=self.list[:]
        print(c0)
        c0.reverse()
        print(c0)
        print('Method 1')
    def method2(self):
        c1=self.list[:]
        print(c1)
        print(c1[::-1])

        print('Method 2')
    def method3(self):
        c2=self.list[:]
        print(c2)
        i=0
        j=len(c2)-1
        for i in range(len(c2)//2):
            temp = c2[i]
            c2[i] = c2[j]
            c2[j] = temp
            j-=1
        print(c2)
        print('Method 3')
print("Enter the numbers of list")
size=int(input("Ente the size of list"))
list=[]
for i in range(size):
    list.append(int(input("Enter the elements")))
obj1=sachi(list)
obj1.method1()
obj1.method2()
obj1.method3()
