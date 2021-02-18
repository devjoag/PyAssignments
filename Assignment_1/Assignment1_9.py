"""
Write a program which display first 10 even numbers on screen.  
"""
def PrintEven(number):
    evenNo=list()
    for i in range(1,number*2+1):
                   if(i%2 == 0):
                               evenNo.append(i)
    print(evenNo)                 
       
def main():
    PrintEven(10)

if(__name__) == "__main__":
    main()
    