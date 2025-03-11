# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    if request.form.get('button_comunes'):
        return redirect('/comunes')
    
    elif request.form.get('button_raros'):
        return redirect('/raros')
    
    elif request.form.get('button_ultrararos'): 
        return redirect('/ultrararos')
    
    return render_template('index.html')

@app.route('/comunes', methods=['GET', 'POST'])
def comunes():
    if request.method == 'POST':
        if request.form.get('button_bajo'):
            return redirect('/comunesbajo')
        elif request.form.get('button_medio'):
            return redirect('/comunesmedio')
        elif request.form.get('button_alto'):
            return redirect('/comunesalto')
    return render_template('comunes.html')

@app.route('/comunesbajo')
def comunesbajo():
    return render_template('comunesbajo.html')

@app.route('/comunesmedio')
def comunesmedio():
    return render_template('comunesmedio.html')

@app.route('/comunesalto')
def comunesalto():
    return render_template('comunesalto.html')

@app.route('/raros', methods=['GET', 'POST'])
def raros():
    if request.method == 'POST':
        if request.form.get('button_bajo'):
            return redirect('/rarosbajo')
        elif request.form.get('button_medio'):
            return redirect('/rarosmedio')
        elif request.form.get('button_alto'):
            return redirect('/rarosalto')
    return render_template('raros.html')

@app.route('/rarosbajo')
def rarosbajo():
    return render_template('rarosbajo.html')

@app.route('/rarosmedio')
def rarosmedio():
    return render_template('rarosmedio.html')

@app.route('/rarosalto')
def rarosalto():
    return render_template('rarosalto.html')

@app.route('/ultrararos', methods=['GET', 'POST'])
def ultrararos():
    if request.method == 'POST':
        if request.form.get('button_bajo'):
            return redirect('/ultrararosbajo')
        elif request.form.get('button_medio'):
            return redirect('/ultrararosmedio')
        elif request.form.get('button_alto'):
            return redirect('/ultrararosalto')
    return render_template('ultrararos.html')

@app.route('/ultrararosbajo')
def ultrararosbajo():
    return render_template('ultrararosbajo.html')

@app.route('/ultrararosmedio')
def ultrararosmedio():
    return render_template('ultrararosmedio.html')

@app.route('/ultrararosalto')
def ultrararosalto():
    return render_template('ultrararosalto.html')

if __name__ == "__main__":
    app.run(debug=True)