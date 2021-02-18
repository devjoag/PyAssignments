"""
Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.  
"""
def Add(no1,no2):
       return no1+no2      
def main():
      no1=int(input("Please Enter First Number :"))
      no2=int(input("Please Enter Second Number :"))
      ret=Add(no1,no2)
      print("Addition of {} and {} is {}".format(no1,no2,ret))

if(__name__) == "__main__":
    main()