import json

# Anta at vi laster inn JSON-data fra en fil kalt 'googleplaystore.json'
with open('twitterbrukere.json', 'r', encoding='utf-8') as file:
    apps_data = json.load(file)

# Sorter data basert på antall følgere, i synkende rekkefølge
sorted_data = sorted(apps_data, key=lambda x: x['followers'], reverse=True)

# Skriv ut de ti brukerne med flest følgere, deres antall tweets, og følgere/følger-ratio
for user in sorted_data[:10]:
    # Beregn følgere/følger-ratio og håndter deling med null
    if user['following'] == 0:
        followers_to_following_ratio = float('inf')  # Uendelig, siden deling med null ikke er tillatt
    else:
        followers_to_following_ratio = user['followers'] / user['following']
    
    print(f"Username: {user['username']}, "
          f"Tweets: {user['tweets']}, "
          f"Followers: {user['followers']}, "
          f"Following: {user['following']}, "
          f"Followers/Following Ratio: {followers_to_following_ratio:.2f}")
