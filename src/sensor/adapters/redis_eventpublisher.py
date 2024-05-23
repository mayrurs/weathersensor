import json
import redis 
import logging

from dataclasses import asdict

from sensor import config

logger = logging.getLogger(__name__)

r = redis.Redis(**config.get_redis_host_and_port())

def publish(channel, message: dict):
    logging.debug(f"publishing: channel={channel}, message={message}")
    r.publish(channel, json.dumps(message.to_dict()))


