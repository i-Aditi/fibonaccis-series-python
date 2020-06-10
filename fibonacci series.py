def fib (n):
    n= int(input("enter the no. of terms you wish to see "))
    a=0
    b=1

    if n==1:
        print (a)

    else:
        print (a)
        print (b)

        for i in range (2,n):
            c = a+b
            a=b
            b=c
            print (c)


fib (3)
    
           


