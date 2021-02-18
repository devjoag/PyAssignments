"""
Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false. 
"""
def CheckDivision(no,by=5):
        result=False
        if(no%by==0):
                      result=True
        return result
def main():
    no=int(input("Please Enter Number :"))
    isDivisible=CheckDivision(no)
    if(isDivisible):
         print("{} is Divisible by {}".format(no,5))
    else:
       print("{} is not Divisible by {}".format(no,5))

if(__name__) == "__main__":
    main()
    