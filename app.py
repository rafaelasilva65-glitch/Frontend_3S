from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/funcionarios')
def funcionarios():
    return render_template("funcionarios.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash('Soma realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # Passo 1: Emitir a mensagem e a categoria do flash
            flash('Preencha o campo', 'alert-danger')

    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            sub = n1 - n2
            flash('Soma realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, sub=sub)
        else:
            flash('Preencha o campo', 'alert-danger')


    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multi = n1 * n2
            flash('Soma realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multi=multi)
        else:
            flash('Preencha o campo', 'alert-danger')


    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            divi = n1 / n2
            flash('Soma realizada', 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, divi=divi)
        else:
            flash('Preencha o campo', 'alert-danger')


    return render_template("operacoes.html")

@app.route('/triangulo', methods=['GET', 'POST'])
def triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = float(request.form['form-n1'])
            n2 = float(request.form['form-n2'])
            triangulo = n1 * n2 / 2
            flash('Soma realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, triangulo=triangulo)
        else:
            flash('Preencha o campo', 'alert-danger')

    return render_template("geometria.html")

@app.route('/perimetro_tria', methods=['GET', 'POST'])
def perimetro_tria():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2'] and request.form['form-n3']:
            n1 = float(request.form['form-n1'])
            n2 = float(request.form['form-n2'])
            n3 = float(request.form['form-n3'])
            perimetro_tria = n1 + n2 + n3
            flash('Soma realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, perimetro_tria=perimetro_tria)
        else:
            flash('Preencha o campo', 'alert-danger')

    return render_template("geometria.html")

@app.route('/area_circ', methods=['GET', 'POST'])
def area_circ():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = float(request.form['form-n1'])
            n2 = float(request.form['form-n2'])
            area_circ = n1 * n2 * 3.14
            flash('Soma realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, area_circ=area_circ)
        else:
            flash('Preencha o campo', 'alert-danger')

    return render_template("geometria.html")

@app.route('/perimetro_circ', methods=['GET', 'POST'])
def perimetro_circ():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            perimetro_circ = n1 * 3.14
            flash('Soma realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, perimetro_circ=perimetro_circ)
        else:
            flash('Preencha o campo', 'alert-danger')

    return render_template("geometria.html")

@app.route('/area_quad', methods=['GET', 'POST'])
def area_quad():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = float(request.form['form-n1'])
            n2 = float(request.form['form-n2'])
            area_quad = n1 * n2
            flash('Soma realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, area_quad=area_quad)
        else:
            flash('Preencha o campo', 'alert-danger')

    return render_template("geometria.html")

@app.route('/perimetro_quad', methods=['GET', 'POST'])
def perimetro_quad():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2'] and request.form['form-n3'] and request.form['form-n4']:
            n1 = float(request.form['form-n1'])
            n2 = float(request.form['form-n2'])
            n3 = float(request.form['form-n3'])
            n4 = float(request.form['form-n4'])
            perimetro_quad = n1 + n2 + n3 + n4
            flash('Soma realizada', 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, n4=n4, perimetro_quad=perimetro_quad)
        else:
            flash('Preencha o campo', 'alert-danger')

    return render_template("geometria.html")

@app.route('/area_hexa', methods=['GET', 'POST'])
def area_hexa():
    if request.method == 'POST':
        if request.form['form_area_hexa']:
            lado_h = float(request.form['form_area_hexa'])
            area_h = 3 * pow(lado_h, 2) * 3 ** 0.5 / 2
            flash('Soma realizada', 'alert-success')
            return render_template("geometria.html", area_hexa=area_hexa, area_h=round (area_h, 2), lado_h=lado_h)
        else:
            flash('Preencha o campo', 'alert-danger')

    return render_template("geometria.html")

@app.route('/perimetro_hexa', methods=['GET', 'POST'])
def perimetro_hexa():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2'] and request.form['form-n3'] and request.form['form-n4'] and request.form['form-n5'] and request.form['form-n6']:
            n1 = float(request.form['form-n1'])
            n2 = float(request.form['form-n2'])
            n3 = float(request.form['form-n3'])
            n4 = float(request.form['form-n4'])
            n5 = float(request.form['form-n5'])
            n6 = float(request.form['form-n6'])
            perimetro_hexa = n1 + n2 + n3 + n4 + n5 + n6
            flash('Soma realizada', 'alert-success')
            return render_template(geometria.html, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, perimetro_hexa=perimetro_hexa)
        else:
            flash('Preencha o campo', 'alert-danger')

        return render_template("geometria.html")


    return render_template("geometria.html")
#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)