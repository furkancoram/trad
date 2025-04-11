# Real-Time Financial Charting App

## 🧠 Ne İşe Yarar?
Gerçek zamanlı fiyat ve hacim verilerini grafiklerle gösteren bir web uygulaması. BTC/USDT gibi sembollerin fiyatlarını canlı olarak takip edebilirsin.

## ⚙️ Kurulum

### 1. Backend (Python)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
redis-server  # Redis çalışıyor olmalı
python app.py
