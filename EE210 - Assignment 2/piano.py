from music_synth import *

harmonics = np.array([1., - 1. / 9, 1. / 25])  # Spectral Profile
rate = 16  # sampling rate in kHz
sustain = 0.75

def get_envelope(duration):
	global rate
	envelope = np.ones(sustain * duration * rate)
	x = np.arange(duration * rate * (1 - sustain))
	x = x / np.max(x)
	release = 1 - x
	# envelope = list(envelope)
	envelope = np.append(envelope, release)
	return envelope


def gen_tone(f, duration):
	global rate
	t = np.arange(duration * rate)
	x = np.sin(2 * np.pi * f * t / (1000 * rate))
	x = x + harmonics[1] * np.sin(2 * np.pi * 3 * f * t / (1000 * rate))
	x = x + harmonics[2] * np.sin(2 * np.pi * 5 * f * t / (1000 * rate))
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
# sd.play(song, rate * 1000)