from music_synth import *

pluck = np.zeros(10)
harmonics = np.array([1., - 1. / 9, 1. / 25])  # Spectral Profile
adsr = np.array([80, 750, 0, 0])  # Temporal Profile (ms)
rate = 16  # sampling rate in kHz
total = np.sum(adsr)  # total time for which one pluck persists

def generate_independent():
	songfile = "Songs/song_a.txt"
	strip_file(songfile)
	song = get_notes(songfile)
	print song

def gen_impulse():
	global adsr, rate;
	if (adsr[2]!=0 or adsr[3]!= 0):
		print "Please Remove S, R values. Working on that!"
		return
	impulse = np.zeros(total * rate)
	for i in range(total * rate):
		if(i < adsr[0] * rate):
			impulse[i] = (1.0 * i / rate) / adsr[0]
		elif(i < (adsr[0] + adsr[1]) * rate):
			impulse[i] = 1.0 * (adsr[0] + adsr[1] - 1.0 * i / rate) / adsr[1]
		# Add code for sustain and release also
	return impulse

def gen_tone(f):
	t = np.arange(total * rate)
	x = np.sin(2 * np.pi * f * t / (1000 * rate))
	x = x + harmonics[1] * np.sin(2 * np.pi * 3 * f * t / (1000 * rate))
	x = x + harmonics[2] * np.sin(2 * np.pi * 5 * f * t / (1000 * rate))
	return x

def posify(notes_in):
	cumulative = 0
	notes = []
	for i in range(len(notes_in)):
		notes.append([float(notes_in[i][0]), cumulative])
		cumulative = cumulative + int(notes_in[i][1])
	return notes

def generate_song(filename):
	strip_file(filename)
	notes_file = get_notes(filename)
	duration = 0.
	notes = []
	for line in notes_file:
		for note in line:
			if (len(note.split(',')) == 2):
				duration = duration + int(note.split(',')[1])
				notes.append(note.split(','))
	notes = np.array(notes)
	notes.astype(np.float32)
	song = np.zeros(int((duration + total) * rate))
	notes = posify(notes)
	impulse = gen_impulse()
	for i in range(len(notes)):
		tone = gen_tone(notes[i][0])
		tune = tone * impulse
		song[notes[i][1] * rate : (notes[i][1] * rate) + len(tone)] += tune
		# print len(tone)
	song = np.clip(song, -1.0, 1.0)
	return song


song = generate_song("Songs/song_b.txt")
sd.play(song, rate * 1000)