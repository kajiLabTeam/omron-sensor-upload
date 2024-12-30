from features.Sensor.Repository.SensorRepository import SensorRepository
import asyncio
import sys
import signal

async def stop_service(sensorRepository):
    """サービスを停止するための非同期処理"""
    await sensorRepository.sensorApi.clear_led()
    print("SIGTERM received, cleaning up...")
    sys.exit(0)

def main():
    try:
        sensorRepository = SensorRepository()

        # シグナルハンドラーの設定
        def signal_handler(signum, frame):
            """SIGTERMを受け取った時に呼ばれる"""
            asyncio.create_task(stop_service(sensorRepository))

        signal.signal(signal.SIGTERM, signal_handler)

        # メイン処理
        asyncio.run(sensorRepository.get_sensor())

    except KeyboardInterrupt:
        sys.exit()

    except asyncio.CancelledError:
        sys.exit()

    except Exception as e:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
