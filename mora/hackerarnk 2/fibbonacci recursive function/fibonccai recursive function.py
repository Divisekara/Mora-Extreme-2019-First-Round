global L
L=[]

def fibo(n):  
   if n <= 1:
      #L.append(n)
      return n
   else:
      #L.append(fibo(n-1))
      #L.append(fibo(n-2))
      return(fibo(n-1) + fibo(n-2))

#output the nth term of the fibonaci sequence.

   
print fibo(20)
M = sorted(list(set(L)))
print M

    
    
        
