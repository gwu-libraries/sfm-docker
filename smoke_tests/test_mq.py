import unittest
import os
from pyrabbit.api import Client


class MqSmokeTest(unittest.TestCase):
    def setUp(self):
        self.cl = Client("mq:15672",
                         os.environ.get("SFM_RABBITMQ_USER"),
                         os.environ.get("SFM_RABBITMQ_PASSWORD"))
        self.assertTrue(self.cl.is_alive())

    def test_exchange(self):
        exchanges = self.cl.get_exchanges()
        for exchange in exchanges:
            if exchange["name"] == "sfm_exchange":
                break
        else:
            self.assertTrue(False, "Exchange not found.")

    def test_queues(self):
        queues = self.cl.get_queues()
        queues_names = {queue["name"] for queue in queues}
        # Add additional queue names as new components are added.
        self.assertTrue(queues_names.issuperset(set(["flickr_harvester",
                                                     "flickr_exporter",
                                                     "sfm_ui",
                                                     "twitter_harvester",
                                                     "twitter_rest_harvester",
                                                     "twitter_rest_harvester_priority",
                                                     "twitter_rest_exporter",
                                                     "twitter_stream_exporter",
                                                     "tumblr_harvester",
                                                     "tumblr_exporter"])))
