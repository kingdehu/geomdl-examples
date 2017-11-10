# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
from geomdl import BSpline

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set evaluation delta
surf.delta = 0.01

# Set up surface
surf.read_ctrlpts_from_txt("ex_surface01.cpt")
surf.degree_u = 3
surf.degree_v = 3
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Evaluate surface points
surf.evaluate()

# Save control points and evaluated curve points
surf.save_surfpts_to_csv("surfpts01_orig.csv", mode='zigzag')
surf.save_ctrlpts_to_csv("ctrlpts01_orig.csv", mode='mesh')

# Good to have something here to put a breakpoint
pass
