t1=(4,3,2,2,-1,18)
t2=(2,4,8,8,3,2,9)
print("The first list is: ",t1)
print("The first second is: ",t2)
newt1=[]
newt2=[]


def tup1(t1):
    s=0
    while s<7:
        q=s*2
        newt1.append(q)
        s+=1
tup1(t1)
print("The new first list is: ",newt1)


def tup2(t2):
    e=0
    while e<8:
        w=e*2
        newt2.append(w)
        e+=1

tup2(t2) 
print("The new second list is: ",newt2)












