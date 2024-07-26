# motivational-video-finder

Motivational Video Finder is a web application that helps users discover motivational videos based on various categories such as relationships, life, work, success, and more.

**Features**
  Search for motivational videos by category.
  View the latest motivational videos fetched from YouTube.
  Click to watch videos directly on YouTube.

**Technologies Used**
  Python
  Flask
  HTML/CSS
  YouTube Data API (via google-api-python-client)
  Werkzeug
  Gunicorn (for deployment)

Setup Instructions

To run Motivational Video Finder locally, follow these steps:

**Prerequisites**
  Python 3.x installed on your system
  YouTube Data API key (instructions on obtaining one here)
  Git installed (optional for cloning the repository)
**Installation**
  Clone the repository (if you haven't already):
  git clone https://github.com/yourusername/motivational-video-finder.git
  cd motivational-video-finder
  Install Dependencies
  pip install -r requirements.txt
**Configuration**
  Set Up API Key
  Obtain your YouTube Data API key from Google Developer Console.
  
  Replace 'YOUR_YOUTUBE_API_KEY' in app.py with your actual API key:
  YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'
**Running the Application**
  Start Flask Server
  python app.py
  Access the Application
  Open your web browser and go to http://localhost:5000 to access the Motivational Video Finder application.

**Usage**
  Choose a category (e.g., relationships, life, work) and click "Search" to find motivational videos.
  Click on any video link to watch it directly on YouTube.
