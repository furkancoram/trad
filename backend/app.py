import os
import time
import threading
from flask import Flask
from flask_cors import CORS
from flask_sse import sse
from data_feed import get_realtime_data

app = Flask(__name__)
CORS(app)

# Redis bağlantısı
app.config['REDIS_URL'] = os.environ.get('REDIS_URL')
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return 'Real-time Financial Chart Backend'

# Arka planda veri gönderen thread
def push_data():
    while True:
        try:
            data = get_realtime_data("BTCUSDT")  # Sembol istersen dinamik yaparız
            sse.publish({"price": data['price'], "volume": data['volume']}, type='update')
            time.sleep(2)
        except Exception as e:
            print(f"Veri gönderilirken hata oluştu: {e}")
            time.sleep(5)

if __name__ == '__main__':
    threading.Thread(target=push_data).start()
    port = int(os.environ.get("PORT", 5000))  # Render ortamı için PORT değişkeni
    app.run(debug=True, threaded=True, host='0.0.0.0', port=port)
