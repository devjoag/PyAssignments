def checkPrime(no):
    isPrime=True
    for i in range(2,no):
     if(no%i==0):
            return False
      
    return isPrime        
    