# WeatherBack

WeatherBack is a simple web app that lets you look up historical weather data for any location and date, going as far back as 1950. Just enter a city name or coordinates along with a date, and see what the weather was like on that day.

![image](https://github.com/user-attachments/assets/5a7028a5-0242-416d-b524-ddcfa6bb6538)


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

The Dockerfile and app source code are located in the `docker/` folder.

1. Move to the docker folder:
   ```
   cd docker
   ```

2. Build and push the image (requires Docker login):
   ```
   ./build.sh
   ```

3. Run the container locally:
   ```
   docker run -p 5000:5000 --env-file ../.env weatherback
   ```

---

### Kubernetes

Kubernetes deployment files are located in the `kubernetes/` folder.

#### Deploy to Minikube

1. Start Minikube if not already running:
   ```
   minikube start
   ```

2. Apply the secrets, deployment, and service:
   ```
   kubectl apply -f kubernetes/secrets/api_key_secret.yaml
   kubectl apply -f kubernetes/weatherback_deployment.yaml
   kubectl apply -f kubernetes/weatherback_service.yaml
   ```

3. Expose the app:
   ```
   minikube service weatherback-service
   ```

Or manually get the Minikube IP and access the app:
   ```
   minikube ip
   # Use http://<minikube-ip>:30001 in your browser
   ```

## Credits

- Weather data provided by [Visual Crossing](https://www.visualcrossing.com/)
- Built with Flask and Bootstrap
- Developed by Emil Jonsson

## License & Usage

This project is open source and free to use under the MIT License. Feel free to use, modify, and share it as you like.
