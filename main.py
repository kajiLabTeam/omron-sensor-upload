from features.Sensor.Repository.SensorRepository import SensorRepository
import asyncio

if __name__ == "__main__":
    sensorRepository = SensorRepository()
    asyncio.run(sensorRepository.get_sensor())
