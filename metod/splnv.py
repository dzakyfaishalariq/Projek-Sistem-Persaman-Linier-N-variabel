import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt

class SplnvMetod:
    nama="Sistem Persamaan Linier n variabel"
    def __init__(self, matrix, c):
        self.matrix = matrix
        self.c = c
    def hasil_system_persamaan(self):
        return np.dot(np.linalg.inv(self.matrix), self.c)


class InputanSplnv:
    matrix = []
    variabel = []
    konstan = []
    def __init__(self, jumlah_persamaan, jumlah_variabel):
        self.jumlah_pesamaan = jumlah_persamaan
        self.jumlah_variabel = jumlah_variabel
        self.jumlah_konstan = jumlah_persamaan
    def inputan_sistem_persamaan(self):
        print("Masukan Nilai kofision :")
        for i in range(self.jumlah_pesamaan):
            lis_kofision = []
            for j in range(self.jumlah_variabel):
                lis_kofision.append(int(input("Masukan nilai kofision ke-{} : ".format(i))))
            self.matrix.append(lis_kofision)
        print("Masukan variabelnya :")
        for i in range(self.jumlah_variabel):
            self.variabel.append(str(input("Masukan nilai variabelnya ke-{} :".format(i))))
        print("Masukan Nilai Konstan :")
        for i in range(self.jumlah_konstan):
            self.konstan.append(int(input("Masukan nilai konstan ke-{} :".format(i))))
        return [self.matrix, self.variabel, self.konstan]
