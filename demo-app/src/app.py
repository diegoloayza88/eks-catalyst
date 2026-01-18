from flask import Flask, jsonify, request
import os
import socket
import datetime
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'EKS Catalyst Demo Application',
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'version': os.getenv('APP_VERSION', '1.0.0')
    })


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat()
    }), 200


@app.route('/ready')
def ready():
    return jsonify({
        'status': 'ready',
        'timestamp': datetime.datetime.now().isoformat()
    }), 200


@app.route('/info')
def info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return jsonify({
        'hostname': hostname,
        'ip_address': ip_address,
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'timestamp': datetime.datetime.now().isoformat()
    })


@app.route('/metrics')
def metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return jsonify({
        'cpu_percent': cpu_percent,
        'memory': {
            'total': memory.total,
            'available': memory.available,
            'percent': memory.percent
        },
        'disk': {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': disk.percent
        },
        'timestamp': datetime.datetime.now().isoformat()
    })


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        'received': data,
        'timestamp': datetime.datetime.now().isoformat()
    })


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)


