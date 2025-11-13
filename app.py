from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'
API = "https://d1gvlspmcma3iu.cloudfront.net/restaurants-3d-party.json.gz"

info = {
    'id' : '85FE15DB',
    'key' : '5bec82b946a3675b9337148433234321'
}

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_r():
    restaurante_name = request.form.get ('restaurante_name', '').strip().lower()
    
    if not pokemon_name:
        flash('Ingresa un nombre correcto del restaurante', 'error')
        return redirect(url_for('index'))
    
    
    if __name__ == "__main__":
        app.run(debug=True)