#!/usr/bin/env python3


import argparse
from string import capwords
import requests
import json
import pyperclip


def parse_args():
	parser = argparse.ArgumentParser(description="This script gets the lyrics for a specified song.")
	parser.add_argument("artist", help="Specify the artist's name")
	parser.add_argument("song", help="Specify the name of the song")
	return parser.parse_args()


def get_lyrics(artist, title):
	artist = capwords(artist)
	title = capwords(title).replace(" ", "%20")
	r = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
	return r.text


def main():
	args = parse_args()
	# artist = input("Enter artist name: ")
	# title = input("Enter song title: ")
	song = get_lyrics(args.artist, args.song)
	lyrics = json.loads(song)['lyrics']
	# print(lyrics)
	pyperclip.copy(lyrics)
	print(f'The lyrics to "{args.song}" by "{args.artist}" have been copied to your clipboard.')
	exit()


if __name__ == "__main__":
    main()
