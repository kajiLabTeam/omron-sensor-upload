from features.Sensor.Repository.SensorRepository import SensorRepository
import asyncio
import sys

if __name__ == "__main__":

    try:
        sensorRepository = SensorRepository()
        asyncio.run(sensorRepository.get_sensor())

    except KeyboardInterrupt:
        sys.exit()

    except asyncio.CancelledError:
        sys.exit()

    except: 
        import traceback
        traceback.print_exc()
