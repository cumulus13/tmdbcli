#!c:/SDK/Anaconda2/python.exe
import sys
from tmdbv3api import TMDb, Movie
from make_colors import make_colors


tmdb = TMDb()
tmdb.api_key = "e86ee300ee55e5bc16eb110e97635cd6"

tmdb.language = 'en'
if 'debug' in sys.argv[1:]:
	tmdb.debug = True

movie = Movie()

search = movie.search(sys.argv[1])
if not search or len(search) == 0:
	print(make_colors("No Movie Found !", 'lw', 'lr', ['blink']))
	sys.exit()
n = 1
for res in search:
	number = str(n)
	if len(str(n)) == 1:
		number = "0" + str(n)
	print(make_colors(number, 'lc') + ". " + make_colors(str(res.title), 'lw', 'b') + " " + make_colors("[" + str(res.id) + "]", 'b', 'lg') + " " + make_colors("[" + str(res.vote_average) + "]", 'b','ly'))
	n += 1

if search:
	print("__all__ =", dir(search[0]))
	
q = raw_input(make_colors("Select Number: ", 'lw', 'lm'))
if q and str(q).isdigit() and int(str(q)) <= len(search):
	print(make_colors(search[int(str(q).strip()) - 1].overview), 'lc')
	