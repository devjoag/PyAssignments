def Fact(no):
             fact=0
             for i in range(1,no) :
                              if(no%i==0):
                                      fact=fact+i
                              
             return fact                  
                                    

def main():
            no=int(input("Enter Number: "))
            print("Factor Addition of {} is {}".format(no,Fact(no)))
            
                                    
if(__name__) == "__main__":
    main()