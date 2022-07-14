# 1) Nombres de las películas según un género solicitado.
# 2) La cantidad de películas estrenadas antes de un año solicitado.
# 3) Nombres, años de estreno y géneros de las películas cuyo nombre comienza con una letra pedida al usuario.

movies = [
"Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genders = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

def position(movie):
  namePosition = movie.find("(")
  genrePosition = movie.find(")") + 1
  return namePosition, genrePosition

def nameByGenre(gen):
  nameMovies = []
  for movie in movies:
    namePosition,genrePosition = position(movie)
    name = movie[:namePosition] 
    genre = movie[genrePosition:]
    if gen == genre:
      nameMovies.append(name)
  print(nameMovies)   


nameByGenre('act')

def premiersBeforeAYears(yearChoice):
  counter = 0
  for movie in movies:
    namePosition,genrePosition = position(movie)
    year = movie[namePosition+1:genrePosition-1]
    if int(year) < yearChoice:
      counter += 1
  print(counter)
    
premiersBeforeAYears(1999)

def movieByALetter(letter):
  for movie in movies:
    namePosition,genrePosition = position(movie)
    name = movie[:namePosition]
    genre = movie[genrePosition:]
    year = movie[namePosition + 1:genrePosition - 1]
    if name[0] == letter.capitalize():
      print(f"Nombre: {name}, Año: {year}, Genero: {genders[genre]}")

movieByALetter("D")


