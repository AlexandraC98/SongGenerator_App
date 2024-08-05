# SongGenerator_App

Thanks to Spotify and the course I've been following on Replit (100 DoC), I was able to use a free developer's API for creating an easy app which shows 10 of the most popular songs for a given year.

https://github.com/user-attachments/assets/8dada4b7-ca98-4994-b6c0-72bfbe120c78

## How it works

- Clone this repo to your computer
- Create an account on https://developer.spotify.com/ and, once you are logged in, create an app with a name, description and URI
- In the root directory of your project create a .env file where you should write your CLIENT_ID and CLIENT_SECRET in order to authenticate
- Install Flask and run the app using the command python app.py in your terminal

The result should look like the one in the clip above.

## Personal experience creating the app

For the first page I learned how to create an image slider for the background.

The second page contains track names, artists and images of albums from the API given by Spotify.
With help from ChatGPT I learned how to create an event listener setup which detects when a new song starts playing and then stops the current one. I definitely have a lot more to learn to expand my frontend knowledge, but for now I wanted to concentrate on the backend and make this app more user friendly.