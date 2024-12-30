
import time
from Utils.CSVFileStorage import CSVFileStorage
from Utils.DateUtils import DateUtils
from features.Sensor.Api.SensorApi import SensorApi
from features.Sensor.Entity.SensorData import SensorData
from features.http.Api.HttpApi import HttpApi
import signal
import asyncio


class SensorRepository:
    def __init__(
        self,
        sensorApi: SensorApi = SensorApi(),
        # csvFileStorage: CSVFileStorage = CSVFileStorage(DateUtils.now_utc_str() + ".csv", SensorData.get_header()),
        httpApi: HttpApi = HttpApi()
    ):
        self.sensorApi = sensorApi
        # self.csvFileStorage = csvFileStorage
        self.httpApi = httpApi
        self.new_file_created = False

        # SIGTERMが起きた時に着火させる
        signal.signal(signal.SIGTERM, self.termed)

    # systemctl stop を起こした時に止める用のコード
    def termed(self, signum, frame):
        self.sensorApi.clear_led()

        print("SIGTERM!")
        sys.exit(0)
    
    async def dataUpload(self, data: SensorData) -> None:
        
        
        self.sensorApi.set_led(
            r=0,
            g=255,
            b=0
        )
    
        # self.csvFileStorage.save(data.to_csv())
        # TODO: area_idをセットする
        data.area_id = 1 
        print("アップロードしようとするよ")
        print(data)
        self.httpApi.post(data)

        self.sensorApi.set_led(
            r=0,
            g=255,
            b=255
        )

    def get_sensor(self) -> None:

        try: 
            self.sensorApi.set_led(
                r=0,
                g=255,
                b=255
            )

            data = self.sensorApi.get_sensor_data(self.dataUpload)

            # # 新しいファイルを作成するかどうかの判定
            # current_minute = DateUtils.now_utc().minute
            # current_second = DateUtils.now_utc().second

            # if current_minute == 0 and current_second == 0 and not self.new_file_created:
            #     self.csvFileStorage = CSVFileStorage(DateUtils.now_utc_str() + ".csv", SensorData.get_header())
            #     self.new_file_created = True
            # elif current_minute != 0 or current_second != 0:
            #     self.new_file_created = False
        
        except KeyboardInterrupt:
            self.sensorApi.clear_led()
        
        except: 
            import traceback
            traceback.print_exc()

            self.sensorApi.set_led(
                r=255,
                g=0,
                b=0
            )
            

