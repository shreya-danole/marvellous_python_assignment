#Celsius to fahrenheit converter

def main():
    temp = int(input("Enter temperature in Celsius: "))

    Ans = ((temp *(9/5))+32)

    print("Temperature in Fahrenheit: ",Ans,"\u00b0""F")
    
if __name__=="__main__":
    main()
