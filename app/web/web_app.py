import traceback

import simplejson as json
from flask import Flask

from app.repositories.Repository import Repository

repository: Repository = None
app = Flask(__name__, static_folder='web')


@app.route('/measurements/<max>')
def get_last_measurements(max):
    last_measurements = repository.get_last(max=int(max))
    last_measurements = sorted(last_measurements, key=lambda x: x.timestamp, reverse=True)
    result = list(map(lambda x: x.to_json(), last_measurements))
    return json.dumps(Response(data=result))


def run_web_server(_repository):
    try:
        global repository  # flask cannot work in class :(
        repository = _repository
        app.run(host='0.0.0.0', port=81)
    except Exception:
        print(str(traceback.format_exc()))


def Response(data=None, ok=True, errors=[]):
    return {
        'data': data,
        'success': ok,
        'errors': errors
    }
