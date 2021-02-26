import functools as f
def main():
    n=int(input("Please Enter how many numbers"))
    mynum=list()
    for i in range(n):
            n1=int(input("Please Enter number "))  
            mynum.append(n1)
    filteredList=list(filter(lambda n:(n>=70 and n<=90),mynum))
    mapList=list(map(lambda n:n*10,filteredList))
    reduceop=f.reduce(lambda n1,n2:n1*n2,mapList)        
    print("Filter Output is  {} is ".format(filteredList))
    print("Map Output is  {} is ".format(mapList))
    print("Final Output is  {} is ".format(reduceop))    
if(__name__) == "__main__":
    main()
    