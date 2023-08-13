#!/usr/bin/node

// Import the 'request' library
const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Construct the URL for the movie's endpoint
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Function to send requests to retrieve character information
function fetchCharacters(characterList, index) {
  // If all characters are fetched, stop
  if (characterList.length === index) {
    return;
  }

  // Send a request to the API for a character's information
  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error); // Display error message if request fails
    } else {
      const character = JSON.parse(body); // Parse the response body as JSON
      console.log(character.name); // Display the character's name
      fetchCharacters(characterList, index + 1); // Fetch next character
    }
  });
}

// Send a request to the movie's endpoint to get movie details
request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error); // Display error message if request fails
  } else {
    const movieData = JSON.parse(body); // Parse the movie data as JSON
    const characterList = movieData.characters; // Extract the list of characters

    // Start fetching characters using the fetchCharacters function
    fetchCharacters(characterList, 0);
  }
});
