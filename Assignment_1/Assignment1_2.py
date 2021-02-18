"""
Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console. 
"""
def ChkNum(no):
       return no&1       
def main():
      no=int(input("Please Enter Number :"))
      ret=ChkNum(no)
      if(ret==0):
              print("{} is Even Number".format(no))
      else :
            print("{} is Odd Number".format(no))
if(__name__) == "__main__":
    main()