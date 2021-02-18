"""
Write a program which accept number from user and check whether that number is positive or
negative or zero. 
"""
def isPositiveNegative(no):
            if(no==0):
                      print("Number is Zero")
            elif(no>0):
                       print("{} is Positive".format(no))
            else :
                    print("{} is Negative".format(no))           
def main():
      no=int(input("Please Enter Number :"))
      isPositiveNegative(no)

if(__name__) == "__main__":
    main()