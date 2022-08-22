movies_I_watched = ["KGF", "Avengers", "Harry Potter", "Narnia", "Spyder", "Avatar"]
no_of_movies = int(input("How many movies did you watched recently? : "))
movies_friend_watched = []
movies_I_only_watched = []
movies_friend_only_watched = []
movies_both_watched = []

for movie in range(no_of_movies):
    watched = input("Tell the name of the movie? : ")
    movies_friend_watched.append(watched)

for his_movie in range(len(movies_friend_watched)):
    both_watched = False
    for my_movie in range(0, len(movies_I_watched)):
        if(movies_friend_watched[his_movie] == movies_I_watched[my_movie]):
            movies_both_watched.append(movies_friend_watched[his_movie])
            both_watched = True
    if(both_watched == False):
        movies_friend_only_watched.append(movies_friend_watched[his_movie])


for movie in range(len(movies_I_watched)):
    if movies_I_watched[movie] not in movies_friend_watched:
        movies_I_only_watched.append(movies_I_watched[movie])

print("Movies my friend and I watched\n", movies_both_watched)
print("Movies I only watched\n", movies_I_only_watched)
print("Movies my friend only watched\n", movies_friend_only_watched)



#test case 1
# How many movies did you watched recently? : 5
# Tell the name of the movie? : ET
# Tell the name of the movie? : KGF
# Tell the name of the movie? : Avengers
# Tell the name of the movie? : Narnia
# Tell the name of the movie? : Spyder
# Movies my friend and I watched
#  ['KGF', 'Avengers', 'Narnia', 'Spyder']
# Movies I only watched
#  ['Harry Potter', 'Avatar']
# Movies my friend only watched
#  ['ET']

# test case 2
# How many movies did you watched recently? : 1
# Tell the name of the movie? : Maleficient
# Movies my friend and I watched
#  []
# Movies I only watched
#  ['KGF', 'Avengers', 'Harry Potter', 'Narnia', 'Spyder', 'Avatar']
# Movies my friend only watched
#  ['Maleficient']