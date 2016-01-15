from __future__ import print_function, division
import json
from datetime import datetime

from flask import jsonify, abort, make_response, request
from flask_security import  login_required

from zapat_ip import app

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

    Request Body
    ------------
    Do not supply a request body with this method.

    Return
    ------
    plug : json
      Propertie of a plug by its ID.
    """
    plugs = read4json(path)

    # Check if the plug_id exist
    ids = [x['id'] for x in plugs]
    if plug_id not in ids:
        abort(404)

    return jsonify({'plug': plugs[plug_id]})


@app.route('/api/plugs/<int:plug_id>', methods=['PUT'])
def rename_plug(plug_id):
    """
    Rename some plug, by its ID.

    Path Parameters
    ---------------
    plug_id : int
      Plug ID.

    Request Body
    ------------
    name : str
      New name.

    Return
    ------
    plug : json
      Propertie of the rename plug.
    """
    plugs = read4json(path)

    # Check if the plug_id exist
    ids = [x['id'] for x in plugs]
    if plug_id not in ids:
        abort(404)

    # Check the request body
    if not request.json:
        abort(400)
    if not 'name' in request.json:
        abort(400)
    if type(request.json['name']) != unicode:
        abort(400)

    plugs[plug_id]['name'] = request.json['name']
    save2json(path, plugs)
    return jsonify({'plug': plugs[plug_id]})


@app.route('/api/plugs/<int:plug_id>/state', methods=['PUT'])
def change_state(plug_id):
    """
    Change plug state (On/Off).

    Path Parameters
    ---------------
    plug_id : int
      Plug ID.

    Request Body
    ------------
    state : bool
      Plug state.

    Return
    ------
    plug : json
      Propertie of a plug (by id).
    """
    plugs = read4json(path)

    # Check if the plug_id exist
    ids = [x['id'] for x in plugs]
    if plug_id not in ids:
        abort(404)

    # Check the request body
    if not request.json:
        abort(400)
    if not 'state' in request.json:
        abort(400)
    if type(request.json['state']) != bool:
        abort(400)

    plugs[plug_id]['state'] = request.json['state']
    save2json(path, plugs)
    return jsonify({'plug': plugs[plug_id]})


@app.route('/api/plugs/<int:plug_id>', methods=['POST'])
def create_alarm(plug_id):
    """
    Create alarm to plug[id]

    Path Parameter
    --------------
    plug_id : int
      Plug ID.

    Request Body
    ------------
    date : str
      Date of the new alarm. The format must be `yyyy-mm-dd hh:mm`.

    Return
    ------
    plug : json
      Propertie of a plug by its ID.
    """
    plugs = read4json(path)

    # Check if the plug_id exist
    ids = [x['id'] for x in plugs]
    if plug_id not in ids:
        abort(404)

    # Check the request body
    if not request.json:
        abort(400)
    if not 'date' in request.json:
        abort(400)
    if type(request.json['date']) != unicode:
        abort(400)

    date_format = '%Y-%m-%d %H:%M'
    new_alarm = request.json['date']

    try:
        new_alarm = datetime.strptime(new_alarm, date_format)
    except ValueError:
        abort(400)

    now = datetime.now()
    if now > new_alarm:
        abort(400)

    # Not repeat the same alarms
    if not str(new_alarm) in plugs[plug_id]['alarm']:
        plugs[plug_id]['alarm'].append(str(new_alarm))
        save2json(path, plugs)

    return jsonify({'plug': plugs[plug_id]}), 201


@app.route('/api/plugs/<int:plug_id>', methods=['DELETE'])
def delete_alarm(plug_id):
    """
    Delete an alarm.

    Path Parameters
    ---------------
    plug_id : int
      Plug ID.

    Request Body
    ------------
    date : str
      Alarm to delete. The format must be `yyyy-mm-dd hh:mm`.

    Return
    ------
    plug : json
      Propertie of a plug by its ID.
    """
    plugs = read4json(path)

    # Check if the plug_id exist
    ids = [x['id'] for x in plugs]
    if plug_id not in ids:
        abort(404)

    # Check the request body
    if not request.json:
        abort(400)
    if not 'date' in request.json:
        abort(400)
    if type(request.json['date']) != unicode:
        abort(400)

    date_format = '%Y-%m-%d %H:%M'
    new_alarm = request.json['date']

    try:
        new_alarm = datetime.strptime(new_alarm, date_format)
    except ValueError:
        abort(400)

    return jsonify({'result': True})


######################################################################
# ERRORS
######################################################################

@app.errorhandler(400)
def not_found(error):
    """
    Error 400 for Bad Request.

    The body request is empy or with a bad key (for example `new_name` in side of `name`).
    """
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(401)
def not_found(error):
    """
    Error 401 for Unauthorized.
    """
    return make_response(jsonify({'error': 'Unauthorized'}), 401)


@app.errorhandler(404)
def not_found(error):
    """
    Error 404 for Resource Not Found.

    The id in the URI don't exist.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)
