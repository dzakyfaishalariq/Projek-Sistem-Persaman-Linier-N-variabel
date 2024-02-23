import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt

class splnv_metod:
    nama="Sistem Persamaan Linier"
    def __init__(self, matrix, c):
        self.matrix = matrix
        self.c = c
    def boot_system_persamaan(self):
        return np.dot(np.linalg.inv(self.matrix), self.c)

