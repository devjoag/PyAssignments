
def Fact(no):
             fact=1
             for i in range(1,no+1) :
                              fact=fact*i
                              
             return fact                  
                                    

def main():
            no=int(input("Enter Number: "))
            print("Factorial of {} is {}".format(no,Fact(no)))
            
                                    
if(__name__) == "__main__":
    main()