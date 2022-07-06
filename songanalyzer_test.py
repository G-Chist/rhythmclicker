import librosa

song_name = 'testsong.wav'
toofast = 300

x, sr = librosa.load(song_name)
hop_length = 512
chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
times = librosa.times_like(chromagram)

#Каждый элемент, не равный 1, становится 0
for i in range(len(chromagram)):
    for j in range(len(chromagram[i])):
        chromagram[i][j] = int(chromagram[i][j])

#В массиве chromagram меняются местами столбцы и строки, новый массив называется chromarr
chromarr = []
for i in range(len(chromagram[0])):
    chromarr.append([])
for i in range(len(chromarr)):
    for j in chromagram:
        chromarr[i].append(j[i])

#Заполняется массив с моментами появления нот (timearr)
timearr = []
for i in range(len(times)-1):
    if chromarr[i] != chromarr[i+1]:
        timearr.append(int(times[i]*1000)) #Секунды переводятся в миллисекунды

#Самые резкие появления нот убираются
mean = sum(timearr) / len(timearr)
for i in range(len(timearr)-1):
    if timearr[i+1] - timearr[i] < toofast:
        timearr[i+1] = timearr[i]

#print(timearr)
