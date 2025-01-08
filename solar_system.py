from space_object import SpaceObject
from ellipse import Ellipse
from space_station import SpaceStation
from data import star_colors, english_alphabet

import numpy as np
import random
import math

class SolarSystem:
    def __init__(self, star_pos, star_name, num_planets, star_radius, planet_speed_range, scene_manager, planets=[], station=None, station_has_player=False, system_has_station=False):
        self.star_pos = np.array(star_pos)
        self.num_planets = num_planets
        self.planet_speed_range = planet_speed_range

        self.station_has_player = station_has_player

        radius = star_radius
        color = random.choice(star_colors)
        self.star = SpaceObject(radius, color, star_pos, type="Star", name=star_name)

        self.station = station
        
        if self.station == None:
            if system_has_station:
                pass # Generate Station
        else:
            self.station.follow_planet = self.star

        self.planets = planets
        self.scene_manager = scene_manager

        if self.planets == []:
            for i in range(random.randint(1, 10)):
                radius = random.randint(1, 40)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                ellipse = Ellipse(random.randint(random.randint(40, 100)+40*i, random.randint(100, 200)+40*i), random.randint(random.randint(40, 100)+40*i, random.randint(100, 200)+40*i), math.radians(random.randint(0, 360)))
                speed = random.randint(self.planet_speed_range[0], self.planet_speed_range[1])/100000
                planet = SpaceObject(radius, color, ellipse=ellipse, follow_planet=self.star, type="Planet", speed=speed)
                planet.scene_manager = self.scene_manager
                self.planets.append(planet)
                

        else:
            for planet in self.planets:
                planet.follow_planet = self.star
                planet.scene_manager = self.scene_manager
                if self.planets.index(planet) < len(english_alphabet):
                    planet.name = self.star.name + " " + english_alphabet[self.planets.index(planet)].upper()

                else:
                    planet.name = self.star.name + " " + str(self.planets.index(planet)//len(english_alphabet)) + english_alphabet[self.planets.index(planet)%len(english_alphabet)].upper()


    def update(self):
        self.station.scene_manager = self.scene_manager
        self.star.scene_manager = self.scene_manager

        for planet in self.planets:
            planet.update()
            planet.follow_planet = self.star
            planet.scene_manager = self.scene_manager

        self.station.update()

    def draw(self, display, camera, draw_orbits=False, scene="game"):
        self.station.draw(display, camera, scene=scene, draw_with_angle=not (self.station_has_player and scene == "game"))
        self.star.draw(display, camera, draw_orbits)
        for planet in self.planets:
            planet.draw(display, camera, draw_orbits)