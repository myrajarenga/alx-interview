#!/usr/bin/node
// Import the 'request' module
const request = require('request');

// Define a function to fetch and print characters from a movie
function getMovieCharacters (movieId) {
  // Construct the URL for the movie's API endpoint using the provided movieId
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  // Make an HTTP GET request to the movie URL
  request(movieUrl, (movieError, movieResponse, movieBody) => {
    // Handle errors and responses from the movie request
    if (movieError || movieResponse.statusCode !== 200) {
      console.error(`Error fetching movie data: ${movieError || movieResponse.statusCode}`);
      return;
    }

    // Parse the JSON response body into a JavaScript object
    const movieData = JSON.parse(movieBody);
    // Extract the list of characters from the movie data
    const characters = movieData.characters;

    // Loop through each character's URL
    characters.forEach(characterUrl => {
      // Make an HTTP GET request to the character's URL
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        // Handle errors and responses from the character request
        if (characterError || characterResponse.statusCode !== 200) {
          console.error(`Error fetching character data: ${characterError || characterResponse.statusCode}`);
          return;
        }

        // Parse the JSON response body for the character
        const characterData = JSON.parse(characterBody);
        // Extract the character's name
        const characterName = characterData.name;
        // Print the character's name
        console.log(characterName);
      });
    });
  });
}

// Get command-line arguments (excluding 'node' and script filename)
const args = process.argv.slice(2);

// Check if the correct number of arguments is provided
if (args.length !== 1) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

// Extract the movie ID from the command-line argument
const movieId = args[0];
// Call the function to fetch and print characters for the given movie ID
getMovieCharacters(movieId);
