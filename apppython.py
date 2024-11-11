from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ["GET"])
def hello():
    data = [{
        'nama': 'akbarr',
        'pekerjaan' : 'polisi dunia',
        'pesan' : 'kamu pasti takut ketemu evos galang'
    }]
    return make_response(jsonify({'data': data}), 200)

app.run

@app.route('/karyawan', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama' : 'akbarr GET',
                'pekerjaan' : 'polisi dunia',
                'usia' : '10',
            }]
        elif request.method == 'POST':
            data = [{
                'nama' : 'akbarr POST',
                'pekerjan' : 'polisi dunia',
                'usia' : '10',
            }]
        elif request.method == 'PUT':
            data = [{
                'nama' : 'akbarr PUT', 
                'pekerjaan' : 'polisi dunia',
                'usia' : '10'
            }]
        else:
            data = [{
                'nama' : 'selmaet DELETE',
                'pekerjaan' : 'polisi dunia',
                'usia' : '10',
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    return make_response(jsonify({'data': data}), 200)

app.run()
