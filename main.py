import flask


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    time={
        'mon':[[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
        'tue':[[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
        'wed':[[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
        'thu':[[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
        'fri':[[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
    }
    return flask.render_template('index.html', time=time)


@app.route('/update', methods=['GET', 'POST'])
def update():
    return flask.jsonify({
        
    })
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55555)
    