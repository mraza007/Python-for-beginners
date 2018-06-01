#In this file I am going to model a Spotify playlist
playlist ={
	'name':'hip-hop',
	'author':'John',
	'songs' : [
	{
		'title':'Walk it Talk it',
		'artist': 'Migos',
	},
	{
		'title':'New Freezer',
		'artist' : 'Rich Kid',
	},
	{
	'title':'New Freezer',
	'artist':'Chris Brown',
	}
	],
}

for song in playlist['songs']:
	print(song['title'])