
import requests
import time
import aiohttp
import asyncio
import json

from features.Sensor.Entity.SensorData import SensorData

class HttpApi:
    def __init__(self):
        self.url = "https://enviroment-backend.kajilab.dev"
        # self.url = "https://sensor-api.sysken.net"
        # self.url = "http://192.168.101.65:3000"

    async def post(self, data: SensorData) -> int:
        headers = {
            'Content-Type': 'application/json'
        }
        
        # データをJSONに変換
        json_data = json.dumps(data.to_json())
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=json_data, headers=headers) as response:
                if response.status != 200:
                    print("Non-200 status code received:", response.status)
                    print("Response body:", await response.text())
                return response.status
