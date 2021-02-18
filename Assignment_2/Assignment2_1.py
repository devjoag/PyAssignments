"""Write a program which contains one function named as Fun(). That function should display
“Hello from Fun” on console. """
import Arithmetic as a

                             
def main():
           no1=int(input("Enter First Number :"))
           no2=int(input("Enter Second Number :"))
           print("Calling Addition")
           print("Addition of {} and {} is {}".format(no1,no2,a.Add(no1,no2))) 
           print("Calling Sub")
           print("Sub of {} and {} is {}".format(no1,no2,a.Sub(no1,no2)))  
           print("Calling Div")
           print("Division of {} and {} is {}".format(no1,no2,a.Div(no1,no2)))
           print("Calling Mult")
           print("Mult of {} and {} is {}".format(no1,no2,a.Mult(no1,no2)))             
            
if(__name__) == "__main__":
    main()