#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 20:56:59 2023

@author: ashar
"""

import zipfile
import os
import xarray as xr
import numpy as np
import sys
import glob

# Specify the path to the zip file
storm_path = glob.glob(sys.argv[1])
storm_yr = np.array([])
storms = int(sys.argv[2])
for storm in storm_path:
    storm = xr.open_dataset(storm)
    start_time = int(storm.time[0].dt.year)
    storm_yr = np.append(storm_yr, start_time)

unique, ncounts = np.unique(storm_yr, return_counts=True)
count_storms = dict(zip(unique, ncounts))

print(count_storms)

        