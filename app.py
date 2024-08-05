import requests, os # type: ignore
from requests.auth import HTTPBasicAuth # type: ignore
from flask import Flask, request, render_template # type: ignore
from dotenv import load_dotenv # type: ignore

app = Flask(__name__, static_url_path='/static')

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(client_id, client_secret)

response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]

@app.route("/", methods=["GET"])
def index():

    url = "https://api.spotify.com/v1/search"
    headers = {'Authorization': f'Bearer {accessToken}'}
    
    year = request.args.get("year")

    if year:
    
        search = f"?q=year%3A{year}&type=track%2Cartist&limit=10"
        
        fullURL = f"{url}{search}"
        
        response = requests.get(fullURL, headers=headers)
        data = response.json()

        tracks = [
            {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "preview_url": track["preview_url"],
                "images": track["album"]["images"][0]["url"]
            } 
            for track in data["tracks"]["items"]
        ]

        return render_template("home.html", tracks = tracks)
    
    return render_template("index.html")


if __name__ == "__main__":
  app.run(debug=True)