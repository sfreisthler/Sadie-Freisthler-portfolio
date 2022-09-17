from collections import defaultdict

def read_market_data(filename):
    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """
    # initialize dictionaries 
    zip_to_market = defaultdict(list)
    town_to_market = defaultdict(set)

    with open(filename, 'r') as f:
        for line in f:
            # remove whitespace
            line.strip()
            fields = line.split('@')
                
            # define variables
            zip = fields[4]
            market_info = fields[:5]
            town = fields[3]

            if fields[4] != "" and fields[4] != 'none':
                # populate zip_to_market dictionary 
                zip_to_market[zip].append(tuple(market_info))

                # populate town_to_market dictionary
                town_to_market[town].add(zip)

    return zip_to_market, town_to_market 

def print_market_data(market):
    """
    Returns a human-readable string representing the farmers market tuple
    passed to the market parameter.
    """
    name = market[1]
    location = market[2]
    city_state_zip = market[3] + ', ' + market[0] + ' ' + market[4]

    formated_info = f"{name}\n{location}\n{city_state_zip}\n"

    return formated_info

if __name__ == "__main__":

    # This main program first reads in the markets.txt once (using the function
    # from part (a)), and then asks the user repeatedly to enter a zip code or
    # a town name (in a while loop until the user types "quit").

    FILENAME = "markets.txt"

    try: 
        zip_to_market, town_to_zips = read_market_data(FILENAME) 
        
        running = True 
        while running == True:
            print("Enter a city name or zip code to find farmers markets in your area!")
            user_input = input("Input 'quit' to quit. ")

            # if user input is a zip code, print markets in that zip code
            if user_input == 'quit':
                running = False   

            elif user_input.isdigit():

                # print error if zip is not found
                if not user_input in zip_to_market:
                    print("Not found")
                else:
                    # input is zip, use zip_to_market dictionary
                    markets = zip_to_market[user_input]
                    for market in markets:
                        print(print_market_data(market))
            
            # if user input is a city, print markets in city
            elif not user_input.isdigit():

                # print error if city is not found
                if not user_input in town_to_zips:
                    print("Not found.")
                else:
                    zips = town_to_zips[user_input]
                    for zip in zips:
                        markets = zip_to_market[zip]
                        for market in markets:
                            print(print_market_data(market))


    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
