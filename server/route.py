from __future__ import print_function, division

import json
from datetime import datetime

import numpy as np
from flask import Flask, jsonify, abort, make_response, request
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/plugs/*": {"origins": "*"}})

states = np.array([0, 0, 0, 0], dtype=bool)
path = 'plugs_data.json'


def read4json(file_path):
    "Read configuration data form json file and return a list"
    with open(file_path, 'r') as data_file:
        data = json.load(data_file)

    return data['plugs']

def save2json(file_path, data):
    "Save configuration data to a json file"
    with open(file_path, 'w') as data_file:
        json.dump({'plugs':data}, data_file, indent=4)


################################################################
# Definition of the routes
################################################################
@app.route('/api/plugs', methods=['GET'])        
def get_plugs():
    """
    Gets metadata of all plugs.

    Return
    ------
    plugs : json
      Json with the properties of all plugs.
      The properties are:
        id : int
          Id of the plug.
        name : str
          Some name to remember wath it has connected.
        state : bool
          On/Off
        alarm : list
          List with the alarms.
    """
    plugs = read4json(path)
    return jsonify({'plugs': plugs})


@app.route('/api/plugs/<int:plug_id>', methods=['GET'])
def get_plug(plug_id):
    """
    Gets a plug's metadata by ID.

    Path Parameters
    ---------------
    plug_id : int
      Plug ID.

    Request body
    ------------
    Do not supply a request body with this method.

    Return
    ------
    plug : json
      Propertie of one plug by its ID.
    """
    plugs = read4json(path)
    plug = [plug for plug in plugs if plug['id'] == plug_id]

    if len(plug) == 0:
        abort(404)
    return jsonify({'plug': plug[0]})


@app.route('/api/plugs/<int:plug_id>', methods=['PUT'])
def rename_plug(plug_id):
    """
    Rename some plug, by its ID, to remember wath it has connected.

    Path Parameters
    ---------------
    plug_id : int
      Plug ID.

    Request body
    ------------
    name : str
      New name.

    Return
    ------
    plug : json
      Propertie of one plug by its ID.
    """
    plugs = read4json(path)
    plug = [plug for plug in plugs if plug['id'] == plug_id]

    if len(plug) == 0:
        abort(400)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)

    plugs[plug_id]['name'] = request.json['name']
    save2json(path, plugs)
    return jsonify({'plugs': plugs})


@app.route('/api/plugs/<int:plug_id>/state', methods=['PUT'])
def change_state(plug_id):
    """
    Change plug state (On/Off).

    Parameters
    ----------
    plug_id : int
      Plug ID.
    state : bool
      Plug state.
    """
    plugs = read4json(path)
    plug = [plug for plug in plugs if plug['id'] == plug_id]

    print(request.json)

    if len(plug) == 0:
        abort(400)
    if not request.json:
        abort(400)
    if 'state' in request.json and type(request.json['state']) != bool:
        abort(400)

    plugs[plug_id]['state'] = request.json['state']
    save2json(path, plugs)
    return jsonify({'plugs': plugs})


@app.route('/api/plugs/<int:plug_id>', methods=['POST'])
def create_alarm(plug_id):
    """
    Create alarm to plug[id]

    Parameter
    ---------
    plug_id : int
      Plug ID.
    date : str
      Date of the new alarm. The format must be `yyyy-mm-dd hh:mm`.
    """
    if not request.json or not 'date' in request.json:
        abort(400)

    date_format = '%Y-%m-%d %H:%M'
    new_alarm = request.json['date']
    new_alarm = datetime.strptime(new_alarm, date_format)
    now = datetime.now()

    if now > new_alarm:
        abort(400)

    data = read4json(path)
    if not str(new_alarm) in data[plug_id]['alarm']:
        data[plug_id]['alarm'].append(str(new_alarm))
        save2json(path, data)

    return jsonify({'plugs': data}), 201


@app.route('/api/plugs/<int:plug_id>', methods=['DELETE'])
def delete_alarm(plug_id):
    """
    Delete an alarm.

    Parameters
    ----------
    plug_id : int
      Plug ID.
    date : str
      Alarm to delete. The format must be `yyyy-mm-dd hh:mm`.
    """
    plugs = read4json(path)
    plug = [plug for plug in plugs if plug['id'] == plug_id]

    if len(plug) == 0:
        abort(400)
    if not request.json:
        abort(400)
    if 'state' in request.json and type(request.json['state']) != bool:
        abort(400)

    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    """
    404 error.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8003"),
        debug=True
    )
