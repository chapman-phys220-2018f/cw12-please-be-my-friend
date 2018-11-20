#! /usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Morgan Holve
# Student ID: 2281337
# Email: holve100@mail.chapman.edu
# Course: MATH 220 Fall 2018
# Assignment: CW 12
###

import math
import sombrero as so

def test_sombrero_start():
    """
    Checks if the second and last values are right.
    """
    xbegin = -0.899999995500383
    ybegin = 8.99884295089148e-06
    test = so.stingray(0.18, -0.9, 0, 50)
    assert math.isclose(test[0][1], xbegin)
    assert math.isclose(test[1][1], ybegin)
    
def test_sombrero_end():
    xend = -0.8161161019919646
    yend = 0.03854402992812615
    test = so.stingray(0.18, -0.9, 0, 50)
    assert math.isclose(test[0][-1], xend)
    assert math.isclose(test[1][-1], yend)