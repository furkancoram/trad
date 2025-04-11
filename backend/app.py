import os
import time
import threading
from flask import Flask
from flask_cors import CORS
from flask_sse import sse
from data_feed import get_realtime_data

app = Flask(__name__)
CORS(app)

# Redis bağlantı ayarı (Render için)
app.config['REDIS_URL'] = os.environ.get('REDIS_URL')
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return 'Real-time Financial Chart Backend'

# Gerçek zamanlı veriyi SSE ile frontend'e yollayan thread
def push_data():
    while True:
        try:
            data = get_realtime_data("BTCUSDT")  # Coin sembolü burada sabit, istersen kullanıcıya açarız
            sse.publish({"price": data['price'], "volume": data['volume']}, type='update')
            print(f"Gönderildi: {data}")  # Debug log
            time.sleep(2)  # 2 saniyede bir güncelle
        except Exception as e:
            print(f"[HATA] Veri gönderiminde sorun: {e}")
            time.sleep(5)

if __name__ == '__main__':
    threading.Thread(target=push_data).start()
    port = int(os.environ.get("PORT", 10000))  # Render sunucusu buradan portu belirliyor
    app.run(debug=True, threaded=True, host='0.0.0.0', port=port)
