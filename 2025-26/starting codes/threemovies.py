movies=[0,1,2]
print("Enter your three Favourite movies")
movies[0]=input("First:")
movies[1]=input("Second:")
movies[2]=input("Third:")
print("Your three favourite movies are:",movies)



#using append function will be a better choice

movies=[]
print("Enter your three Favourite movies")
mov=input("First:")
movies.append(mov)
mov=input("Second:")
movies.append(mov)
mov=input("Third:")
movies.append(mov)
print("Your three favourite movies are:",movies)
