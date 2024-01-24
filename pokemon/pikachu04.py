#!/usr/bin/python3

import argparse
import requests
import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():
    items = requests.get(f"{ITEMURL}?limit=1000").json()
    matchedwords = []

    for index, item in enumerate(items.get("results"), start=1):
        if args.searchword in item.get("name"):
            matchedwords.append(item.get("name"))
            print(f"{index}. {item.get('name')}")

    finishedlist = matchedwords.copy()

    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print("\n".join([f"{index}. {name}" for index, name in enumerate(finishedlist, start=1)]))

    itemsdf = pandas.DataFrame({"matched": finishedlist})
    itemsdf.index = itemsdf.index + 1  # Adjust index to start from 1
    itemsdf.to_excel("pokemonitems.xlsx", index=True)

    print("Gotta catch 'em all!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search the Pokemon item API")
    parser.add_argument('--searchword', metavar='SEARCHW', type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()
