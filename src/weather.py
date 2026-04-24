import requests
from src.geocoding import get_coordinates


def get_weather_for_city(city):
    """
    Obtiene el clima actual de una ciudad.

    Args:
        city (str): Nombre de la ciudad

    Returns:
        dict: Información del clima
    """
    if not city or not city.strip():
        raise ValueError("Nombre de ciudad inválido")

    location = get_coordinates(city)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current_weather": True
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if "current_weather" not in data:
        raise ValueError("No se encontraron datos del clima")

    weather = data["current_weather"]

    return {
        "city": location["name"],
        "country": location["country"],
        "temperature": weather.get("temperature"),
        "wind_speed": weather.get("windspeed"),
        "condition": map_weather_code(weather.get("weathercode"))
    }


def map_weather_code(code):
    """
    Traduce el weathercode de Open-Meteo a una descripción simple.
    """
    weather_map = {
        0: "Despejado",
        1: "Mayormente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Niebla",
        48: "Niebla con escarcha",
        51: "Llovizna ligera",
        53: "Llovizna moderada",
        55: "Llovizna intensa",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia fuerte",
        71: "Nieve ligera",
        73: "Nieve moderada",
        75: "Nieve fuerte",
        80: "Chubascos ligeros",
        81: "Chubascos moderados",
        82: "Chubascos fuertes"
    }

    return weather_map.get(code, "Condición desconocida")