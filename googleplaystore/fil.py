import json

# Anta at vi laster inn JSON-data fra en fil kalt 'googleplaystore.json'
with open('googleplaystore.json', 'r', encoding='utf-8') as file:
    apps_data = json.load(file)

def rens_rating(rating_str):
    rating_str == int(rating_str)