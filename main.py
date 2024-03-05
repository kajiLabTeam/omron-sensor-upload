

if __name__ == '__main__':
    # Serial.
    ser = serial.Serial("/dev/ttyUSB0", 115200, serial.EIGHTBITS, serial.PARITY_NONE)

    try:
        # LED On. Color of Green.
        command = bytearray([0x52, 0x42, 0x0a, 0x00, 0x02, 0x11, 0x51, DISPLAY_RULE_NORMALLY_ON, 0x00, 0, 255, 0])
        command = command + calc_crc(command, len(command))
        ser.write(command)
        time.sleep(0.1)
        ret = ser.read(ser.inWaiting())

        while ser.isOpen():
            # Get Latest data Long.
            command = bytearray([0x52, 0x42, 0x05, 0x00, 0x01, 0x21, 0x50])
            command = command + calc_crc(command, len(command))
            tmp = ser.write(command)
            time.sleep(0.1)
            data = ser.read(ser.inWaiting())
            print_latest_data(data)
            time.sleep(1)

    except KeyboardInterrupt:
        # LED Off.
        command = bytearray([0x52, 0x42, 0x0a, 0x00, 0x02, 0x11, 0x51, DISPLAY_RULE_NORMALLY_OFF, 0x00, 0, 0, 0])
        command = command + calc_crc(command, len(command))
        ser.write(command)
        time.sleep(1)
        # script finish.
        sys.exit
