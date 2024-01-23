#!/usr/bin/env python3
"""Alta3 Research
   CHALLENGE SOLUTION 02
   He first appeared in the movie {A New Hope} and could be found flying around in his {TIE Advanced x1}."""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

#URL = "https://swapi.dev/luke/force"      # Comment out this line
URL= "https://swapi.dev/api/people/4/"     # Uncomment this line

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader= resp.json()
        pprint(vader)

    else:
        print("That is not a valid URL.")


    # CHALLENGE 02 - SOLUTION
    # Create the following:
    # He first appeared in the movie {A New Hope} and could be found flying around in his {TIE Advanced x1}.
    
    # pick up the name of the first movie
    resp = requests.get(vader['films'][0])
    first_movie = resp.json() # skip checking for the 200

    # pick up the name of his ship
    resp = requests.get(vader['starships'][0])
    ship = resp.json() 

    # this solution uses "f-strings" (string templates) to return the data
    print(f"He first appeared in the movie {first_movie['title']} and could be found flying around in his {ship['name']}.")



if __name__ == "__main__":
    main()
