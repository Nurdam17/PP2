movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Task1:
def solve(movies, name_of_movies):
    for x in movies:
            if x["name"] == name_of_movies:
                if x["imdb"] > 5.5:
                     return True
                else:
                     return False
    return False

name_of_movies=input()
print(solve(movies, name_of_movies))

#Task2:
def solve(movies):
    new_list = []
    for x in movies:
        if x["imdb"] > 5.5:
                new_list.append(x["name"])
    print(new_list)

solve(movies)

#Task3:
def solve(movies, category_of_movies):
    new_list = []
    for x in movies:
            if x["category"] == category_of_movies:
                  new_list.append(x["name"])
    print(new_list)

category_of_movies=input()

solve(movies, category_of_movies)

#Task4:
def solve(movies, my_list):
    total = 0
    for x in movies:
         for y in my_list:
              if x["name"]==y:
                   total += x["imdb"]
    print(total/len(my_list))

my_list=["Usual Suspects", "Hitman", "Dark Knight", "The Help", "The Choice", "Colonia", "Love", "Bride Wars", "AlphaJet",
         "Ringing Crime", "Joking muck", "What is the name", "Detective", "Exam", "We Two"]

solve(movies, my_list)

#Task5:
def solve(movies, cat):
    total = 0
    number_of_movies=0
    for x in movies:
        if x["category"]==cat:
            total += x["imdb"]
            number_of_movies += 1
    avg=total/number_of_movies
    print(avg)

cat=input()

solve(movies, cat)