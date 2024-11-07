from flask import Flask
from jinja2.utils import F
from routes.log_eqto import log_eqto_route
from routes.Ctr_Eqto import Ctr_Eqto_route
from routes.Carr_Img import Carr_Img_route
from gevent.pywsgi import WSGIServer
import os

 
app = Flask(__name__)

UPLOAD_FOLDER_CERT = '/static/certificados'

app.config['UPLOAD_FOLDER_CERT'] = UPLOAD_FOLDER_CERT

app.register_blueprint(log_eqto_route, url_prefix="/")
app.register_blueprint(Ctr_Eqto_route, url_prefix="/Ctr_Eqto")
app.register_blueprint(Carr_Img_route, url_prefix="/Carr_Img")


if __name__ == "__main__":
    # Debug/Development
    port = int(os.getenv('PORT','5000'))
    app.run(host='0.0.0.0', port = port)
    # Production
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    
 
    