import dataclasses
from typing import Any, Dict

@dataclasses.dataclass
class SensorData:
    time_measured: str = ""
    area_id: int = 1
    temperature: float = 0.0
    relative_humidity: float = 0.0
    ambient_light: int = 0
    barometric_pressure: float = 0.0
    sound_noise: float = 0.0
    eTVOC: int = 0
    eCO2: int = 0
    discomfort_index: float = 0.0
    heat_stroke: float = 0.0
    vibration_information: int = 0
    si_value: float = 0.0
    pga: float = 0.0
    seismic_intensity: float = 0.0
    temperature_flag: int = 0
    relative_humidity_flag: int = 0
    ambient_light_flag: int = 0
    barometric_pressure_flag: int = 0
    sound_noise_flag: int = 0
    etvoc_flag: int = 0
    eco2_flag: int = 0
    discomfort_index_flag: int = 0
    heat_stroke_flag: int = 0
    si_value_flag: int = 0
    pga_flag: int = 0
    seismic_intensity_flag: int = 0

    @staticmethod
    def get_header() -> str:
        return "time_measured,area_id,temperature,relative_humidity,ambient_light,barometric_pressure,sound_noise,eTVOC,eCO2,discomfort_index,heat_stroke,vibration_information,si_value,pga,seismic_intensity,temperature_flag,relative_humidity_flag,ambient_light_flag,barometric_pressure_flag,sound_noise_flag,etvoc_flag,eco2_flag,discomfort_index_flag,heat_stroke_flag,si_value_flag,pga_flag,seismic_intensity_flag\n"

    def to_csv(self) -> str:
        return f"{self.time_measured},{self.area_id},{self.temperature},{self.relative_humidity},{self.ambient_light},{self.barometric_pressure},{self.sound_noise},{self.eTVOC},{self.eCO2},{self.discomfort_index},{self.heat_stroke},{self.vibration_information},{self.si_value},{self.pga},{self.seismic_intensity},{self.temperature_flag},{self.relative_humidity_flag},{self.ambient_light_flag},{self.barometric_pressure_flag},{self.sound_noise_flag},{self.etvoc_flag},{self.eco2_flag},{self.discomfort_index_flag},{self.heat_stroke_flag},{self.si_value_flag},{self.pga_flag},{self.seismic_intensity_flag}\n"
    
    def to_json(self) -> Dict[str, Any]:
        return {
            "area_id": self.area_id,
            "time_measured": self.time_measured,
            "area_id": self.area_id,
            "temperature": self.temperature,
            "relative_humidity": self.relative_humidity,
            "ambient_light": self.ambient_light,
            "barometric_pressure": self.barometric_pressure,
            "sound_noise": self.sound_noise,
            "eTVOC": self.eTVOC,
            "eCO2": self.eCO2,
            "discomfort_index": self.discomfort_index,
            "heat_stroke": self.heat_stroke,
            "vibration_information": self.vibration_information,
            "si_value": self.si_value,
            "pga": self.pga,
            "seismic_intensity": self.seismic_intensity,
            "temperature_flag": self.temperature_flag,
            "relative_humidity_flag": self.relative_humidity_flag,
            "ambient_light_flag": self.ambient_light_flag,
            "barometric_pressure_flag": self.barometric_pressure_flag,
            "sound_noise_flag": self.sound_noise_flag,
            "etvoc_flag": self.etvoc_flag,
            "eco2_flag": self.eco2_flag,
            "discomfort_index_flag": self.discomfort_index_flag,
            "heat_stroke_flag": self.heat_stroke_flag,
            "si_value_flag": self.si_value_flag,
            "pga_flag": self.pga_flag,
            "seismic_intensity_flag": self.seismic_intensity_flag
        }