# 1. Imports
import shodan
import argparse
import sys
from colorama import Style, Back
from time import sleep

# 2. API KEY Configuration
API_KEY = "kYSjmGrndxVfIx6LhIGQ5XW1kXo2oPsV"


# 3.
def ips(x):                             # IP Address wordlist function
    with open(x.strip()) as f:          # open file passed as argument
        for line in f:                  # for each line (i.e. ip addr)
            ip = line.strip()
            query(ip)                   # pass to query function


# 4.
def domains(x):                         # Domain wordlist function
    with open(x.strip()) as f:          # open file passed as argument
        for line in f:                  # for each line (i.e. domain)
            domain = line.strip()
            query(domain)               # pass to query function


# 5.
def search(x):                          # Search function
    query(x)                            # directly pass input argument to query function


# 6. Main Query Function - 99% of work done here
def query(x):
    try:
        api = shodan.Shodan(API_KEY)    # setup the API
        query = f'{x}'                  # define query variable
        result = api.search(query)      # Call API and return query results

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
            for items in ports:             # use ports as iteration baseline
                print(Back.GREEN + '  ' + Style.RESET_ALL + f' Port: {ports[counter]}/{transport[counter]}')
                print(f'{data[counter]}')
                counter += 1

            print('<===========================================================================>\n')
            sleep(1)    # sleep 1 second before next API call, so we don't get cut-off by Shodan

    except Exception as e:
            print(f'Error: {e}')
            sys.exit(1)


# 7. main argument function
def main():
    # 7.1. Argparse help menu: display help menu
    parser = argparse.ArgumentParser(description='Description......')
    # 7.2. define flags
    parser.add_argument('-s', '--search', help='Enter a Shodan search query', required=False)
    parser.add_argument('-i', '--ips', help='Enter the wordlist file name containing IP addresses', required=False)
    parser.add_argument('-d', '--domain', help='Enter the wordlist file name containing domain names', required=False)

    # 7.3. save input as variables
    args = parser.parse_args()
    searchArg = str(args.search).lower()
    ipsArg = str(args.ips).lower()
    domainArg = str(args.domain).lower()

    # 7.4. function decision tree, based on input
    if searchArg != "none":
        search(searchArg)
    elif ipsArg != "none":
        ips(ipsArg)
    elif domainArg != "none":
        domains(domainArg)
    else:
        print("oops! Wrong argument, please read the help menu and try again.")


# 8. Main function call to kick-off the whole chain of events
main()
