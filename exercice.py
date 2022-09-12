#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return math.pow(a, 2)


def average(a: float, b: float, c: float) -> float:

    return (a+b+c)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degs = angle_secs*(1/3600)
    degs = degs + angle_mins*(1/60)
    degs = degs+ angle_degs
    return math.radians(degs)


def to_degrees(angle_rads: float) -> tuple:
    degs = math.degrees(angle_rads) # Transforme radians en degrés
    mins = (degs - math.floor(degs))* 60 # degrés moins sa partie entière donne le nombre de minute
    secs = (mins - math.floor(mins)) * 60 # minutes moins sa partie entière donne le nombre de secondes
    return math.floor(degs), math.floor(mins), secs

#test

def to_celsius(temperature: float) -> float:
    return (temperature - 32)/1.8


def to_farenheit(temperature: float) -> float:
    return temperature * 1.8 + 32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
