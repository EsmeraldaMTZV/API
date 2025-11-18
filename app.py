from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

API = "https://trackapi.nutritionix.com/v2/natural/nutrients"
API_ID = "85FE15DB"
API_KEY = "5bec82b946a3675b9337148433234321"

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/search', methods=('GET', 'POST'))
def search_recipe():
    recipe_query = request.form.get('query', '').strip()

    if not recipe_query:
        flash("Ingresa un nombre de comida o ingrediente.", "error")
        return redirect(url_for('index'))


    if not API_ID or not API_KEY:
        flash("Error de configuración: faltan claves de la API.", "error")
        return redirect(url_for('index'))

    info = {
        "x-app-id": API_ID,
        "x-app-key": API_KEY,
    }


    params = {
        "query": recipe_query,
        "detailed": True
    }

    try:
        
        resp = requests.get(API, info=info, params=params, timeout=10)

        print("STATUS CODE:", resp.status_code)  
        print("RESPUESTA JSON:", resp.json())      

        if resp.status_code != 200:
            flash(f"Error con Nutritionix: código {resp.status_code}", "error")
            return redirect(url_for('index'))

        data = resp.json()

    
        results = data.get("common", []) + data.get("branded", [])

        if not results:
            flash(f'No se encontró información para "{recipe_query}".', 'error')
            return redirect(url_for('index'))

        return render_template('receta.html', results=results, query=recipe_query)

    except requests.exceptions.RequestException:
        flash("Error de conexión con Nutritionix. Intenta más tarde.", "error")
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
