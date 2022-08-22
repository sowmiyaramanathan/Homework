movies_I_watched = ["KGF", "Avengers", "Harry Potter", "Narnia", "Spyder", "Avatar"]    #initializing a list with the movies I have watched
no_of_movies = int(input("How many movies did you watched recently? : "))               #reading the number of movies my friend watched recently
movies_friend_watched = []              #declaring a list for movies which has been watched by my friend
movies_both_watched = []                #declaring a list for movies which has been watched by my friend and I
movies_I_only_watched = []              #declaring a list for movies which has been watched by myself only
movies_friend_only_watched = []         #declaring a list for movies which has been watched by my friend only
    
for movie in range(no_of_movies):       #using for to get the name of the movies my friend has watched
    watched = input("Tell the name of the movie? : ")       #reading the movie name from my friend
    movies_friend_watched.append(watched)                   #adding the movie into its corresponding list

for his_movie in range(len(movies_friend_watched)):         #using for to find the movies that are watched by both of us
    both_watched = False                                    #initialzing a boolean value to keep track of whether the movie is watched by both of us or by my friend only
    for my_movie in range(0, len(movies_I_watched)):        #using for to find the movies that are watched by me
        if(movies_friend_watched[his_movie] == movies_I_watched[my_movie]):     #using if to check whether the the movie watched by my friend is as same as that of the movie I have already watched
            movies_both_watched.append(movies_friend_watched[his_movie])        #adding the movie we both watched into its corresponding list
            both_watched = True             #changing the boolean to know that the current movie has been watched by both of us
    if(both_watched == False):              #using if to check the boolean value which implies whether the current has been watched by both of us or only by my friend
        movies_friend_only_watched.append(movies_friend_watched[his_movie])     #adding the movie watched by my friend only to its corresponding list


for movie in range(len(movies_I_watched)):          #using for to fing the movies that are watched by me only
    if movies_I_watched[movie] not in movies_friend_watched:        #using if to check whether the movie I watched is not the movie my friend has watched
        movies_I_only_watched.append(movies_I_watched[movie])       #adding the current movie to its corresponding list

print("Movies my friend and I watched\n", movies_both_watched)      #printing the movies watched by both of us
print("Movies I only watched\n", movies_I_only_watched)             #printing the movies watched by my only
print("Movies my friend only watched\n", movies_friend_only_watched)#printing the movies watched by my friend only



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