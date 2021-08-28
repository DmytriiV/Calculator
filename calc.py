#Kalkulator

what = input( "Co robimy? (+, -, *, /)")

a = float( input("Wprowadż pierwszą liczbe: "))
b = float( input("Wprowadż drugą liczbe: "))

if what == "+":
    c = a + b
    print("Wynik :"  + str(c) )
    print("Do widzenia")
elif what == "-":
    c = a - b 
    print("Wynik :"  + str(c) )
    print("Do widzenia")
elif what == "/":
    c = a / b
    if b == 0:
        print("Деление на 0!")
    
        print("Wynik :"  + str(c) )
        print("Do widzenia")    
elif what == "*":
    c = a * b
    print("Wynik :"  + str(c) )
    print("Do widzenia")
else:
    print("ERROR")

    

    


 



    