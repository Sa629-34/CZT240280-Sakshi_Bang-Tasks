from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(_name_)

movies = [
    {"Id": 1, "Title": "Harry Potter and the Sorcerer's Stone", "Director": "Chris Columbus", "Year": 2001, "IMDb": "7.7/10", "Rotten Tomatoes": "80%", "Metacritic": "65/100"},
    {"Id": 2, "Title": "Harry Potter and the Philosopher's Stone", "Director": "Chris Columbus", "Year": 2003, "IMDb": "7.9/10", "Rotten Tomatoes": "70%", "Metacritic": "60/100"},
    {"Id": 3, "Title": "Harry Potter and the Chamber of Secrets", "Director": "Chris Columbus", "Year": 2007, "IMDb": "8.4/10", "Rotten Tomatoes": "90%", "Metacritic": "80/100"}
]

@app.route('/')
def list_movies():
    return render_template('list_movies.html', movies=movies)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        data = request.form
        new_movie = {
            "Id": movies[-1]["Id"] + 1 if movies else 1,
            "Title": data.get("Title"),
            "Director": data.get("Director"),
            "Year": int(data.get("Year")),
            "IMDb": data.get("IMDb"),
            "Rotten Tomatoes": data.get("RottenTomatoes"),
            "Metacritic": data.get("Metacritic")
        }
        movies.append(new_movie)
        return redirect(url_for('list_movies'))
    return render_template('add_movie.html')

@app.route('/update/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(movie_id):
    movie = None
    for m in movies:
        if m["Id"] == movie_id:
            movie = m
            break
    if not movie:
        return "Movie not found", 404

    if request.method == 'POST':
        data = request.form
        movie.update({
            "Title": data.get("Title", movie["Title"]),
            "Director": data.get("Director", movie["Director"]),
            "Year": int(data.get("Year", movie["Year"])),
            "IMDb": data.get("IMDb", movie["IMDb"]),
            "Rotten Tomatoes": data.get("RottenTomatoes", movie["Rotten Tomatoes"]),
            "Metacritic": data.get("Metacritic", movie["Metacritic"])
        })
        return redirect(url_for('list_movies'))
    return render_template('update_movie.html', movie=movie)

@app.route('/delete/<int:movie_id>', methods=['GET', 'POST'])
def delete_movie(movie_id):
    global movies
    movies = [movie for movie in movies if movie["Id"] != movie_id]
    return redirect(url_for('list_movies'))

if __name__ == '_main_':
    app.run(debug=True)