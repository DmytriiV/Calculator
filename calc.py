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
    
    if b == 0:
        print("nie można dzielić na zero!")
       
    else: 
        c = a / b
        print("Wynik :"  + str(c) )
        print("Do widzenia")      
elif what == "*":
    c = a * b
    print("Wynik :"  + str(c) )
    print("Do widzenia")
else:
    print("ERROR")

    

    


 



    