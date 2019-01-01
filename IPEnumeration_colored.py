import shodan
import sys
from colorama import Style, Back
from time import sleep

# Configuration
API_KEY = "kYSjmGrndxVfIx6LhIGQ5XW1kXo2oPsV"

# Input validation
if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]} <search query>')
        sys.exit(1)

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)

    # Perform the search
    query = ' '.join(sys.argv[1:])
    result = api.search(query)      # query returns ip addresses
    ipAddrs = []                    # create empty list to house IP's

    for ips in result['matches']:   # loop through return IP's and add to list
        ipAddrs.append(str(ips['ip_str']))

    for x in ipAddrs:               # loop through IP address list
        result2 = api.host(f"{x}")  # API query for each IP
        # print(result2['data'])    # Raw, un-parsed data
        city = result2['city']
        region = result2['region_code']
        postal = result2['postal_code']
        country = result2['country_code']
        tags = ', '.join(result2['tags'])
        isp = result2['isp']
        update = result2['last_update']
        hostname = ', '.join(result2['hostnames'])
        org = result2['org']
        ip_str = result2['ip_str']

        print(Back.MAGENTA + '  ' + Style.RESET_ALL + f' IP:\t\t{ip_str}')
        print(Back.LIGHTGREEN_EX + '  ' + Style.RESET_ALL + f' Location:\t{city}, {region} {postal} {country}')
        print(Back.BLUE + '  ' + Style.RESET_ALL + f' Tag:\t\t{tags}')
        print(Back.LIGHTRED_EX + '  ' + Style.RESET_ALL + f' ISP:\t\t{isp}')
        print(Back.CYAN + '  ' + Style.RESET_ALL + f' Updated:\t{update}')
        print(Back.LIGHTYELLOW_EX + '  ' + Style.RESET_ALL + f' Hostnames:\t{hostname}')
        print(Back.RED + '  ' + Style.RESET_ALL + f' Org:\t\t{org}\n')

        # empty list variables to hold data dictionary values
        ports = []
        transport = []
        data = []
        for keys in result2['data']:    # loop through all keys in data dict
            for x, y in keys.items():   # for each key/value pair
                if x == 'port':         # search for port & append to list
                    ports.append(y)
                if x == 'transport':    # search for transport & append to list
                    transport.append(y)
                if x == 'data':         # search for data & append to list
                    data.append(y)

        counter = 0
        for items in ports:                 # use ports as iteration baseline
            print(Back.GREEN + '  ' + Style.RESET_ALL + f' Port: {ports[counter]}/{transport[counter]}')
            print(f'{data[counter]}')
            counter += 1

        print('<===========================================================================>\n')
        sleep(1)    # sleep 1 second before next API call

except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)
