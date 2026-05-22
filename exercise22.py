name = input("qual seu nome? ")
god = "God bless you"

while True:

    try:
        age = int(input("digite a sua idade: "))
        print(f"seu nome é {name}, sua idade é {age}, {god}, {name}")
        break

    except:
        print("isso não é número!")
