
import requests

from features.Sensor.Entity.SensorData import SensorData

class HttpApi:
    def __init__(self):
        self.url = "https://sensor-api.sysken.net"

    def post(self, data:SensorData) -> requests.Response:
        return requests.post(self.url + "/set/sensor", data.to_json())