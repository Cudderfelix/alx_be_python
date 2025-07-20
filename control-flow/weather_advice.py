weather = "sunny", "rainy", "cold"
get_weather_advice = str(input("What's the weather like today? (sunny/rainy/cold): "))
if get_weather_advice == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif get_weather_advice == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif get_weather_advice == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry I don't have recommendations for this weather.")
print("Thank you for using the weather advice program!")  