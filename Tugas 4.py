data=[]
while(True):
    nama=input("Masukkan nama   :  ")
    nim=input("Masukkan nim    :  ")
    Tugas=int(input("Masukkan Nilai Tugas   :  "))
    UTS=int(input("Masukkan Nilai UTS     :  "))
    UAS=int(input("Masukkan Nilai UAS     :  "))
    Akhir= (30 * Tugas / 100) + (35 * UTS / 100) + (35 * UAS / 100)
    data.append([nama, nim, Tugas, UTS, UAS, Akhir])
    ulangi=input("Tambah daya  (y/t)?")
    if ulangi.lower() == 't':
        break;

print("\nDaftar Nama\n")
print("============================================================================")
print("|   Nama   |    NIM   |    Tugas   |     UTS    |    UAS     |    Akhir    |")
print("============================================================================")
for x in data:
    print("| {0:8s} | {1:8s} | {2:10d} | {3:10d} | {4:10d} | {5:10f}  |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
print("============================================================================")