import pickle
import jsonpickle


class PersistenciaMascotas():


    @classmethod
    def save(cls, mascota):
        binary_open = open("files/" + str(mascota.id) + '.gui', mode='wb')
        pickle.dump(mascota, binary_open)
        binary_open.close()

    @classmethod
    def load(cls, file_name):
        binary_open = open("files/" + file_name, mode='rb')
        mascota = pickle.load(binary_open)
        binary_open.close()
        return mascota

    @classmethod
    def save_json(cls, mascota):
        text_open = open("files/" + str(mascota.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(mascota)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        mascota = jsonpickle.decode(json_gui)
        text_open.close()
        return mascota


