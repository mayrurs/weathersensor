from . import redis_client

from tenacity import Retrying, RetryError, stop_after_delay

import time
import logging

from sensor.adapters import redis_eventpublisher
from sensor.domain import sensors

sensor = sensors.FakeSensor(
    values = [12, 14],
    timestamps = ["2023-12-12 12:00:00", "2023-12-12 12:00:01"],
    )
channel = "sensor_stream"

for _ in range(1):
    result = sensor.read()
    redis_eventpublisher.publish(channel, result)
    time.sleep(0.5)

     # wait until we see a message saying the order has been reallocated
    messages = []
    for attempt in Retrying(stop=stop_after_delay(3), reraise=True):
        with attempt:
            message = subscription.get_message(timeout=1)
            if message:
                messages.append(message)
                print(messages)
            data = json.loads(messages[-1]["data"])
            assert data["orderid"] == orderid
            assert data["batchref"] == later_batch



