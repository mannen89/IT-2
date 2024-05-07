import json

# Anta at vi laster inn JSON-data fra en fil kalt 'googleplaystore.json'
with open('Global YouTube Statistics.json', 'r', encoding='utf-8') as file:
    apps_data = json.load(file)

# Opprett en ordbok for å holde oversikt over antall kanaler og totalt antall abonnenter og videovisninger per land
country_channel_stats = {}

# Gå gjennom datasettet og samle statistikk per land
for entry in apps_data:
    country = entry['Country']
    if country != 'nan':  # Ignorer oppføringer uten et gyldig land
        if country not in country_channel_stats:
            country_channel_stats[country] = {
                'channel_count': 0,
                'total_subscribers': 0,
                'total_video_views': 0
            }
        
        country_channel_stats[country]['channel_count'] += 1
        country_channel_stats[country]['total_subscribers'] += entry['subscribers']
        country_channel_stats[country]['total_video_views'] += entry['video views']

# Beregn gjennomsnittlig antall abonnenter og videovisninger per kanal for hvert land
for country, stats in country_channel_stats.items():
    if stats['channel_count'] > 0:  # For å unngå divisjon med null
        stats['average_subscribers'] = stats['total_subscribers'] / stats['channel_count']
        stats['average_video_views'] = stats['total_video_views'] / stats['channel_count']
    else:
        stats['average_subscribers'] = 0
        stats['average_video_views'] = 0

# Sorter landene basert på antall kanaler, i synkende rekkefølge
sorted_countries = sorted(country_channel_stats.items(), key=lambda x: x[1]['channel_count'], reverse=True)

# Skriv ut de ti landene med flest YouTube-kanaler og deres gjennomsnittlige abonnenter og videovisninger
print("De 5 mest populære stasjonene og hvor mange turer som starter der:")
for country, stats in sorted_countries[:10]:
    print(f"{country}: {stats['channel_count']} kanaler, "
          f"Gjennomsnittlige abonnenter: {stats['average_subscribers']:.2f}, "
          f"Gjennomsnittlige videovisninger: {stats['average_video_views']:.2f}")