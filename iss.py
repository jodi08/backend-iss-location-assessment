#!/usr/bin/env python
import requests


__author__ = 'Jo Anna Mollman (jodi08 on github)'

url = "http://api.open-notify.org/astros.json"

def get_current_astronauts():
    """Connect to API and get astronaut information"""
    res = requests.get(
        url,
        headers={"Accept": "application/json"}
    )
    data = res.json()
    print("Current astronauts are: ")
    for astro in data["people"]:
        
        print(f"{astro['name']} on the {astro['craft']}")
    print(f"There are {data['number']} astronauts on board")


get_current_astronauts()

def iss_coordinates():
    """Get current coordinates of ISS and timestamp"""
    pass


def visualize_iss():
    """make visual to show location of ISS and also list time ISS will next be over Indianapolis, IN"""
    pass


def main():
    pass


if __name__ == '__main__':
    main()
