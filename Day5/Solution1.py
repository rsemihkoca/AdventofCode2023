from pprint import pprint
with open('input.txt', 'r') as file:
    lines = file.read()

lines = lines.strip().split('\n')
total = 0

seeds = lines[0].split()[1:]

seed_to_soil = lines[3:28]
soil_to_fertilizer = lines[30:39]
fert_to_water = lines[41:74]
water_light = lines[76:122]
light_to_temp = lines[124:159]
temp_to_humidity = lines[161:181]
humi_to_location = lines[183:226]



def finder(list_of_values, mapping):
    mapping_dict = {}
    for seed in list_of_values:

        seed_number = int(seed)
        mapping_dict[seed_number] = seed_number
        for value in mapping:
            value = value.split()
            soil = int(value[0])
            seed = int(value[1])
            rangei = int(value[2])
            
            min_number = seed
            max_number = seed + rangei - 1

            if min_number<=seed_number<=max_number:

                mapping_dict[seed_number] = (seed_number-min_number)+soil

    
    return mapping_dict


soils = finder(seeds, seed_to_soil)

pprint(soils)

ferts = finder([*soils.values()], soil_to_fertilizer)
waters = finder([*ferts.values()], fert_to_water)
lights = finder([*waters.values()], water_light)
temps = finder([*lights.values()], light_to_temp)
humis = finder([*temps.values()], temp_to_humidity)
locations = finder([*humis.values()], humi_to_location)


pprint([*locations.values()])

print(min([*locations.values()]))
# ferts = finder(seeds, soil_to_fertilizer)
