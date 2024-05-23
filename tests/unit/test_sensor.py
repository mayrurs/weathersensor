import pytest
from datetime import datetime
from sensor.domain import sensors

def test_read_present_value():
    values = [12, 14]
    timestamps = ["2023-12-12 12:00:00", "2023-12-12 12:00:01"]
    sensor = sensors.FakeSensor(values, [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in timestamps])

    assert sensor.current_value().value == 12
    assert sensor.current_value().value == 14

def test_read_random_value():
    sensor = sensors.FakeSensor()

    assert sensor.current_value().value == 10
