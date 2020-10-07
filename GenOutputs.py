#!/usr/bin/env python

import GetObjects
from UserLocation import Location
import pandas as pd
import matplotlib.pyplot as plt


def visible_objects():
    '''
    Returns the stars and constellations that are visible to the user.
    '''
    my_stars = GetObjects.get_stars()
    stars_up = Location(targets=my_stars).whats_visible()
    my_consts = GetObjects.get_constellations()
    consts_up = Location(targets=my_consts).whats_visible()

    stars_dict = {
                  'ObjID': [(stars_up[n].name) for n in range(len(stars_up))],
                  'RA': [(stars_up[n].ra.value) for n in range(len(stars_up))],
                  'DEC': [(stars_up[n].dec.value) for n in range(len(stars_up))]
                  }

    consts_dict = {
                  'Name': [(consts_up[n].name) for n in range(len(consts_up))],
                  'RA': [(consts_up[n].ra.value) for n in range(len(consts_up))],
                  'DEC': [(consts_up[n].dec.value) for n in range(len(consts_up))]
                   }

    stars_df = pd.DataFrame(data=stars_dict)
    constellations_df = pd.DataFrame(data=consts_dict)

    return stars_df, constellations_df


def star_visualization(obj):
    '''
    PLots RA and DEC of visible stars.
    '''
    fig, ax = plt.subplots()
    ax.scatter(obj['RA'], obj['DEC'], marker='.')
    ax.set_aspect('equal')
    ax.set_xlabel('RA')
    ax.set_ylabel('DEC')
    ax.set_title('Stars')
    plt.savefig('./Outputs/stars.png')


def const_visualization(obj):
    '''
    PLots RA and DEC of the center of visible constellations.
    '''
    fig, ax = plt.subplots()
    ax.scatter(obj['RA'], obj['DEC'], marker='.')
    ax.set_aspect('equal')
    ax.set_xlabel('RA')
    ax.set_ylabel('DEC')
    ax.set_title('Constellations')
    plt.savefig('./Outputs/constellations.png')
