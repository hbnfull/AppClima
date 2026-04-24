from src.weather import get_weather_for_city
from src.utils import validate_city_input, format_weather_output


def main():
    print("=== Weather App ===")
    print("Consulta el clima actual de una o varias ciudades.")
    print("Escribe varias ciudades separadas por coma.")
    print()

    user_input = input("Ingresa ciudad(es): ")

    try:
        cities = validate_city_input(user_input)

        print("\nResultados:\n")

        for city in cities:
            try:
                weather = get_weather_for_city(city)
                print(format_weather_output(weather))

            except ValueError as error:
                print(f"{city}: {error}")
                print("-" * 35)

            except Exception as error:
                print(f"{city}: ocurrió un error inesperado: {error}")
                print("-" * 35)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()