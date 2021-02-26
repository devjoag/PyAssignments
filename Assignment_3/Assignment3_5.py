import isPrime as prime
def listprime(inlist):
    sum=0
    for i in range(len(inlist)):
      if(prime.checkPrime(inlist[i])):
        sum=sum+inlist[i]
    return sum        
    
def main():
    no=int(input("Please Enter Number of Elements :")) 
    inputList=list()
    for i in range (no):
        inno=int(input("Please Enter Number :"))
        inputList.append(inno)
    sum=listprime(inputList)
    print("Prime sum of  {} is {} ".format(inputList,sum))     
if(__name__) == "__main__":
    main()