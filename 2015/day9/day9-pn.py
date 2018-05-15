#!/usr/bin/env python


import matplotlib.pyplot as plt
import random
import time  
import itertools
import urllib
import csv
import functools
from statistics import mean, stdev


def alltours_tsp(cities):
    "Generate all possible tours of the cities and choose the shortest tour."

    return shortest_tour(alltours(cities))


def shortest_tour(tours):
    "Choose the tour with the minimum tour length"

    return min(tours, key=tour_length)


def tour_length(tour):
    "The total of distances between each pair of consecutive cities in the tour"

    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))


class Point(complex):
    x=property(lambda p : p.real)
    y=property(lambda p : p.imag)

City=Point

def distance(A, B):
    "The distance between two points"

    return abs(A-B)


def Cities(n, width=900, height=600, seed=42):

    random.seed(seed*n)

    return frozenset(City(random.randrange(width), random.randrange(height)) for c in range(n))


def plot_tour(tour):
    plot_lines(list(tour)+[tour[0]])


def plot_lines(points, style='bo-'):
    plt.plot([p.x for p in points], [p.y for p in points], style)
    plt.axis('scaled'); plt.axis('off')


def plot_tsp(algorithm, cities):
    t0=time.clock()
    tour=algorithm(cities)
    t1=time.clock()
    assert valid_tour(tour, cities)
    plot_tour(tour); plt.show()
    print ("{} city tour with length {:.1f} in {:.3f} secs for {}"
           .format(len(tour), tour_length(tour), t1-t0, algorithm.__name__))
    

def valid_tour(tour, cities):
    return set(tour) == set(cities) and len(tour) == len(cities)

alltours=itertools.permutations

cities={1, 2, 3}

list(alltours(cities))

plot_tsp(alltours_tsp, Cities(8))

plt.show()
