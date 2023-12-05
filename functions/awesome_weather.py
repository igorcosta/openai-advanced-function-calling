import requests
from utils.functions_metadata import function_schema


@function_schema(
    name="get_weather_forecast",
    description="Finds information the forecast of a specific location and provides a simple interpretation like, is going to rain, it's hot, it's super hot instead of warmer",
    required_params=["location"]
)
def get_weather_forecast(location):
    """
    :param location: The location to get the weather forecast
    """
    url = f"http://wttr.in/{location}?format=3"
    try:
        print("Called ")
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Error getting weather data: {e}"


if __name__ == "__main__":
    location = "London"  # Example location
    print(get_weather_forecast(location))
