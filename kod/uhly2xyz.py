"""Priama kinematika robota so šiestimi stupňami voľnosti."""
from math import cos, sin

import numpy as np


def uhly2xyz(u1, u2, u3, u4, u5, u6):
    """Vráti polohu efektora [x, y, z] v metroch ako pole s tvarom (3,).

    Šesť skalárnych vstupov predstavuje uhly kĺbov v radiánoch.
    Pracovný interval zadania je od -pi do pi pre každý uhol.
    """
    R1 = 0.188
    R2 = 1.175
    R3 = 1.3
    R4 = 0.2
    R6x = 0.3
    R6z = 0.1

    A = np.array([
        [cos(u1), -sin(u1), 0, 0],
        [sin(u1), cos(u1), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    B = np.array([
        [1, 0, 0, R1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    C = np.array([
        [cos(u2), 0, sin(u2), 0],
        [0, 1, 0, 0],
        [-sin(u2), 0, cos(u2), 0],
        [0, 0, 0, 1],
    ])
    D = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, R2],
        [0, 0, 0, 1],
    ])
    E = np.array([
        [cos(u3), 0, sin(u3), 0],
        [0, 1, 0, 0],
        [-sin(u3), 0, cos(u3), 0],
        [0, 0, 0, 1],
    ])
    F = np.array([
        [1, 0, 0, 0],
        [0, cos(u4), -sin(u4), 0],
        [0, sin(u4), cos(u4), 0],
        [0, 0, 0, 1],
    ])
    G = np.array([
        [1, 0, 0, R3],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    H = np.array([
        [cos(u5), 0, sin(u5), 0],
        [0, 1, 0, 0],
        [-sin(u5), 0, cos(u5), 0],
        [0, 0, 0, 1],
    ])
    I = np.array([
        [1, 0, 0, R4],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    J = np.array([
        [1, 0, 0, 0],
        [0, cos(u6), -sin(u6), 0],
        [0, sin(u6), cos(u6), 0],
        [0, 0, 0, 1],
    ])

    KB = A @ B @ C @ D @ E @ F @ G @ H @ I @ J @ np.array([R6x, 0, -R6z, 1])
    return KB[:3]
