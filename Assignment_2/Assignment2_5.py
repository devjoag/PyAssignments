def isPrime(no):
            retval=True
            for i in range(2,no):
                        if(no%i==0):
                            retval=False
                              
            return retval                  
                                    

def main():
            no=int(input("Enter Number: "))
            if(isPrime(no)):
                 print(" {} is Prime Number ".format(no))
            else:
                 print(" {} is Not Prime Number ".format(no))
            
                                    
if(__name__) == "__main__":
    main()