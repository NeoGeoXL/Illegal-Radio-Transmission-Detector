from ensurepip import bootstrap
from filecmp import DEFAULT_IGNORES
from flask import  request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user
from app import create_app
from app.forms import LoginForm, TodoForm, DeleteTodoForm
from app.firestore_service import *
from sdrscanfm.fm import *
from sdrscantv.tv import *

app = create_app()



@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)




@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)



@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response



@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)

        flash('Tu tarea se creo con éxito!')

        return redirect(url_for('hello'))

    return render_template('hello.html', **context)

@app.route('/fm', methods=['GET', 'POST'])
@login_required
def fm():
    user_ip = session.get('user_ip')
    username = current_user.id

    data1_fm, espuria_1, descision_1 =primera_iteracion_fm()
    frecuencia_fm_1 = espuria_1['Frecuencia']
    potencia_fm_1 = espuria_1['Potencia']

    data2_fm, espuria_2, descision_2 =segunda_iteracion_fm()
    frecuencia_fm_2 = espuria_2['Frecuencia']
    potencia_fm_2 = espuria_2['Potencia']

    data3_fm, espuria_3, descision_3 =tercera_iteracion_fm()
    frecuencia_fm_3 = espuria_3['Frecuencia']
    potencia_fm_3 = espuria_3['Potencia']

    data4_fm, espuria_4, descision_4 =cuarta_iteracion_fm()
    frecuencia_fm_4 = espuria_4['Frecuencia']
    potencia_fm_4 = espuria_4['Potencia']
 
    data5_fm, espuria_5, descision_5 =quinta_iteracion_fm()
    frecuencia_fm_5 = espuria_5['Frecuencia']
    potencia_fm_5 = espuria_5['Potencia']

    context = {
        'username': username,
        'data1_fm': data1_fm,
        'frecuencia_fm_1': frecuencia_fm_1,
        'potencia_fm_1': potencia_fm_1,
        'descision_1': descision_1,
        'data2_fm': data2_fm,
        'frecuencia_fm_2': frecuencia_fm_2,
        'potencia_fm_2': potencia_fm_2,
        'descision_2': descision_2,
        'data3_fm': data3_fm,
        'frecuencia_fm_3': frecuencia_fm_3,
        'potencia_fm_3': potencia_fm_3,
        'descision_3': descision_3,
        'data4_fm': data4_fm,
        'frecuencia_fm_4': frecuencia_fm_4,
        'potencia_fm_4': potencia_fm_4,
        'descision_4': descision_4,
        'data5_fm': data5_fm,
        'frecuencia_fm_5': frecuencia_fm_5,
        'potencia_fm_5': potencia_fm_5,
        'descision_5': descision_5,
    }
    
    #put_signal_fm(user_id=username, signal=data1_fm)
    
    if descision_1 == 1:
        put_alarma(user_id=username, parasita=espuria_1)
    
    if descision_2 == 1:
        put_alarma(user_id=username, parasita=espuria_2)
    
    if descision_3 == 1:
        put_alarma(user_id=username, parasita=espuria_3)
    
    if descision_4 == 1:
        put_alarma(user_id=username, parasita=espuria_4)
    
    if descision_5 == 1:
        put_alarma(user_id=username, parasita=espuria_5)

    return render_template('fm.html',**context)

@app.route('/tv_vhf', methods=['GET', 'POST'])
@login_required
def tv_vhf():
    user_ip = session.get('user_ip')
    username = current_user.id

    data1_tv, espuria_tv_1, descision_tv_1 =primera_iteracion_tv()
    frecuencia_tv_1 = espuria_tv_1['Frecuencia']
    potencia_tv_1 = espuria_tv_1['Potencia']

    data2_tv, espuria_tv_2, descision_tv_2 = segunda_iteracion_tv()
    frecuencia_tv_2 = espuria_tv_2['Frecuencia']
    potencia_tv_2 = espuria_tv_2['Potencia']


    context = {
        'username': username,
        'data1_tv': data1_tv,
        'frecuencia_tv_1': frecuencia_tv_1,
        'potencia_tv_1': potencia_tv_1,
        'descision_tv_1': descision_tv_1,
        'data2_tv': data2_tv,
        'frecuencia_tv_2': frecuencia_tv_2,
        'potencia_tv_2': potencia_tv_2,
        'descision_tv_2': descision_tv_2,

    }

    if descision_tv_1 == 1:
        put_alarma(user_id=username, parasita=espuria_tv_1)
    
    if descision_tv_2 == 1:
        put_alarma(user_id=username, parasita=espuria_tv_2)

    return render_template('tv_vhf.html',**context)

@app.route('/tv_uhf', methods=['GET', 'POST'])
@login_required
def tv_uhf():
    user_ip = session.get('user_ip')
    username = current_user.id

    data3_tv, espuria_tv_3, descision_tv_3 =tercera_iteracion_tv()
    frecuencia_tv_3 = espuria_tv_3['Frecuencia']
    potencia_tv_3 = espuria_tv_3['Potencia']

    data4_tv, espuria_tv_4, descision_tv_4 = cuarta_iteracion_tv()
    frecuencia_tv_4 = espuria_tv_4['Frecuencia']
    potencia_tv_4 = espuria_tv_4['Potencia']

    data5_tv, espuria_tv_5, descision_tv_5 = quinta_iteracion_tv()
    frecuencia_tv_5 = espuria_tv_5['Frecuencia']
    potencia_tv_5 = espuria_tv_5['Potencia']


    context = {
        'username': username,
        'data3_tv': data3_tv,
        'frecuencia_tv_3': frecuencia_tv_3,
        'potencia_tv_3': potencia_tv_3,
        'descision_tv_3': descision_tv_3,
        'data4_tv': data4_tv,
        'frecuencia_tv_4': frecuencia_tv_4,
        'potencia_tv_4': potencia_tv_4,
        'descision_tv_4': descision_tv_4,
        'data5_tv': data5_tv,
        'frecuencia_tv_5': frecuencia_tv_5,
        'potencia_tv_5': potencia_tv_5,
        'descision_tv_5': descision_tv_5,
    
    }

    if descision_tv_3 == 1:
        put_alarma(user_id=username, parasita=espuria_tv_3)
    
    if descision_tv_4 == 1:
        put_alarma(user_id=username, parasita=espuria_tv_4)
    
    if descision_tv_5 == 1:
        put_alarma(user_id=username, parasita=espuria_tv_5)
        
    return render_template('tv_uhf.html',**context)

 
@app.route('/alarmas', methods=['GET', 'POST'])
@login_required
def alarmas():
    user_ip = session.get('user_ip')
    username = current_user.id
    alarmas = get_alarma_fm(user_id=username)
    
    context = {
        'username': username,
        'alarmas': alarmas,

    }
    #print(alarmas)
    alarmas.sort(key=lambda x: x['Fecha'], reverse=True)
    return render_template('alarmas.html',**context)


