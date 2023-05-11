import flask
import settings

app = flask.Flask(__name__)
setting = settings.Settings()


@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html', time=setting.time)


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
            setting.time['teu'][int(key[0]) - 1][int(key[-1]) - 1] = flask.request.form.get(key)
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
        
    })
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55555)
    