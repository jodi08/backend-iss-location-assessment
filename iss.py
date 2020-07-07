#!/usr/bin/env python
import requests
import turtle
import time


__author__ = 'Jo Anna Mollman (jodi08 on github)'


def get_current_astronauts():
    """Part A Connect to API and get astronaut information"""
    url = "http://api.open-notify.org/astros.json"
    res = requests.get(
        url,
        headers={"Accept": "application/json"}
    )
    data = res.json()
    print("Current astronauts are: ")
    for astro in data["people"]:
        
        print(f"{astro['name']} on the {astro['craft']}")
    print(f"There are {data['number']} astronauts on board")




def iss_coordinates():
    """Part B Get current coordinates of ISS and timestamp"""
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)
    data = res.json()
    print("The current position is: ")
    for k, v in data["iss_position"].items():
        print(k, v)
    print(f"The current timestamp is: {data['timestamp']}")
    
    return data

kenzie_coord = [39.76838, -86.15804]

def get_iss_passover():
    api_url = 'http://api.open-notify.org/iss-pass.json'
    r_indy = requests.get(f'{api_url}?lat={kenzie_coord[0]}&lon=\
        {kenzie_coord[1]}').json()
    indy_next_pass = time.ctime(r_indy['response'][0]['risetime'])
    return [indy_next_pass]

    
def visualize_iss(current, next_pass):
    """Part C make visual to show location of ISS and also list time ISS will next be over Indianapolis, IN"""
    wn = turtle.Screen()
    wn.title("ISS Locator")
    wn.setup(width=720, height=360)

    wn.setworldcoordinates(-180, -90, 180, 90)

    wn.bgcolor("black")
    wn.bgpic("map.gif")
    wn.register_shape("iss.gif")
    
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(90)

    lon = round(float(current["iss_position"]["longitude"]))
    lat = round(float(current["iss_position"]["latitude"]))

    iss.penup()
    iss.goto(lon, lat)
    indy = turtle.Turtle()
    indy.shape("circle")
    indy.color("yellow")
    indy.setheading(90)
    indy_lon = round(float(kenzie_coord[1]))
    indy_lat = round(float(kenzie_coord[0]))
    indy.penup()
    indy.goto(indy_lon, indy_lat)
    indy.write(next_pass[0], font=("Arial", 16, "bold"))
    

    turtle.done()


def main():
    get_current_astronauts()
    current = iss_coordinates()
    next_pass = get_iss_passover()
    visualize_iss(current, next_pass)


if __name__ == '__main__':
    main()
