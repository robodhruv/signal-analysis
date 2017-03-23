from helper import *

harmonics = np.array([1., - 1./2,  1. / 3, - 1./4, 1. / 5])  # Spectral Profile
rate = 16  # sampling rate in kHz
ADSR = [0.1, 0, 0.75, 0.15]

def get_envelope(duration):
	global rate
	envelope = np.arange(duration * rate * (ADSR[0]))
	envelope = envelope / np.max(envelope)
	envelope = np.append(envelope, np.ones(ADSR[2] * duration * rate))
	x = np.arange(duration * rate * ADSR[3])
	x = x / np.max(x)
	release = 1 - x
	# envelope = list(envelope)
	envelope = np.append(envelope, release)
	return envelope


def gen_tone(f, duration):
	global rate, harmonics
	t = np.arange(duration * rate)
	x = np.sin(2 * np.pi * f * t / (1000 * rate))
	x = x + harmonics[1] * np.sin(2 * np.pi * 2 * f * t / (1000 * rate))
	x = x + harmonics[2] * np.sin(2 * np.pi * 3 * f * t / (1000 * rate))
	x = x + harmonics[3] * np.sin(2 * np.pi * 4 * f * t / (1000 * rate))
	x = x + harmonics[4] * np.sin(2 * np.pi * 5 * f * t / (1000 * rate))
	return x

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
	song = []
	for i in range(len(notes)):
		tone = gen_tone(float(notes[i][0]), int(notes[i][1]))
		envelope = get_envelope(int(notes[i][1]))
		tune = tone * envelope
		song.extend(list(tune))
	song = np.clip(song, -1.0, 1.0)
	return song


song = generate_song("Songs/song_b.txt")
sd.play(song, rate * 1000)
