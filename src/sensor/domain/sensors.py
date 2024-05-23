import abc
import time
import board
import adafruit_dht

from typing import List
from datetime import datetime

from dataclasses import dataclass

@dataclass
class SensorData:
    sensor: str
    value: int
    timestamp: datetime

    def to_dict(self):
        return {
                "sensor": self.sensor,
                "value": self.value, 
                "timestamp": self.timestamp.strftime(r'%Y-%m-%d %H:%M:%S')
                }

class Sensor(abc.ABC):
    sensor: str

    def read(self) -> SensorData:
        return self._read()

    @abc.abstractmethod
    def _read(self):
        raise NotImplementedError


class FakeSensor(Sensor):
    def __init__(self, values: List[int] = [], timestamps: List[datetime] = []):
        self.sensor = "fake"

        if values and timestamps:
            self.sensor_data = (SensorData(self.sensor, value, timestamp) for value, timestamp in zip(values, timestamps))
        else:
            self.sensor_data = None

    def _read(self) -> SensorData:
        if self.sensor_data:
            return next(self.sensor_data, None)
        else:
            return SensorData(self.sensor, 10, datetime.now())

class Dht22(Sensor):
    def __init__(self, pin=board.D4):
        self.pin = pin
        self.sensor = adafruit_dht.DHT22(pin)

    def _read(self) -> SensorData:
        temperatue = None
        while not temperature:
            try:
                temperature = self.sensor.temperature
                SensorData('temperature', temperature, datetime.now())
            except RuntimeError as error:
                time.sleep(0.1)
                continue
            except Exception as error:
                self.sensor.exit()
                raise error
            time.sleep(0.1)

