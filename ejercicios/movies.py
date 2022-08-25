'''
De una lista dada de duraciones de películas, seleccionar una combinación de 2 películas que duren 60 minutos.
Si existen más de dos combinaciones, mostrar la combinación de mayor duración
'''

from xml.etree.ElementTree import tostring


def choose_movies(movies, goal_duration):
    index_movie = 0
    longest_movie = 0
    selected_movies = []
    for movie in movies:
        next_movies = movies[index_movie:]
        second_index_movie = 0
        for next_movie in next_movies:
            if movie + next_movie == goal_duration:
                index1 = index_movie
                index2 = second_index_movie + index_movie
                #print(f'{index1}({movie}), {index2}({next_movie})')
                if (movie > longest_movie) or (next_movie > longest_movie):
                    longest_movie = max(movie, next_movie)
                    selected_movies = [index1, index2]
            second_index_movie += 1
        index_movie += 1
    #print(longest_movie)
    return selected_movies


flight_duration = 90
margin = 30
goal_duration = flight_duration - margin
movies_duration = [1,10,25,35,19,60,30,41,30,40,20,33,27]
print(choose_movies(movies_duration, goal_duration))

