import requests


def get_coordinates(city):
    """
    Obtiene latitud y longitud de una ciudad usando la API de geocodificación de Open-Meteo.

    Args:
        city (str): Nombre de la ciudad

    Returns:
        dict: Diccionario con latitude, longitude, name y country

    Raises:
        ValueError: Si la ciudad no es válida o no se encuentra
        requests.exceptions.RequestException: Si falla la solicitud HTTP
    """
    if not city or not city.strip():
        raise ValueError("Nombre de ciudad inválido")

    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1,
        "language": "es",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if "results" not in data or not data["results"]:
        raise ValueError("Ciudad no encontrada")

    result = data["results"][0]

    return {
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "name": result["name"],
        "country": result.get("country", "N/A")
    }