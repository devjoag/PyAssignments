import functools as f
def main():
    no=int(input("Please Enter Number of Elements :")) 
    inputList=list()
    for i in range (no):
        inno=int(input("Please Enter Number :"))
        inputList.append(inno)
    print("Sum of {} is {} ".format(inputList,f.reduce(lambda no1,no2:no1+no2,inputList)))        
if(__name__) == "__main__":
    main()