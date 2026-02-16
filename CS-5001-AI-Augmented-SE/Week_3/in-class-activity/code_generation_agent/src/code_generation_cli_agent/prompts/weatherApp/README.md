# Weather Dashboard

A simple Weather Dashboard application built with Express.js and OpenWeatherMap API.

## Features

- Fetch real-time weather data for any city
- Clean, modern UI with responsive design
- Displays temperature, weather conditions, humidity, wind speed, and more
- Weather icons from OpenWeatherMap

## Setup Instructions

### Prerequisites

- Node.js (v14 or higher)
- npm (comes with Node.js)

### Installation

1. Clone this repository or download the files
2. Navigate to the project directory
3. Install dependencies:
   bash
   npm install
   

### Configuration

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Replace `YOUR_OPENWEATHERMAP_API_KEY` in `server.js` with your actual API key

### Running the Application

Start the server:
bash
npm start


Or for development with automatic restarts:
bash
npm install -g nodemon
nodemon server.js


Then open your browser and navigate to:

http://localhost:3000


## Usage

1. Enter a city name in the input field
2. Click "Get Weather" button
3. View the weather information for that city

## Project Structure


weather-dashboard/
├── public/
│   ├── index.html      # Main HTML file
│   └── style.css       # CSS styling
├── server.js           # Express server
├── package.json        # Project dependencies
└── README.md           # This file


## Dependencies

- **express**: Web framework for Node.js
- **axios**: Promise-based HTTP client for making API requests
- **body-parser**: Middleware for parsing request bodies
- **cors**: Enable CORS for development

## API Endpoints

### POST /api/weather

Fetches weather data for a specified city.

**Request Body:**

{
  "city": "London"
}


**Response:**

{
  "city": "London",
  "temperature": 15.5,
  "feelsLike": 14.2,
  "description": "scattered clouds",
  "humidity": 65,
  "windSpeed": 3.6,
  "icon": "03d",
  "timestamp": "5/15/2023, 2:30:45 PM"
}


## Notes

- This is a basic implementation for demonstration purposes
- In a production environment, you should:
  - Use environment variables for API keys
  - Add input validation
  - Implement proper error handling
  - Add rate limiting
  - Consider caching weather data

## License

MIT