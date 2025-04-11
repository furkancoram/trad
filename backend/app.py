from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sse import sse
import threading
import time
from data_feed import get_realtime_data

app = Flask(__name__)
CORS(app)
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return 'Real-time Financial Chart Backend'

def push_data():
    while True:
        data = get_realtime_data("BTCUSDT")  # Buraya sembol seçimi ekleyebilirsin
        sse.publish({"price": data['price'], "volume": data['volume']}, type='update')
        time.sleep(2)  # Veri güncelleme aralığı

if __name__ == '__main__':
    threading.Thread(target=push_data).start()
    app.run(debug=True, threaded=True)
