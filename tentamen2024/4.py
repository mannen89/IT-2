import json

with open('sykkelturer.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

stasjoner = {

}

for ting in data:
    startsted = ting['start_station_name']
    tider = ting['duration']
    if startsted not in stasjoner:
        stasjoner[startsted] = {
            'antall_turer': 0
            }
        
tider = {

}

for ting in data:
    duration = ting['duration']
    tid = int(tid)
    if duration not in tider:
        pass

    #prøver å konvertere duration fra str til int

for ting in data:
    
        
    stasjoner[startsted]['antall_turer'] += 1
        
sorterte_stasjoner = sorted(stasjoner.items(), key=lambda x: x[1]['antall_turer'], reverse=True)

sorterte_tider = sorted(data, key=lambda x: x['duration'], reverse=True)




print("De 5 mest populære stasjonene og hvor mange turer som starter der:")
for startsted, stats in sorterte_stasjoner[:5]:
    print(f"{startsted}: {stats['antall_turer']} startstasjoner, ")    
for tider in sorterte_tider[:3]:
      print(f"start: {tider['start_station_name']}, "
            f"slutt: {tider['end_station_name']}, "
            f"varighet: {tider['duration']}")
      
      #jeg fikk det til men siden duration er en str så tenker den at 999 er større enn 1000 siden 9 er høyere enn 1