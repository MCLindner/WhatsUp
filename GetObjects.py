#!/usr/bin/env python

from astroquery.sdss import SDSS
from astropy.coordinates import SkyCoord
from astroplan import FixedTarget
import astropy.units as u
import pandas as pd
from pathlib import Path


def get_stars():
    '''
    Querys SDSS for a list of bright stars.
    '''
    query = """
            select top 25
                u as magnitude, ra, dec, objID
            FROM
                Star
            WHERE (u > -9999)
            ORDER by magnitude
            """

    res = SDSS.query_sql(query)

    targets = [FixedTarget(coord=SkyCoord(ra=ra*u.hourangle, dec=dec*u.deg), name=objID)
               for objID, ra, dec, magnitude in res]

    return targets


def get_constellations():
    '''
    Loads in a list of constellations from /Targets/Constelations.csv.
    '''
    data_path = Path('./Targets/')
    data = 'Constellations.csv'
    my_cols = ['Name', 'Symbol', 'RA', 'DEC', 'Flag']
    target_table = pd.read_csv(data_path / data, comment='#',
                               names=my_cols)
    target_list = []

    for index, value in enumerate(target_table['Name']):
        target_RA = target_table['RA'][index]*u.hourangle
        target_DEC = target_table['DEC'][index]*u.deg
        target_name = value
        my_target = FixedTarget(coord=SkyCoord(
                                ra=target_RA,
                                dec=target_DEC),
                                name=value)
        target_list.append(my_target)
    return target_list
    # Could query from a database instead
