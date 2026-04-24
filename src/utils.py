def validate_city_input(user_input):
    """
    Valida y limpia la entrada del usuario.

    Args:
        user_input (str): Entrada del usuario

    Returns:
        list: Lista de ciudades limpias

    Raises:
        ValueError: Si no hay ciudades válidas
    """
    if not user_input or not user_input.strip():
        raise ValueError("Debes ingresar al menos una ciudad")

    cities = [city.strip() for city in user_input.split(",") if city.strip()]

    if not cities:
        raise ValueError("No se encontraron ciudades válidas")

    return cities


def format_weather_output(weather_data):
    """
    Formatea la salida del clima para impresión en consola.

    Args:
        weather_data (dict): Datos del clima

    Returns:
        str: Texto formateado
    """
    return (
        f"Ciudad: {weather_data['city']}, {weather_data['country']}\n"
        f"Temperatura: {weather_data['temperature']} °C\n"
        f"Viento: {weather_data['wind_speed']} km/h\n"
        f"Condición: {weather_data['condition']}\n"
        + "-" * 35
    )