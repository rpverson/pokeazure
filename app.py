import requests
from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    # Obtener un número aleatorio de Pokémon (por ejemplo, entre 1 y 151 para la primera generación)
    random_pokemon_number = randint(1, 151)
    # Hacer una solicitud a la API de Pokémon
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_pokemon_number}')
    # Convertir la respuesta a JSON
    pokemon_data = response.json()

    # Pasar los datos a la plantilla
    return render_template('index.html', pokemon=pokemon_data)


if __name__ == '__main__':
    app.run(debug=True)
