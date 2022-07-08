import librosa
import time
from menu import filename

start_time = time.time()

#Название файла с песней
song_name = filename
#Чем ниже коэффициент k, тем строже отбор нот
k = 0.77
#Минимальная частота смены нот (в миллисекундах)
too_fast = 200

print("Song analysis started!")
x, sr = librosa.load(song_name)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))

#Массив с моментами времени, каждый элемент равен 23*i миллисекунд
times = librosa.times_like(Xdb)

#В массиве Xdb меняются местами столбцы и строки, новый массив называется spectro
spectro = []
for i in range(len(Xdb[0])):
    spectro.append([])
for i in range(len(spectro)):
    for j in Xdb:
        spectro[i].append(j[i])

#Каждый элемент массива spectro - среднее арифметическое своих элементов со знаком +
for i in range(len(spectro)):
    spectro[i] = abs(sum(spectro[i]) / len(spectro[i]))

#Нота появляется, если значение спектра в данный момент ниже среднего * k
timearr = []
c = 0
for i in range(len(spectro)):
    fragment = c // 100
    #Среднее значение вычисляется каждые 2,3 секунды
    mean = sum(spectro[fragment:fragment+1:]) / len(spectro[fragment:fragment+1:])
    #print(mean)
    if spectro[i] < mean * k:
        timearr.append(int(times[i]*1000))
    c += 1

#Самые резкие появления нот убираются с учётом минимальной частоты смены нот
for i in range(len(timearr)-1):
    if timearr[i+1] - timearr[i] < too_fast:
        timearr[i+1] = timearr[i]

#print(timearr)

print("Song analysis time: ", time.time() - start_time, " seconds")
print("Song analysis time per 1 second: ", (time.time() - start_time) / (len(times) * 0.023), " seconds")
