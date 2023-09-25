
def find_name(line_parts):
    return line_parts[0]

def find_currency(line_parts):
    return line_parts[1]

def find_literacy(line_part):
    return int(line_part[2])

def find_time_zone(line_part):
    return float(line_part[3])

def find_cont(line_part):
    return line_part[4]

def find_main_lang(line_part):
    return line_part[5]


def find_most_spoken(line_part):
    return line_part[6] if len(line_part) == 7 else ''

def parse_input_file(file):
    continents = {}
    with open('data.txt','r') as f:
        for line in f:
            line_parts = line.strip().split(', ')
            name = find_name(line_parts)

            currency = find_currency(line_parts)

            literacy = int(find_literacy(line_parts))

            time_zone = float(find_time_zone(line_parts))

            cont = find_cont(line_parts)

            main_lang = find_main_lang(line_parts)

            most_spoken = (find_most_spoken(line_parts))

            if cont not in continents:
                continents[cont] = {
                'name': cont,
                'currency': currency,
                'literacy_rate': literacy,
                'time_zone': time_zone,
                'main_language': main_lang,
                'most_lang': most_spoken,
                'countries': []

            }
            continents[cont] ['countries'].append(name)

    return sorted(continents.values(), key = lambda x: x['name'])
if __name__ == '__main__':
    input_file =open("data.txt","r")
    continents = parse_input_file(input_file)
    for continent in continents:
        print(f"Name of Continent:{continent['name']}")
        print(f"Currency:{continent['currency']}")
        print(f"Literacy rate:{continent['literacy_rate']}")
        print(f"Time Zone:{continent['time_zone']}")
        print(f"Main Language:{continent['main_language']}")
        print(f"Most Spoken Language:{continent['most_lang']}")
        print('Countries:')
        for i in continent['countries']:
            print(i)
        print()
