import wave
import numpy as np
import matplotlib.pyplot as plt

def get_values(nom_arxiu, llindar): # Return a value for each sample of the audio file (average of both channels)
	file = wave.open(nom_arxiu)

	data = file.readframes(-1) # Read all the frames in the array data

	data = np.frombuffer(data, np.int16) # Turn the bytes into ints

	data.shape = -1,2
	data = data.T # Separate the 2 channels into 2 arrays inside of the data array (data[0] is channel 1 and data[1] is channel 2)

	valors = []
	for i in range(len(data[0])): # List "valors" is the average of the two chanels
		valors.append((data[0][i]+data[1][i])/2)

	file.close()

	return valors

def show_graf(nom_arxiu):
	file = wave.open(nom_arxiu)

	framerate = file.getframerate()
	frames = file.getnframes()

	duracio = 1/float(framerate) # Seconds each sample takes
	temps_seq = np.arange(0, frames/float(framerate), duracio) # Array of the time for each sample (to plot it)
	
	data = file.readframes(-1) # Read all the frames in the array data

	data = np.frombuffer(data, np.int16) # Turn the bytes into ints

	data.shape = -1,2
	data = data.T # Separate the 2 channels into 2 arrays inside of the data array (data[0] is channel 1 and data[1] is channel 2)

	valors = []
	for i in range(len(data[0])): # List "valors" is the average of the two chanels
		valors.append((data[0][i]+data[1][i])/2)

	file.close()

	plt.plot(temps_seq, valors) # Plotting the vales over time (average between channel 1 and channel 2)
	plt.show()


def get_duration_vector(nom_arxiu, llindar): # Perque funcioni be s'ha d'ajustar el count i el valor llindar
	valors = get_values(nom_arxiu, llindar)

	file = wave.open(nom_arxiu)

	framerate = file.getframerate()
	frames = file.getnframes()

	duracio = 1/float(framerate) # Seconds each sample takes
	temps_seq = np.arange(0, frames/float(framerate), duracio) # Array of the time for each sample (to plot it)


	duracio_estats = [] # This list will have as its first element the number of microseconds that the first 0 lasted for, following that it will have the microseconds that the following 1 lasted for, then the microseconds that the following 0 lasted and so on

	count = 30
	count_inicial = count
	last_change = 0
	estat = 0
	for i in range(len(valors)): # This loop computes how long the 0s and 1s last
		if (valors[i] > llindar or valors[i] < -llindar) and estat == 0:
			duracio_estats.append(i-last_change)
			last_change = i
			estat = 1

		elif (estat == 1):
			if (count == 0):
				duracio_estats.append(i-count_inicial-last_change)
				last_change = i-count_inicial
				estat = 0
				count = count_inicial
			else:
				if (valors[i] > llindar or valors[i] < -llindar):
					count = count_inicial
				else:
					count -= 1

	for i in range(len(duracio_estats)):
		duracio_estats[i] = float((duracio_estats[i]*duracio)*1000000)

	for i in range(len(duracio_estats)):
		duracio_estats[i] = int(duracio_estats[i])

	file.close()

	return duracio_estats

