import json

# Anta at vi laster inn JSON-data fra en fil kalt 'googleplaystore.json'
with open('googleplaystore.json', 'r', encoding='utf-8') as file:
    apps_data = json.load(file)

# Funksjon for å rense og konvertere installasjonsstrengen til et heltall
def clean_rating(rating_str):
    try:
        # Konverter til flyttall hvis mulig
        return int(rating_str)
    except ValueError:
        # Returner None hvis konvertering mislykkes
        return 0 

def clean_installs(installs_str):
    # Fjern '+' og ',' fra strengen, og konverter til int
    if installs_str[-1] == '+':
        return int(installs_str.replace('+', '').replace(',', ''))
    return 0

# Oppdater beregningslogikken for å håndtere None-verdier og summere gyldige verdier
def calculate_top_categories(apps_data):
    categories = {}
    for app in apps_data:
        category = app['Category']
        rating = clean_rating(app['Rating'])
        installs = clean_installs(app['Installs'])

        if category not in categories:
            categories[category] = {'count': 0, 'valid_ratings_count': 0, 'total_rating': 0, 'total_installs': 0}

        categories[category]['count'] += 1
        if rating is not None:
            categories[category]['valid_ratings_count'] += 1
            categories[category]['total_rating'] += rating
        categories[category]['total_installs'] += installs

    for category in categories:
        if categories[category]['valid_ratings_count'] > 0:
            categories[category]['average_rating'] = categories[category]['total_rating'] / categories[category]['valid_ratings_count']
        else:
            categories[category]['average_rating'] = 'Ingen gyldige ratings'
        categories[category]['average_installs'] = categories[category]['total_installs'] / categories[category]['count']

    sorted_categories = sorted(categories.items(), key=lambda x: x[1]['count'], reverse=True)
    return sorted_categories[:3]

# Resten av koden...


# Funksjon for å beregne de tre største kategoriene
def calculate_top_categories(apps_data):
    categories = {}
    for app in apps_data:
        category = app['Category']
        rating = float(app['Rating'])
        installs = clean_installs(app['Installs'])

        if category not in categories:
            categories[category] = {'count': 0, 'total_rating': 0, 'total_installs': 0}

        categories[category]['count'] += 1
        categories[category]['total_rating'] += rating
        categories[category]['total_installs'] += installs

    for category in categories:
        categories[category]['average_rating'] = categories[category]['total_rating'] / categories[category]['count']
        categories[category]['average_installs'] = categories[category]['total_installs'] / categories[category]['count']

    sorted_categories = sorted(categories.items(), key=lambda x: x[1]['count'], reverse=True)
    return sorted_categories[:3]

# Beregn de tre største kategoriene
top_categories = calculate_top_categories(apps_data)

# Skriv ut oversikten over de tre største kategoriene
for category, data in top_categories:
    print(f"Kategori: {category}")
    print(f"Antall Apper: {data['count']}")
    print(f"Gjennomsnittsrating: {data['average_rating']:.2f}")
    print(f"Gjennomsnittlige Installasjoner: {data['average_installs']:.2f}")
    print()
