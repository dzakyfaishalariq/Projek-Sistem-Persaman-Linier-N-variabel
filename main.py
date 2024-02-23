from metod.splnv import splnv_metod as sm

f = sm([[1,2],[2,3]],[2,3])
if __name__ == "__main__":
    print("hasil perkalian:")
    print(f.boot_system_persamaan())
    print(f.nama)