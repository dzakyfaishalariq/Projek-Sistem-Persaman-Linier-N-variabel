from metod.splnv import SplnvMetod as Sm
from metod.splnv import InputanSplnv as Is

if __name__ == "__main__":
    print("Selamat Datan Di Sistem Persamaan Linier N variabel")
    print("===================================================")
    j_persamaan = int(input("Jumlah Persamaan : "))
    j_variabel = int(input("Jumlah Variabel : "))
    inp = Is(j_persamaan, j_variabel)
    inp_h = inp.inputan_sistem_persamaan()
    hasil = Sm(inp_h[0],inp_h[2])
    hasil_h = hasil.hasil_system_persamaan()
    print()
    print("========================")
    print("    Hasil Persamaan     ")
    print("========================")
    for i in range(len(hasil_h)):
        print("Nilai {} : {}".format(inp_h[1][i],hasil_h[i]))