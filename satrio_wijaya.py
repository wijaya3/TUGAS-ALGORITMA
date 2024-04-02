class AhliWaris:
    def __init__(self, nama, hubungan, bagian):
        self.nama = nama
        self.hubungan = hubungan
        self.bagian = bagian

class Warisan:
    def __init__(self, total_nilai):
        self.total_nilai = total_nilai
        self.ahli_waris = []

    def tambah_ahli_waris(self, ahli_waris):
        self.ahli_waris.append(ahli_waris)

    def hitung_pembagian(self):
        total_bagian = sum(ahli.bagian for ahli in self.ahli_waris)
        if total_bagian != 100:
            raise ValueError("Total bagian harus sama dengan 100%")
        
        for ahli in self.ahli_waris:
            bagian_diterima = (ahli.bagian / 100) * self.total_nilai
            print(f"{ahli.nama} menerima warisan sebesar ${bagian_diterima:.2f}")

# Fungsi untuk menjalankan program
def main():
    warisan = Warisan(10000000000)  # Total nilai warisan
    # Menambahkan ahli waris
    warisan.tambah_ahli_waris(AhliWaris("Susi", "Ibu", 40))
    warisan.tambah_ahli_waris(AhliWaris("santi", "Anak", 30))
    warisan.tambah_ahli_waris(AhliWaris("sasa", "Anak", 30))
    
    # Menghitung pembagian warisan
    warisan.hitung_pembagian()

if __name__ == "__main__":
    main()
