movies_watched = []

while True:
    movie = input("Enter movie: ")
    rating = float(input("What would you rate this movie: "))
    movies_watched.append({"Movie": movie, "Rating": rating})

    another = input("Add another movie? Y/N ")
    if another.upper() == "N":
        print(movies_watched)
        break