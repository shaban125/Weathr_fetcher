import requests


class WeatherFetcher:
    
    def __init__(self, file_path):
        """
        The constructor method (__init__) is used to initialize the object with an API key.
        It reads the API key from the provided file when the object is created.
        """
        self.api_key = self.read_api_key(file_path)  # Read the API key from the file
    
    def read_api_key(self, file_path):
        """
        This method reads the API key from a text file.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return None
    
    def get_weather_data(self, city):
        """
        This method fetches the weather data for a given city using the API key.
        """
        if self.api_key is None:
            print("API key is not available.")
            return
        
        # API base URL and parameters
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Temperature in Celsius
        }
        
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            
            # Display the weather information
            print(f"City: {city}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather Description: {description}")
        else:
            print(f"Failed to fetch data for {city}. Error code: {response.status_code}")


if __name__ == "__main__":
    # Specify the path to your API key file
    file_path = "/home/shaban/Desktop/weather_forcasting/api_key"  #
    
    weather_fetcher = WeatherFetcher(file_path)
    
    # Specify the city for which you want to fetch the weather
    city = "Islamabad"
    
    # Fetch and display the weather data
    weather_fetcher.get_weather_data(city)
