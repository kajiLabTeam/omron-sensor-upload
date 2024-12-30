
import requests

from features.Sensor.Entity.SensorData import SensorData

class HttpApi:
    def __init__(self):
        self.url = "https://enviroment-backend.kajilab.dev"
        # self.url = "https://sensor-api.sysken.net"
        # self.url = "http://192.168.101.65:3000"

    async def post(self, data:SensorData) -> requests.Response:
        response = requests.post(self.url + "/set/sensor",json=data.to_json())
        if response.status_code != 200:
            print("Non-200 status code received:", response)
            print("Response body:", response.text)
        return response
