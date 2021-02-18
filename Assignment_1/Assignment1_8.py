"""
Write a program which accept number from user and print that number of “*” on screen. 
"""
def PrintMessage(number,message="*"):
       print((message)*number)      
def main():
    no=int(input("Please Enter Number :"))
    PrintMessage(no,"*")

if(__name__) == "__main__":
    main()
    