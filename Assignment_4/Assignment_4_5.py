import functools as f
import isPrime as p
def main():
    n=int(input("Please Enter how many numbers"))
    mynum=list()
    for i in range(n):
            n1=int(input("Please Enter number "))  
            mynum.append(n1)
    filteredList=list(filter(lambda n:(p.checkPrime(n)),mynum))
    mapList=list(map(lambda n:n*2,filteredList))
    reduceop=f.reduce(lambda x, y: x if x > y else y,mapList)        
    print("Filter Output is  {} is ".format(filteredList))
    print("Map Output is  {} is ".format(mapList))
    print("Final Output is  {} is ".format(reduceop))    
if(__name__) == "__main__":
    main()
    