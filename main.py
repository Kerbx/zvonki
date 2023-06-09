import auto
import datetime
import flask
import rpiIO
import settings
import threading


app = flask.Flask(__name__)
setting = settings.Settings()
controller = rpiIO.IOControl()
timing = auto.Auto(controller=controller)

thread = threading.Thread(target=timing.check, daemon=True, args=(setting.time,))


@app.route('/', methods=['GET', 'POST'])
def index():
    print(controller.getState('pin2'))
    return flask.render_template('index.html', time=setting.time, uwuga='Включить' if controller.getState('pin2') else 'Выключить')


@app.route('/uwuga', methods=['GET', 'POST'])
def uwuga():
    if flask.request.method == 'POST':
        print(flask.request.form)
        if flask.request.form.get('uwuga') == 'Включить':
            print('on')
            controller.turnOn('pin2')
        elif flask.request.form.get('uwuga') == 'Выключить':
            print('off')
            controller.turnOff('pin2')
        
        return flask.redirect('/')
    
        
@app.route('/mon', methods=['GET', 'POST'])
def mon():
    if flask.request.method == 'POST':
        for key in flask.request.form:
            setting.time['mon'][int(key[0]) - 1][int(key[-1]) - 1] = flask.request.form.get(key)
        setting.saveSettings()
    return flask.redirect('/')
    

@app.route('/tue', methods=['GET', 'POST'])
def teu():
    if flask.request.method == 'POST':
        for key in flask.request.form:
            setting.time['tue'][int(key[0]) - 1][int(key[-1]) - 1] = flask.request.form.get(key)
        setting.saveSettings()
    return flask.redirect('/')
    
    
@app.route('/wed', methods=['GET', 'POST'])
def wed():
    if flask.request.method == 'POST':
        for key in flask.request.form:
            setting.time['wed'][int(key[0]) - 1][int(key[-1]) - 1] = flask.request.form.get(key)
        setting.saveSettings()
    return flask.redirect('/')
    
    
@app.route('/thu', methods=['GET', 'POST'])
def thu():
    if flask.request.method == 'POST':
        for key in flask.request.form:
            setting.time['thu'][int(key[0]) - 1][int(key[-1]) - 1] = flask.request.form.get(key)
        setting.saveSettings()
    return flask.redirect('/')
    
    
@app.route('/fri', methods=['GET', 'POST'])
def fri():
    if flask.request.method == 'POST':
        for key in flask.request.form:
            setting.time['fri'][int(key[0]) - 1][int(key[-1]) - 1] = flask.request.form.get(key)
        setting.saveSettings()
    return flask.redirect('/')
    
    
@app.route('/update', methods=['GET', 'POST'])
def update():
    return flask.jsonify({
        'time': str(datetime.datetime.now())[:-11]
    })
    
    
if __name__ == '__main__':
    thread.start()
    app.run(host='0.0.0.0', port=55555)
    