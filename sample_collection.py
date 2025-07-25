# Create a sample collection of top Nigerian songs and artists
sample_collection = {"psquare": ["Chop My Money", "Personally", "No One Like You"], "Burna Boy": ["Ye", "Gbona", "Anybody"], "Wizkid": ["Ojuelegba", "Joro", "Essence"], "Davido": ["Fall", "If", "Fia"], "Tiwa Savage": ["All Over", "Ma Lo", "49-99"]}

#filter_strategy: Iterate over a copy
for artist, songs in sample_collection.items():
    print(f"Artist: {artist}")
    for song in songs:
        print(f" - Song: {song}")
    print()  # Print a newline for better readability
# This code creates a sample collection of top Nigerian songs and artists and prints them in a formatted way.
# The collection is a dictionary where the keys are artist names and the values are lists of their popular songs.
# The code iterates over the dictionary and prints each artist along with their songs in a readable format.
# The output will show each artist followed by their songs, making it easy to read and understand.
# Output:
# Artist: psquare
#  - Song: Chop My Money
#  - Song: Personally
#  - Song: No One Like You:

def log_crop_prices():
    """Log crop names and prices using a for loop, formatting prices with commas."""
    crops = [] # Empty list to store crops data
    print("Enter crop name and price (NGN). Type 'done' for name to finish.")

    while True:
        name  = input("Enter crop name:").lower()
        if name == 'done':
            break
        try:
            price = float(input("Enter crop price (NGN):"))
            crops.append({"name": name, "price": price})
        except ValueError:
            print("invalid price. Please enter a number.")
    if crops:
        print("\n Crop Price List:")
        for crop in crops: # Loop through list
            formatted_price = "{:,}".format(int(crop["price"]))
            print(f"{crop['name'].capitalize()}:NGN {formatted_price}")
    else:
        print("No crops logged")
    return crops
# Example usage:
logged_crops = log_crop_prices()    