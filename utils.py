import pygame
import numpy as np
import math
from data import *
import random

def rotate(point, angle):
    R = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ])

    return point @ R

def draw_ellipse_angle(display, color, a, b, center, camera, angle, width=0):
    target_rect = pygame.Rect(-a+center[0], -b+center[1], 2*a, 2*b)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, 180*angle/math.pi)
    scaled_surf = pygame.transform.scale(rotated_surf, (rotated_surf.get_width()*camera.zoom, rotated_surf.get_height()*camera.zoom))
    display.blit(scaled_surf, scaled_surf.get_rect(center = np.array(target_rect.center)*camera.zoom - camera.pos))


def rotate_planet(v, alpha, beta, gamma):
  yaw = np.array([[math.cos(alpha), -math.sin(alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
  pitch = np.array([[math.cos(beta), 0, math.sin(beta)], [0, 1, 0], [-math.sin(beta), 0, math.cos(beta)]])
  roll = np.array([[1, 0, 0], [0, math.cos(gamma), -math.sin(gamma)], [0, math.sin(gamma), math.cos(gamma)]])
  return v @ pitch @ roll @ yaw

def draw_planet_frame(screen, color, pos, radius, alpha = 0, beta = -math.pi / 17, gamma = -math.pi / 4):
  offset = np.array([pos[0], pos[1], 0])

  points = []

  lats = 16
  longs = 32

  for i in range(longs):
    a = i * 2 * math.pi / longs
    ring = []
    for j in range(lats):
      b = j * 2 * math.pi / lats

      point = np.array([math.cos(b) * math.sin(a), math.sin(b) * math.sin(a), math.cos(a)]) * radius
      point = rotate_planet(point, alpha, beta, gamma) + offset
      ring.append(point)
    
    points.append(ring)
  
  for i in range(len(points) - 1):
    ring = points[i]
    next_ring = points[i+1]
    for j in range(len(ring)):
      #pygame.draw.circle(screen, (0,255,0), ring[j][:2], 2)
      T = -0.05 * radius
      if ring[j][2] > T or next_ring[j][2] > T:
        pygame.draw.line(screen, color, ring[j][:2], next_ring[j][:2])
      if ring[j][2] > T or ring[(j + 1)%len(ring)][2] > T:
        if i % 3 == 0:
          pygame.draw.line(screen, color, ring[j][:2], ring[(j + 1)%len(ring)][:2])
      
  pygame.draw.circle(screen, color, offset[:2], radius, width=1)

def draw_planet(screen, color, pos, radius, alpha=0.0, beta=-math.pi/17, gamma=-math.pi/4):
  pygame.draw.circle(screen, color, pos, 0.1 * radius, width = 1)
  pygame.draw.circle(screen, color, pos, 0.07 * radius, width = 1)
  pygame.draw.circle(screen, color, pos, 0.03 * radius, width = 1)
  pygame.draw.line(screen, color, (pos[0] - radius * .15, pos[1]), (pos[0] + radius * .15, pos[1]), width = 1)
  pygame.draw.line(screen, color, (pos[0], pos[1] - radius * .15), (pos[0], pos[1] + radius * .15), width = 1)
  draw_planet_frame(screen, color, pos, radius, alpha=alpha, beta=beta, gamma=gamma)

def draw_label(screen, color, pos, length, text, is_up = True):

  font = pygame.font.SysFont('candara', 20)
  
  label_text = font.render(text, False, color)

  text_width, text_height = font.size(text)

  corner = (pos[0] + length, pos[1] + (-length if is_up else length))
  pygame.draw.line(screen, color, pos, corner, width = 1)
  pygame.draw.line(screen, color, corner, (corner[0] + text_width, corner[1]))

  screen.blit(label_text, (corner[0], corner[1] - text_height))

  label_rect = label_text.get_rect()
  label_rect.x = corner[0]
  label_rect.y = corner[1] - text_height

  return label_rect


def generate_star_name():
    name = random.choice(star_names)
    if random.randint(0, 1) == 1:
       name += " " + random.choice(greek_alphabet)
       return name
    return name