def ln3(a,b,c):
     
     if a>b and a>c:
        l=a
     elif b>a and b>c:
        l=b
     else:
        l=c

     if a<b and a<c:
        s=a
     elif b<a and b<c:
        s=b
     else:
        s=c

     return l,s

d=float(input("enter 1st number:"))
e=float(input("enter 2nd number:"))
f=float(input("enter 3rd number:"))
l,s=ln3(d,e,f)
if l==s:
     print("all numbers are same")
else:
     print("largest number is:",l,"smallest number is:",s)
