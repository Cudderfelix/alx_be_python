weather = "sunny", "rainy", "cold"
get_weather_advice = str(input("Enter the weather condition (sunny, rainy, cold): "))
if get_weather_advice == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif get_weather_advice == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif get_weather_advice == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Invalid weather condition entered. Please try again.")
print("Thank you for using the weather advice program!")    