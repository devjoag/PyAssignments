def main():
            no=int(input("Enter Number: "))
            for i in range(1,no+1):
                strp=""
                for j in range(1,i+1):
                    strp="{}{}{}".format(strp,j,"  ")
            
                print(strp)                        
if(__name__) == "__main__":
    main()