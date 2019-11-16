from flask import Flask

app = Flask(__name__)

if app.config['ENV'] == 'development':
    # Entrar al archivo "config" y levantar la configuración del objeto "DevelopmentConfig"
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.ProductionConfig')

from app import views
from app import admin_views

for k,v in app.config.items():
    print(k, str(v))
