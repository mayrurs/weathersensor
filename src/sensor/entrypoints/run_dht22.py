import time
import logging

from sensor.adapters import redis_eventpublisher
from sensor.domain import sensors

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def main():
    sensor = sensors.Dht22()
    channel = "sensor_stream"
    logger.info(f"Starting stream for sensor {sensor.sensor} on channel {channel}")
    while True:
        message = sensor.read()
        redis_eventpublisher.publish(channel, message)
        logger.debug(f"Publishing event {message}")
        time.sleep(10.0)

if __name__ == "__main__":
    main()