import flask
from flask import Flask

context = None
app = Flask(__name__, static_folder='web')


@app.route('/pms/<max>')
def get_last_pms(max):
    last_pm_measurents = context.dao.get_last_pm_measurements(max=int(max))
    result = map(lambda x: x.as_json(), last_pm_measurents)
    return flask.jsonify(Response(data=result))


def run_web_server(app_context):
    global context  # flask cannot work in class :(
    context = app_context
    app.run(host='0.0.0.0', port=81)


def Response(data=None, ok=True, errors=[]):
    return {
        'data': data,
        'ok': ok,
        'errors': errors
    }
