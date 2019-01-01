import shodan
import sys

# Configuration
API_KEY = "[Shodan API Key]"

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
        tags = result2['tags']
        isp = result2['isp']
        update = result2['last_update']
        hostname = ' '.join(result2['hostnames'])
        org = result2['org']
        ip_str = result2['ip_str']

        print(f'{ip_str}')
        print(f'Location: {city}, {region} {postal} {country}')
        print(f'Tag: {tags}')
        print(f'ISP: {isp}')
        print(f'Last Update: {update}')
        print(f'Hostnames: {hostname}')
        print(f'Org: {org}\n')

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
            print(f'{ports[counter]} / {transport[counter]}')
            print(f'{data[counter]}')
            counter += 1

        print('\n---------------------------------------------\n')


except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)
