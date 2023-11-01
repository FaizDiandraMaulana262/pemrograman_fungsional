from functools import reduce

movies = [
    {"title": "Avenger: End Game", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Scri-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quite Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Action"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"}
]

def getFilm(movies):
    filmList = list(map(lambda film: f"Title : {film['title']}\nYear : {film['year']}\nRating : {film['rating']}\nGenre : {film['genre']}\n", movies))
    for x, y in enumerate(filmList):
        print(f"=== Film {x+1} ===")
        print(y)

def getFilmWithGenre(movies, genre):
    filmGenre = list(filter(lambda x: x['genre'] == genre, movies))
    return(len(filmGenre))

def getFilmAvg(movies, year): 
    filmRating = list(filter(lambda rating: rating['year'] == year, movies))
    ratingList = list(map(lambda film: film['rating'], filmRating))
    ratingSum = reduce(lambda x, y: x + y, ratingList)
    filmAvg = ratingSum / len(filmRating)
    return(filmAvg)

def getBestFilm(movies):
    bestFilm = max(movies, key=lambda film: film['rating'])
    print(f"Title : {bestFilm['title']}\nYear : {bestFilm['year']}\nRating : {bestFilm['rating']}\nGenre : {bestFilm['genre']}")
        
def main():
    global movies
    print("=== Menu ===\n1. Get Film\n2. Get Film With Genre\n3. Get Film Rating Average\n4. Get Best Film")

    userInput = int(input("Masukan Menu : "))
    
    match userInput:
        case 1:
            getFilm(movies)
        case 2:
            inputGenre = str(input("Masukan Genre : "))
            print(getFilmWithGenre(movies, inputGenre))
        case 3:
            inputYear = int(input("Masukan Tahun : "))
            print(getFilmAvg(movies, inputYear))
        case 4:
            getBestFilm(movies)

if __name__ == "__main__":
    main()