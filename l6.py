print("===Smart School Day Planner===")
day = input("What day is it? (Monday to Sunday)").strip().capitalize()
weather = input("What is the weather? (sunny/rainy/cloudy)").strip().lower()
homework = input("Is your homework done? (yes/no)").strip().lower()
print()
print(f"=== Your Plan for the {day} ===")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print(" Weekend - enojy your free time!")
elif day == "Monday":
    print("First day of the week. Pack your weekly planner")
elif day == "Friday":
    print("Last school day.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Regular school day")
else:
    print("Day not recognised.")

if weather == "sunny" and "homework" == "yes":
    print("Great weather and homework is done!")

if weather == "rainy" or "weather" == "cloudy":
    print("Pack ur umbrella might be wet")

if not (homework == "yes"):
    print("homework not done yet finish it before going to play")

if weather == "rainy" and not (homework == "yes"):
    print("Stay in and finish ur homework they watch ur fav tv show")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("perfect weekend weather head out side and have fun!")
else:
    print("Best plan : Take it one step at a time i believe in you got this commit and succeed")
print()
print("Pan completed have a wonderful day and keep doing ur homework")
