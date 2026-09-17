temprature= int(input("How much is the temprature"))
if temprature < 20:
    print("Wear a sweater")
else: 
    print("wear a shirt")
weather= (input("Is it raining"))
if weather== "yes":
    print("Bring an umbrella")
else:
    print("Don't bring an umbrella")
windspeed= int(input("How much is the windspeed today?"))
if windspeed > 30:
    print("It's windy today, don't forget your windbreaker!")
else:
    print("It's not windy today, no need for your windbreaker!")
puddles= (input("Are there puddles on the ground?"))
if puddles== "yes":
    print("It's rainy today so there will be puddles. Wear your boots!")
else:
    print("There's no sign of puddles, you are safe to wear your shoes!")
print("temprature", temprature)
print("weather", weather)
print("windspeed", windspeed)
print("puddles", puddles)
