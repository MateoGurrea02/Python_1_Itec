from json import dumps, loads
import os

pelis = [
    {
        "Title": "Arrival",
        "Year": "2016",
        "Rated": "PG-13",
        "Released": "11 Nov 2016",
        "Runtime": "116 min",
        "Genre": "Drama, Mystery, Sci-Fi, Thriller",
        "Director": "Denis Villeneuve",
        "Writer": "Eric Heisserer (screenplay by), Ted Chiang (based on the story \"Story of Your Life\" written by)",
        "Actors": "Amy Adams, Jeremy Renner, Forest Whitaker, Michael Stuhlbarg",
        "Plot": "A linguist works with the military to communicate with alien lifeforms after twelve mysterious spacecraft appear around the world.",
        "Language": "English, Russian, Mandarin",
        "Country": "USA, Canada",
        "Awards": "Won 1 Oscar. Another 67 wins & 263 nominations.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SX300.jpg",
        "Ratings": [
            {
                "Source": "Internet Movie Database",
                "Value": "7.9/10"
            },
            {
                "Source": "Rotten Tomatoes",
                "Value": "94%"
            },
            {
                "Source": "Metacritic",
                "Value": "81/100"
            }
        ],
        "Metascore": "81",
        "imdbRating": "7.9",
        "imdbVotes": "575,270",
        "imdbID": "tt2543164",
        "Type": "movie",
        "DVD": "14 Feb 2017",
        "BoxOffice": "$100,501,349",
        "Production": "21 Laps Entertainment",
        "Website": "N/A",
        "Response": "True"
    },
    {
        "Title": "Transcendence",
        "Year": "2014",
        "Rated": "PG-13",
        "Released": "18 Apr 2014",
        "Runtime": "119 min",
        "Genre": "Action, Drama, Sci-Fi, Thriller",
        "Director": "Wally Pfister",
        "Writer": "Jack Paglen",
        "Actors": "Johnny Depp, Rebecca Hall, Paul Bettany, Cillian Murphy",
        "Plot": "A scientist's drive for artificial intelligence, takes on dangerous implications when his consciousness is uploaded into one such program.",
        "Language": "English",
        "Country": "UK, China, USA",
        "Awards": "3 wins & 5 nominations.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTc1MjQ3ODAyOV5BMl5BanBnXkFtZTgwNjI1NDQ0MTE@._V1_SX300.jpg",
        "Ratings": [
            {
                "Source": "Internet Movie Database",
                "Value": "6.3/10"
            },
            {
                "Source": "Rotten Tomatoes",
                "Value": "19%"
            },
            {
                "Source": "Metacritic",
                "Value": "42/100"
            }
        ],
        "Metascore": "42",
        "imdbRating": "6.3",
        "imdbVotes": "212,957",
        "imdbID": "tt2209764",
        "Type": "movie",
        "DVD": "22 Jul 2014",
        "BoxOffice": "$23,014,504",
        "Production": "Warner Bros. Pictures",
        "Website": "N/A",
        "Response": "True"
    },
    {
        "Title": "Serenity",
        "Year": "2005",
        "Rated": "PG-13",
        "Released": "30 Sep 2005",
        "Runtime": "119 min",
        "Genre": "Action, Adventure, Sci-Fi, Thriller",
        "Director": "Joss Whedon",
        "Writer": "Joss Whedon",
        "Actors": "Nathan Fillion, Gina Torres, Alan Tudyk, Morena Baccarin",
        "Plot": "The crew of the ship Serenity try to evade an assassin sent to recapture one of their members who is telepathic.",
        "Language": "English, Mandarin",
        "Country": "USA",
        "Awards": "9 wins & 9 nominations.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BOWE2MDAwZjEtODEyOS00ZjYyLTgzNDUtYmNiY2VmNWRiMTQxXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SX300.jpg",
        "Ratings": [
            {
                "Source": "Internet Movie Database",
                "Value": "7.8/10"
            },
            {
                "Source": "Rotten Tomatoes",
                "Value": "82%"
            },
            {
                "Source": "Metacritic",
                "Value": "74/100"
            }
        ],
        "Metascore": "74",
        "imdbRating": "7.8",
        "imdbVotes": "279,329",
        "imdbID": "tt0379786",
        "Type": "movie",
        "DVD": "20 Dec 2005",
        "BoxOffice": "$25,335,935",
        "Production": "Universal Pictures",
        "Website": "N/A",
        "Response": "True"
    }
]

strJson = dumps(pelis)
pelisDict = loads(strJson)

createCsv = open("pelis.csv", "w", encoding="utf-8")
createCsv.write("Nombre,Actor,Rating,Recaudacion\n")
 
for i in range(len(pelisDict)):
  nombre = pelisDict[i]['Title']
  actor = pelisDict[i]['Actors'].split(',')[0]
  rating = pelisDict[i]['Ratings'][1]["Value"].replace('%','')
  recaudacion = int(pelisDict[i]['BoxOffice'].replace('$','').replace(',',''))
  createCsv.write(f"{nombre},{actor},{rating},{recaudacion}\n")
createCsv.close()

a = open("pelis.csv", "r", encoding="utf-8")
listaPelisCsv = a.readlines()    

def ratingPromedio():
    print("\nRating promedio de las peliculas\n")
    totalizador = 0 
    for i in range(1,len(listaPelisCsv)):
        totalizador = totalizador + int(listaPelisCsv[i].split(",")[2])
    print(f"El promedio de rating de las peliculas es: {totalizador / (len(listaPelisCsv)-1)}\n")
    input("Presione Enter para volver al Men??")

def sumaRecaudaciones():
    print("\nSuma de recaudaciones de las peliculas\n")
    totalizador = 0 
    for i in range(1,len(listaPelisCsv)):
        totalizador = totalizador + int(listaPelisCsv[i].split(",")[3])
    print(f"La suma de las recaudaciones totales de las peliculas es de: ${totalizador}\n")
    input("Presione Enter para volver al Men??")

a.close()

def borrar():
    pass

def menu():
    op = ""
    while op != "0":
        os.system("cls")
        print("Men?? de Opciones\n")
        print("1) Rating promedio de las peliculas")
        print("2) Suma de recaudaciones de las peliculas")
        print("0) Salir")
        op = input("Ingrese una opci??n: ")
        match op:
            case "1": ratingPromedio()
            case "2": sumaRecaudaciones()
            case "3": borrar()

menu()
