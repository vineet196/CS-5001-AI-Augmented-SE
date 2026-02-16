const express = require('express');
const axios = require('axios');
const app = express();
const API_KEY = "28bf717c1da5e4ca46f5b8f8d998bbe5";

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Weather App</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
                form { display: flex; margin-bottom: 20px; }
                input { flex-grow: 1; padding: 8px; font-size: 16px; }
                button { padding: 8px 16px; font-size: 16px; background: #007bff; color: white; border: none; cursor: pointer; }
                .result { padding: 15px; border-radius: 5px; margin-top: 20px; }
                .error { background: #ffdddd; color: #d8000c; }
                .success { background: #ddffdd; color: #4f8a10; }
            </style>
        </head>
        <body>
            <h1>Weather App</h1>
            <form action="/get-weather" method="POST">
                <input type="text" name="city" placeholder="Enter city name" required>
                <button type="submit">Get Weather</button>
            </form>
            ${req.query.error ? `<div class="result error">${req.query.error}</div>` : ''}
        </body>
        </html>
    `);
});

app.post('/get-weather', async (req, res) => {
    const city = req.body.city;
    try {
        const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`);
        const data = response.data;
        const temperature = data.main.temp;
        const description = data.weather[0].description;
        res.send(`
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Weather App</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
                    form { display: flex; margin-bottom: 20px; }
                    input { flex-grow: 1; padding: 8px; font-size: 16px; }
                    button { padding: 8px 16px; font-size: 16px; background: #007bff; color: white; border: none; cursor: pointer; }
                    .result { padding: 15px; border-radius: 5px; margin-top: 20px; }
                    .error { background: #ffdddd; color: #d8000c; }
                    .success { background: #ddffdd; color: #4f8a10; }
                </style>
            </head>
            <body>
                <h1>Weather App</h1>
                <form action="/get-weather" method="POST">
                    <input type="text" name="city" placeholder="Enter city name" required>
                    <button type="submit">Get Weather</button>
                </form>
                <div class="result success">
                    <h2>Weather in ${city}</h2>
                    <p>Temperature: ${temperature}°C</p>
                    <p>Conditions: ${description}</p>
                </div>
            </body>
            </html>
        `);
    } catch (error) {
        const errorMessage = error.response?.data?.message || "Failed to fetch weather data. Please try again.";
        res.redirect(`/?error=${encodeURIComponent(errorMessage)}`);
    }
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});