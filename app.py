from flask import Flask, request, render_template, url_for, flash, redirect
from sqlalchemy.exc import SQLAlchemyError
from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@login_manager.user_loader
def login_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    result = db_session.execute(user).scalar_one_or_none()
    return result

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
@login_required
def funcionarios():
    return render_template("funcionarios.html")

@app.route('/animais')
def animais():
    return render_template('animais.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get['form-email']
        senha = request.form.get['form-senha']
        ''' verificação usando not
        if not email or not senha:
            flash('Preenchar todos o campos', 'danger')
            return render_template('login.html')
        '''
        if not email and not senha:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                # se encotrado na base de dados
                if resultado_email.check_password(senha):
                     # login correto
                    login_user(resultado_email)
                    flash(f'Login Sucesso', 'success')
                    return redirect(url_for('home'))
                else:
                    # login incorreto
                    flash('Senha incorreta', 'alert-danger')
                    return render_template('login.html')
            else:
                # se não encontrado
                flash(f'Email não encontrado', 'alert-danger')
                return redirect(url_for('login'))

        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/cadastro_funcionario', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        data_nascimento = request.form.get('form-data_nascimento')
        cpf = request.form.get('form-cpf')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        cargo = request.form.get('form-cargo')
        salario = request.form.get('form-salario')

        if not nome or email or senha:
            flash('Preencher os campos', 'danger')
            return render_template('funcionarios.html')

        verifica_email = select(Funcionario).where(Funcionario.email == email)
        existe_email = db_session.execute(verifica_email).scalar_one_or_none()

        if existe_email:
            flash(f'Email {email} ja esta cadastrado', 'danger')
            return render_template('funcionarios.html')
        try:
            novo_funcionarios = Funcionario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, email=email, senha=senha, cargo=cargo, salario=float(salario))
            novo_funcionarios.set_password(senha)
            db_session.add(novo_funcionarios)
            db_session.commit()
            flash(f'Usuario {nome} cadastrado com sucesso', 'success')
            return redirect(url_for('funcionarios'))
        except SQLAlchemyError as e:
            flash(f'Erro na base de dados ao cadastrar usuario: {e}', 'danger')
            print(f'Erro na base de dados:{e}')
            return redirect(url_for('funcionarios'))
        except Exception as e:
            flash(f'Erro ao cadastro o funcionario: {e}', 'danger')
            print(f'Erro ao cadastrar:{e}')
    return render_template('funcionarios.html')

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
    app.run(debug=True, port=5005)