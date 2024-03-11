import serial
import time
import sys
from Utils.DateUtils import DateUtils

from features.Sensor.Entity.SensorData import SensorData

class SensorApi:
    # LED display rule. Normal Off.
    DISPLAY_RULE_NORMALLY_OFF = 0

    # LED display rule. Normal On.
    DISPLAY_RULE_NORMALLY_ON = 1

    def s16(self,value:int) -> int:
        return -(value & 0x8000) | (value & 0x7fff)

    def calc_crc(self,buf:bytearray, length:int) -> bytearray:
        """
        CRC-16 calculation.

        """
        crc = 0xFFFF
        for i in range(length):
            crc = crc ^ buf[i]
            for i in range(8):
                carrayFlag = crc & 1
                crc = crc >> 1
                if (carrayFlag == 1):
                    crc = crc ^ 0xA001
        crcH = crc >> 8
        crcL = crc & 0x00FF

        return (bytearray([crcL, crcH]))


    def print_latest_data(self,data:bytes) -> SensorData:
        """
        print measured latest value.
        """
        time_measured = str(DateUtils.now_timestamp())
        temperature = self.s16(int(hex(data[9]) + '{:02x}'.format(data[8], 'x'), 16)) / 100
        relative_humidity = int(hex(data[11]) + '{:02x}'.format(data[10], 'x'), 16) / 100
        ambient_light = int(hex(data[13]) + '{:02x}'.format(data[12], 'x'), 16)
        barometric_pressure = int(hex(data[17]) + '{:02x}'.format(data[16], 'x') + '{:02x}'.format(data[15], 'x') + '{:02x}'.format(data[14], 'x'), 16) / 1000
        sound_noise = int(hex(data[19]) + '{:02x}'.format(data[18], 'x'), 16) / 100
        eTVOC = int(hex(data[21]) + '{:02x}'.format(data[20], 'x'), 16)
        eCO2 = int(hex(data[23]) + '{:02x}'.format(data[22], 'x'), 16)
        discomfort_index = int(hex(data[25]) + '{:02x}'.format(data[24], 'x'), 16) / 100
        heat_stroke = self.s16(int(hex(data[27]) + '{:02x}'.format(data[26], 'x'), 16)) / 100
        vibration_information = int(hex(data[28]), 16)
        si_value = int(hex(data[30]) + '{:02x}'.format(data[29], 'x'), 16) / 10
        pga = int(hex(data[32]) + '{:02x}'.format(data[31], 'x'), 16) / 10
        seismic_intensity = int(hex(data[34]) + '{:02x}'.format(data[33], 'x'), 16) / 1000
        temperature_flag = int(hex(data[36]) + '{:02x}'.format(data[35], 'x'), 16)
        relative_humidity_flag = int(hex(data[38]) + '{:02x}'.format(data[37], 'x'), 16)
        ambient_light_flag = int(hex(data[40]) + '{:02x}'.format(data[39], 'x'), 16)
        barometric_pressure_flag = int(hex(data[42]) + '{:02x}'.format(data[41], 'x'), 16)
        sound_noise_flag = int(hex(data[44]) + '{:02x}'.format(data[43], 'x'), 16)
        etvoc_flag = int(hex(data[46]) + '{:02x}'.format(data[45], 'x'), 16)
        eco2_flag = int(hex(data[48]) + '{:02x}'.format(data[47], 'x'), 16)
        discomfort_index_flag = int(hex(data[50]) + '{:02x}'.format(data[49], 'x'), 16)
        heat_stroke_flag = int(hex(data[52]) + '{:02x}'.format(data[51], 'x'), 16)
        si_value_flag = int(hex(data[53]), 16)
        pga_flag = int(hex(data[54]), 16)
        seismic_intensity_flag = int(hex(data[55]), 16)

        return SensorData(
            time_measured=time_measured,
            temperature=temperature,
            relative_humidity=relative_humidity,
            ambient_light=ambient_light,
            barometric_pressure=barometric_pressure,
            sound_noise=sound_noise,
            eTVOC=eTVOC,
            eCO2=eCO2,
            discomfort_index=discomfort_index,
            heat_stroke=heat_stroke,
            vibration_information=vibration_information,
            si_value=si_value,
            pga=pga,
            seismic_intensity=seismic_intensity,
            temperature_flag=temperature_flag,
            relative_humidity_flag=relative_humidity_flag,
            ambient_light_flag=ambient_light_flag,
            barometric_pressure_flag=barometric_pressure_flag,
            sound_noise_flag=sound_noise_flag,
            etvoc_flag=etvoc_flag,
            eco2_flag=eco2_flag,
            discomfort_index_flag=discomfort_index_flag,
            heat_stroke_flag=heat_stroke_flag,
            si_value_flag=si_value_flag,
            pga_flag=pga_flag,
            seismic_intensity_flag=seismic_intensity_flag
        )
    

    def set_led(self, ser:serial.Serial , r:int, g:int, b:int) -> None:
        # LED On. Color of Green.
        command = bytearray([0x52, 0x42, 0x0a, 0x00, 0x02, 0x11, 0x51, self.DISPLAY_RULE_NORMALLY_ON, 0x00, r, g, b])
        command = command + self.calc_crc(command, len(command))
        ser.write(command)
        time.sleep(0.1)
        ser.read(ser.in_waiting)

    def clear_led(self, ser:serial.Serial) -> None:
        # LED Off.
        command = bytearray([0x52, 0x42, 0x0a, 0x00, 0x02, 0x11, 0x51, self.DISPLAY_RULE_NORMALLY_OFF, 0x00, 0, 0, 0])
        command = command + self.calc_crc(command, len(command))
        ser.write(command)
        time.sleep(1)
    

    def get_sensor_data(self) -> SensorData:
        """
        Get sensor data.
        """
        # Serial.
        ser : serial.Serial = serial.Serial("/dev/ttyUSB0", 115200, serial.EIGHTBITS, serial.PARITY_NONE)

        try:
            # 緑に光らせる
            self.set_led(
                ser=ser,
                r=0,
                g=255,
                b=0
            )

            # Get Latest data Long.
            command = bytearray([0x52, 0x42, 0x05, 0x00, 0x01, 0x21, 0x50])
            command = command + self.calc_crc(command, len(command))
            ser.write(command)
            time.sleep(0.1)
            data = ser.read(ser.in_waiting)
            return self.print_latest_data(data)

        except KeyboardInterrupt:
            self.clear_led(ser)
            # script finish.
            sys.exit
            return SensorData()
