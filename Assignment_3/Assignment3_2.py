import functools as f
def main():
    no=int(input("Please Enter Number of Elements :")) 
    inputList=list()
    for i in range (no):
        inno=int(input("Please Enter Number :"))
        inputList.append(inno)
    maxList=sorted(inputList, reverse=True)  
    print("Max of {} is {} ".format(inputList,maxList[0]))        
if(__name__) == "__main__":
    main()