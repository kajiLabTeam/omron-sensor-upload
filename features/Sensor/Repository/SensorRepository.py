
import time
from Utils.CSVFileStorage import CSVFileStorage
from Utils.DateUtils import DateUtils
from features.Sensor.Api.SensorApi import SensorApi
from features.Sensor.Entity.SensorData import SensorData


class SensorRepository:
    def __init__(
        self,
        sensorApi: SensorApi = SensorApi(),
        csvFileStorage: CSVFileStorage = CSVFileStorage(DateUtils.now_utc_str() + ".csv", SensorData.get_header())
    ):
        self.sensorApi = sensorApi
        self.csvFileStorage = csvFileStorage

    def get_sensor(self) -> None:
        while True:
            data = self.sensorApi.get_sensor_data()
            self.csvFileStorage.save(data.to_csv())
            time.sleep(1)

            # 毎時間０分にファイル名を変更
            if time.localtime().tm_min == 0:
                self.csvFileStorage = CSVFileStorage(DateUtils.now_utc_str() + ".csv", SensorData.get_header())

