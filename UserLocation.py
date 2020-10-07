#!/usr/bin/env python

import geocoder
from timezonefinder import TimezoneFinder
from astroplan import Observer
import numpy as np
import astropy.units as u
from astropy.time import Time


class Location(object):
    '''
    Class for location of user.
    '''
    def __init__(self, targets):
        current_time = Time.now()    # Current UTC Time
        self.current_time = current_time
        self.targets = targets

    def get_coords(self):
        '''Gets the user's location from geocoder.'''
        g = geocoder.ip('me')
        location = g.latlng
        return location

    def get_tz(self):
        '''Gets the user's timezone from timezone finder based on the user's coordinates.'''
        lat = self.get_coords()[0]
        lon = self.get_coords()[1]
        tf = TimezoneFinder()
        tz = tf.closest_timezone_at(lng=lon, lat=lat, delta_degree=3)
        return tz

    def observer_location(self):
        '''Creates an astroplan observer object with the users coordinates and timezone.'''
        locale = Observer(
                latitude=(self.get_coords()[0]*u.deg).to(u.arcsec),
                longitude=self.get_coords()[1]*u.deg,
                elevation=63.4 * u.m,
                timezone=self.get_tz(),
                name="Observer Location"
                    )
        return locale

    def local_time(self):
        '''Gets the current time at the user's location.'''
        locale = self.observer_location()
        local_now = self.current_time.to_datetime(locale.timezone)
        return local_now

    def whats_visible(self):
        '''Given a list of fixed targets, determines what is visible at an observers location.'''
        up_list = []
        locale = self.observer_location()
        mask = np.where(locale.target_is_up(self.current_time, self.targets))[0]
        for value in mask:
            up_list.append(self.targets[value])
        return up_list
