from flask import Flask, render_template, request
import requests

app = Flask(__name__)

YOUTUBE_API_KEY = 'AIzaSyD6NsMVcHrIQt-1U_zNwhf97G6kpzlPGM0'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_video', methods = ['POST'])
def get_video():
    category = request.form['category']
    response = requests.get(YOUTUBE_API_URL, params={
        'part': 'snippet',
        'q': f'motivational {category}',
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': 1
    }) 
    
    if response.status_code != 200:
        return render_template('error.html', message="Error fetching videos from YouTube API. ")
    
    data = response.json()
    if 'items' not in data or not data['items']:
        return render_template('error.html',message="No videos found for this category")
    
   
    video_id = data['items'][0]['id']['videoId'] if data['items'] else None
    video_url = f'https://www.youtube.com/watch?v={video_id}' if video_id else "No videos found."
    return render_template('video.html', video_url=video_url, category=category)

if __name__ == '__main__':
    app.run(debug=True)


        
        
        