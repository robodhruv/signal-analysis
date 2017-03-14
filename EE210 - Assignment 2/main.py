from music_synth import *

def generate_independent():
	songfile = "Songs/song_a.txt"
	strip_file(songfile)
	song = get_notes(songfile)
	print song