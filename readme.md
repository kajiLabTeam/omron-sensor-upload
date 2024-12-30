# 参考にしたサイト

https://qiita.com/Toshiaki0315/items/aa43e78c024bb900ef53



# プログラムを書き換えた後に動作を反映させる方法
```bash
sudo systemctl restart omron_sensor.service
```


# サービス化をする方法

以下のファイルを`/etc/systemd/system/omron_sensor.service`に書き込む

```service:/etc/systemd/system/omron_sensor.service
[Unit]
Description=Omron Sensor Service
After=network.target
StartLimitIntervalSec=60  # 再起動試行の時間枠（秒）
StartLimitBurst=5         # 指定時間内での最大再起動回数

[Service]
ExecStart=/usr/bin/python3 /home/harutiro/omron-sensor-upload/main.py
Restart=always # 常に再起動
RestartSec=5    # 再起動前に5秒待機
User=harutiro
WorkingDirectory=/home/harutiro/omron-sensor-upload

[Install]
WantedBy=multi-user.target
```

その後以下のコマンドを実行して、動作を開始する

```bash
sudo systemctl enable omron_sensor.service
sudo systemctl start omron_sensor.service
```