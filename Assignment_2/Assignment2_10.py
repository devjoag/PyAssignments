def main():
    no=int(input("Enter Number: ")) 
    st=list(str(no))
    sum=0
    for i in range (0,len(st)):
        sum=sum+int(st[i])
    print("Sum of Digits in {} are {}".format(no,sum))    
if(__name__) == "__main__":
    main()