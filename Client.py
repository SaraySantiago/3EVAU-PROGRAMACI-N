# Cliente que consume la API REST del servidor
import requests

response = requests.get("http://localhost:5000/api/data")
print(response.json())
