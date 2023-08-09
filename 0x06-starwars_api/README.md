## Technical Interview questio on APIS

# TASk
0. Star Wars Characters
Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module

alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$ 

#Explanaation
Import the request module: This module is used to make HTTP requests to the provided API endpoints.

Define the getMovieCharacters function: This function takes a movie ID as an argument and is responsible for fetching and printing the characters from that movie.

Construct the movie URL: Using the provided movie ID, the script constructs the URL for the movie's API endpoint.

Make a GET request for the movie data: The script uses the request module to send an HTTP GET request to the movie URL. It provides a callback function that will be executed when the request completes.

Handle movie request errors and responses: If there is an error or the response status code is not 200 (OK), the script logs an error message and returns from the function.

Parse movie data: If the request is successful, the script parses the JSON response body into a JavaScript object.

Extract character URLs: The script extracts the list of character URLs from the movie data.

Loop through character URLs: For each character URL, the script sends an HTTP GET request using the request module.

Handle character request errors and responses: Similar to the movie request, the script handles errors and responses from the character requests.

Parse character data: If the character request is successful, the script parses the JSON response body for the character data.

Extract character name: The script extracts the character's name from the character data.

Print character name: The script prints the character's name to the console.

Get command-line arguments: The script extracts the command-line arguments, excluding 'node' and the script filename.

Check argument count: The script checks if the correct number of arguments (one movie ID) is provided. If not, it displays a usage message and exits.

Extract movie ID: The script extracts the movie ID from the command-line argument.

Call the function: The getMovieCharacters function is called with the provided movie ID to start fetching and printing character names.
