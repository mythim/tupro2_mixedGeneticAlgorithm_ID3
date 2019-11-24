#ludfi_azimada
#1301154192

import numpy as np
import random
#from np import vstack

suhu = []
waktu = []
kondisilangit = []
kelembapan = []
status = []
total_populasi = 10

#buka data latih
with open('DataLatih.txt', 'r') as data_latih :
    list = [line.strip().split(',') for line in data_latih.readlines()]
suhu = [line[0] for line in list]
waktu = [line[1] for line in list]
kondisilangit = [line[2] for line in list]
kelembapan = [line[3] for line in list]
status = [line[4] for line in list]

print(suhu)
print(waktu)
print(kondisilangit)
print(kelembapan)
print(status)

#konvert dari string menjadi biner untuk membuat gene
bin_suhu =[]
for i in range (0, len(suhu)):
    if (suhu[i] ==  'Normal' ):
        bin_suhu.append(1)
    elif (suhu[i] == ' Rendah'):
        bin_suhu.append(0)
    else:
        bin_suhu.append(0)

bin_waktu =[]
for i in range (0, len(waktu)):
    if (waktu[i] ==  'Siang' ):
        bin_waktu.append(1)
    elif (waktu[i] == ' Pagi'):
        bin_waktu.append(0)
    elif (waktu[i]) == 'Sore':
        bin_waktu.append(0)
    else :
        bin_waktu.append(0)

bin_kondisilangit =[]
for i in range (0, len(kondisilangit)):
    if (kondisilangit[i] ==  'Cerah' ):
        bin_kondisilangit.append(1)
    elif (kondisilangit[i] == ' Berawan'):
        bin_kondisilangit.append(0)
    elif (kondisilangit[i] == 'Rintik'):
        bin_kondisilangit.append(0)
    else :
        bin_kondisilangit.append(0)

bin_kelembapan =[]
for i in range (0, len(kelembapan)):
    if (kelembapan[i] ==  'Normal' ):
        bin_kelembapan.append(1)
    elif (kelembapan[i] == ' Rendah'):
        bin_kelembapan.append(1)
    else:
        bin_kelembapan.append(0)

bin_kelas =[]
for i in range (0, len(status)):
    if (status[i] ==  'Ya' ):
        bin_kelas.append(1)
    else :
        bin_kelas.append(0)

print(bin_suhu)
print(bin_kondisilangit)
print(bin_waktu)
print(bin_kelembapan)
print(bin_kelas)

lengs = 0
def cek_lenList(bin_suhu, bin_kondisilangit, bin_waktu, bin_kelembapan, bin_kelas) :
    """

    :type bin_suhu: object
    """

    if len(bin_suhu) <= len(bin_kondisilangit) and len(bin_suhu) <= len(bin_kelembapan) and len(bin_suhu) <= len(bin_waktu) and len(bin_suhu) <= len(bin_kelas) :
        lengs = len(bin_suhu)
    return lengs
print(cek_lenList(bin_suhu,bin_kondisilangit,bin_waktu,bin_kelembapan,bin_kelas))

#membuat kromosom dari gen yang telah dibuat
def make_kromosom(bin_suhu, bin_kondisilangit, bin_waktu, bin_kelembapan, bin_kelas, lengs) :
    kromosom = []
    for i in range (0,lengs) :
        kromosom.append([bin_suhu[i] , bin_kondisilangit[i] , bin_waktu[i] , bin_kelembapan[i] , bin_kelas[i]])
    return kromosom

print(make_kromosom(bin_suhu, bin_kondisilangit, bin_waktu, bin_kelembapan, bin_kelas, cek_lenList(bin_suhu,bin_kondisilangit,bin_waktu,bin_kelembapan,bin_kelas)))

krom = make_kromosom(bin_suhu, bin_kondisilangit, bin_waktu, bin_kelembapan, bin_kelas, cek_lenList(bin_suhu,bin_kondisilangit,bin_waktu,bin_kelembapan,bin_kelas))

def make_individu(kromosom) : # menggunakan nilai fungsi fitness maximum f=1/h
    individu = []
    tofit = 0
    cupro = 0

    # print(len(kromosom))
    for j in range(0, len(kromosom)):
        y = 0
        y = bin_suhu[j] ** 0 + bin_kondisilangit[j] ** 1 + bin_waktu[j] ** 2 + bin_kelembapan[j] ** 3 + bin_kelas[
            j] ** 4
        fit = 1 / (y + 1)  # menghitung fitness
        tofit = tofit + fit

    for i in range (0, len(kromosom)) :
        x = 0
        fitness = 0
        probalilitas = 0
        x = bin_suhu[i]**0 + bin_kondisilangit[i]**1 + bin_waktu[i]**2 + bin_kelembapan[i]**3 + bin_kelas[i]**4
        fitness = 1/(x+1)  #menghitung fitness dari setiap individu
        # print(tofit)
        probalilitas = fitness/tofit  # menghitung probablitias dari setiap individu
        cupro = cupro + probalilitas  #menghitung cumulative probabilitas
        # print(total_prob)
        individu.append([kromosom[i], fitness, probalilitas, cupro])
    # print(tofit)
    # print(probalilitas)
    return individu

print(make_individu(krom))

ind = make_individu(krom)

def seleksi(individu,total_populasi) :
    temp = []
    populasi = []
    r = []
    for j in range(total_populasi) :
        r.append(random.uniform(0, 0.05))
    print(r)
    for i in range(total_populasi) :
        # r = random.uniform(0,0.05)
        #print(r)
        m=0
        while (m <len(individu)):
            if (individu[1][3] > r[i]) :
                # temp.append(individu[1])
                temp.append(individu[i])
                m=len(individu)
            elif (individu[m-1][3] < r[i] < individu[m][3]) :
            #else :
                # temp.append(individu[m])
                temp.append(individu[i])
                m=len(individu)
            # else : # untuk memenuhi jika total_populasi kurang dari
            #     temp.append(individu[i])
            #     m = total_populasi
            m = m+1

    # for i in range(0,5) :
    #     populasi.append([temp[i][1], temp[i+2][i]])

    return populasi

aa = seleksi(ind, total_populasi)
print(aa)
print(len(aa))

# def crossover(individu, temp) :
#     k =0
#     rr = []
#
#     while (k < total_total_populasi) :
#         rr.append(random.uniform(0, 1))

def crossover(orangtua_1, orangtua_2):
    global gen_length

    cut = random.randint(0, gen_length-2)

    anak_orangtua_1 = []
    anak_orangtua_2 = []
    for i in range(0, cut+1):
        anak_orangtua_1.append(orangtua_1[i])
        anak_orangtua_2.append(orangtua_2[i])
    for i in range(cut+1, gen_length):
        anak_orangtua_1.append(orangtua_2[i])
        anak_orangtua_2.append(orangtua_1[i])
    return anak_orangtua_1, anak_orangtua_2

# melakukan mutasi untuk pembuatan anak yang dihasilkan dari gen orang tua
def mutasi(individu):
    global gen_length
    pm = 1/gen_length
    for i in range(0, len(individu)):
        prob = random.random()
        if (prob<pm):
            if (individu[i]==1):
                individu[i]=0
            elif (individu[i]==0):
                individu[i]=1
    return individu
while (j < len(pop) - 1):
    rand_value = random.random()
    k = 0
    while (rand_value > list_prob[k]):
        k += 1
    orangtua_1 = populasi[k - 1]
    rand_value = random.random()
    k = 0
    while (rand_value > list_prob[k]):
        k += 1
    orangtua_2 = populasi[k - 1]
    anak_orangtua1, anak_orangtua2 = crossover(orangtua_1[0], orangtua_2[0])
    anak_orangtua1 = mutasi(anak_orangtua1)
    anak_orangtua2 = mutasi(anak_orangtua2)

    x1, x2 = value_Individu(anak_orangtua1)


