# Function to generate gardening advice based on season and plant type
def get_gardening_advice(season, plant_type):
    # Variable to hold the gardening advice
    advice = ""

    # Determine advice based on the season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice


# Get the season and plant type from the user
season = input("Enter the season (summer/winter): ").lower()
plant_type = input("Enter the plant type (flower/vegetable): ").lower()

# Generate and display the gardening advice
advice = get_gardening_advice(season, plant_type)
print(advice)

# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.