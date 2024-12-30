run:
	python main.py

service_start:
	sudo systemctl start omron_sensor.service

service_restart:
	sudo systemctl restart omron_sensor.service

service_stop:
	sudo systemctl stop omron_sensor.service

service_status: 
	sudo systemctl status omron_sensor.service
