🌦️ Weather App (Aplicación del Clima)
Descripción

Esta es una aplicación del clima desarrollada en Python que utiliza la API de Open-Meteo para obtener datos meteorológicos en tiempo real. Permite consultar el clima actual de una o varias ciudades ingresadas por el usuario.

La aplicación obtiene primero las coordenadas de la ciudad mediante la API de geocodificación y luego consulta los datos del clima actual, mostrando resultados claros y estructurados.

🚀 Características
Consulta del clima en tiempo real
Soporte para múltiples ciudades
Muestra:
Temperatura (°C)
Velocidad del viento
Validación de entrada (evita valores vacíos)
Manejo de errores (ciudades no encontradas o fallas de API)
Código estructurado y fácil de mantener
🛠️ Requisitos
Python 3.8 o superior
Librería requests

Instalar dependencias:

pip install requests
📦 Instalación
Clona el repositorio:
git clone https://github.com/tuusuario/weather-app.git
Entra al directorio:
cd weather-app
Ejecuta el script:
python app.py
🧑‍💻 Uso

Ejecuta la aplicación e ingresa el nombre de una ciudad:

Ingresa el nombre de una ciudad: Tokyo

También puedes consultar varias ciudades (según implementación).

Ejemplo de salida:
{
  "city": "Tokyo",
  "temperature_celsius": 10.9,
  "wind_speed": 6.1
}
⚠️ Manejo de Errores

La aplicación contempla:

Ciudad no encontrada
Entrada vacía
Fallos en la API o conexión

Mostrando mensajes claros para el usuario.

🧪 Pruebas

Se realizaron pruebas básicas:

Entrada válida (ej. "Tokyo")
Entrada inválida (ej. "asdasd123")
Entrada vacía
🤖 Uso de IA

Durante el desarrollo se utilizó IA para:

Generar código base
Detectar errores
Mejorar validaciones y estructura
Generar documentación

Todas las sugerencias fueron revisadas antes de implementarse.

🔒 Seguridad y Buenas Prácticas
No se exponen claves sensibles
Validación de entradas
Manejo de errores robusto
Revisión de código generado por IA
📌 Mejoras Futuras
Interfaz gráfica o web
Implementación de caché
Más variables climáticas (humedad, precipitación)
Optimización de llamadas a la API
📄 Licencia

Este proyecto es de uso educativo.
