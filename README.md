# WeatherBack

WeatherBack is a simple web app that lets you look up historical weather data for any location and date, going as far back as 1950. Just enter a city name or coordinates along with a date, and see what the weather was like on that day.

## Features

- Check daily weather conditions back to 1950
- Supports city names and latitude/longitude coordinates
- Powered by the Visual Crossing Weather API

## Usage

### Running Locally

1. Clone the repository.
2. Create a `.env` file with your Visual Crossing API key:
   ```
   API_KEY=your_api_key_here
   ```
3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   flask run --debug
   ```

### Docker
1. Build image with `build.sh`
2. Run container
```
docker run -p 5001:5000 --env-file .env weatherback
```

### 

### Kubernetes

## Credits

- Weather data provided by [Visual Crossing](https://www.visualcrossing.com/)
- Built with Flask and Bootstrap
- Developed by Emil Jonsson

## License & Usage

This project is open source and free to use under the MIT License. Feel free to use, modify, and share it as you like.