#!/usr/bin/python3
"""Alta3 Research - RZFeeser 
   SOLUTION 01 - Returning names to house and books with GOT API."""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

# check on the names of data passed
def name_finder(got_list):
    names = []  # list to return back of decoded names
    for x in got_list:
        try:
            # send HTTP GET to one of the entries within the list
            r = requests.get(x)
            decodedjson = r.json() # decode the JSON on the response
            names.append(decodedjson.get("name"))  # this returns the housename and adds it to our list
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            names.append("Error")
    return names  # when operation is over, send it back

def main():
    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

    try:
        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)
        gotresp.raise_for_status()  # raise an HTTPError for bad responses

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        # call our function
        print("This character belongs to the following houses:")
        for x in name_finder(got_dj.get("allegiances")):
            print(x)

        print("This character appears in the following books:")
        for x in name_finder(got_dj.get("books")):
            print(x)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()

