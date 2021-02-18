"""
Write a program which display 5 times Marvellous on screen 
"""
def PrintMessage(number,message="Marvellous"):
       print((message+"\n")*number)      
def main():
    PrintMessage(5)
    PrintMessage(5,"Python")

if(__name__) == "__main__":
    main()
    