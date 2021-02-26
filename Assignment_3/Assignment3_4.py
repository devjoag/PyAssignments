def main():
    no=int(input("Please Enter Number of Elements :")) 
    inputDict=dict()
    for i in range (no):
        inno=int(input("Please Enter Number :"))
        if inno in inputDict.keys():
                count=inputDict[inno]
                count=count+1
                inputDict[inno]=count
        else:
            inputDict[inno]=1        
    nsearch=int(input("Enter Number to search :"))
    print("Occ of {} is {} times ".format(nsearch,inputDict[nsearch]))        
if(__name__) == "__main__":
    main()