print("Step 1: Pick your vehicle")
print(" 1 - bike")
print(" 2 - car")
print()

choice = int(input("Enter 1 or 2: "))
print()


if choice == 1:
    print("Step 2: Pick your type bike")
    print(" 1 - Scooty")
    print(" 2 - Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2"))
    print()

    if bike_type == 1:
        print("You picked : Scooty")
        print("Top Speed : 80km/h")
        print("Best for : City Roads")
    else:
        print("You picked : Mountain Bike")
        print("Top Speed : 40km/h")
        print("Best for : Off-road trails")

elif choice == 2:
     if choice == 1:
        print("Step 2: Pick your car type")
        print(" 1 - Lamborginni")
        print(" 2 - BMW")
        print()

    car_type = int(input("Enter 1 or 2"))
    print()

    if car_type == 1:
        print("You picked : Lamborginni")
        print("Top Speed : 100km/h")
        print("Best for : City Roads")
    else:
        print("You picked : BMW")
        print("Top Speed : 50km/h")
        print("Best for : City Roads")

else:
    print("That wasn't a valid choice")
    print("Please enter 1 for Bike or 2 for Car")

print()
print("========================================")
print("        Your custom ride is ready!      ")
print("        Enjoy your custom journey!      ")
print("========================================")
