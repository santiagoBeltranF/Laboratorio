
import waitress
from infraestructura.PersistenciaPerros import PersistenciaPerros
import json

import falcon
from falcon import API


class HolaMundo():

    def on_get(self, req, resp, uuid):
        db = PersistenciaPerros()
        gui = db.load_json_perro(uuid + '.json')
        mensajes = ['Hola Mindo', 'Hola Que hace', 'Adio', 'Ciao', '2+2=4']
        resp.body = json.dumps(gui.__dict__)
        resp.status = falcon.HTTP_OK


def iniciar() -> API:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = API()
    api.add_route("/perro/{uuid}", HolaMundo())

    return api


app = iniciar()

if __name__ == "__main__":
    waitress.serve(app, port=8081, url_scheme="http")
