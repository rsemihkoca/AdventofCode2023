from pprint import pprint
from collections import OrderedDict


with open('input.txt') as f:
    lines = f.read()
    
    total = 0

    results = OrderedDict()

    for line in lines.strip().split('\n'):

        ID, content = line.split(':')

        ID = ID.split(' ')[1]

        results[ID] = []

        content = content.strip().split(';')


        for input_string in content:
            
            parts = input_string.split(',')

            # Create a dictionary to store the results
            color_count = {'blue': 0, 'green': 0, 'red': 0}

            # Process each part and update the dictionary
            for part in parts:
                
                # Split each part into count and color
                count_color = part.strip().split()
                
                # Set default count to 0 if not present
                count = int(count_color[0]) if count_color[0].isdigit() else 0
                
                # Get the color (skipping the count if present)
                color = count_color[-1]
                
                # Update the dictionary
                color_count[color] = count
            
            results[ID].append(color_count)
        
        pprint(results)

        for key, value in results.items():


            blue = 0
            red = 0
            green = 0

            for game in value:

                red = max(red, game['red'])
                blue = max(blue, game['blue'])
                green = max(green, game['green'])


            value = red * blue * green
            total += value

        print(sum(total))



"""
113600
2913 **

"""