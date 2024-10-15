# Weather Fetcher

This is a simple Python program that fetches real-time weather data for a given city using the [OpenWeatherMap API](https://openweathermap.org/api). The program is designed in an object-oriented way using Python classes.

## Features

- Fetch current temperature, humidity, and weather description for any city.
- Reads the OpenWeatherMap API key from a text file for security.
- Displays the weather information in a human-readable format.

## Requirements

- Python 3.x
- [Requests library](https://pypi.org/project/requests/)

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/weather-fetcher.git
    cd weather-fetcher
    ```

2. Install the required dependencies:

    ```bash
    pip install requests
    ```

3. Create a file called `api_key.txt` in the root folder of the project. In this file, paste your OpenWeatherMap API key.

    - Example of `api_key.txt`:
      ```
      your_openweather_api_key_here
      ```

4. Run the program by specifying the city name in the code.

## Usage

1. Open the `main.py` file.

2. You can change the `city` variable in the `__main__` block of the script to fetch the weather for a different city.

3. Example:

    ```python
    city = "London"
    ```

4. Run the Python script:

    ```bash
    python weather_fetcher.py
    ```

5. The weather data (temperature, humidity, and description) will be printed to the console.

## Example Output

```bash
City: London
Temperature: 15°C
Humidity: 78%
Weather Description: clear sky
