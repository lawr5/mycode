#!/usr/bin/python3

import requests

issurl = "http://api.open-notify.org/iss-now.json"

def main():

    issrequest = requests.get(issurl)

    issdata = issrequest.json()

    print(issdata)

    lon = issdata['iss_position']['longitude']
    lat = issdata['iss_position']['latitude']

    print(f"""
    Current location of the ISS:
    Longitude: {lon}
    Latitude: {lat}
    """)

if __name__ == "__main__":
    main()

