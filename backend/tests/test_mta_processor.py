import unittest
from mta_flask import mta_processor
from mta_flask.proto import gtfs_realtime_pb2
from datetime import datetime, timedelta
import os


class TestMTAProcessor(unittest.TestCase):
    def test_find_stop_on_ace_empty(self):
        no_stops = mta_processor.find_stop_on_ace(feed="", target_stop_id="A44N")
        self.assertEqual(no_stops, [])

    def test_find_stop_on_ace_results(self):
        feed = gtfs_realtime_pb2.FeedMessage()
        test_file = open(
            os.path.join(
                os.path.dirname(__file__), "test-mock-data/example-ace-results"
            ),
            "rb",
        )
        example_feed = test_file.read()
        test_file.close()
        feed.ParseFromString(example_feed)
        seven_stops = mta_processor.find_stop_on_ace(feed=feed, target_stop_id="A44N")
        self.assertEqual(len(seven_stops), 7)

        nextStops = mta_processor.find_next_n_stop_times(seven_stops, 3)
        expectedNextStops = [
            datetime(2023, 1, 3, 20, 31, 13),
            datetime(2023, 1, 3, 20, 39, 27),
            datetime(2023, 1, 3, 20, 51),
        ]
        self.assertEqual(nextStops, expectedNextStops)

    def test_find_times_to_next_stops(self):
        now = datetime.now()
        mockNextStops = [
            now + timedelta(minutes=2, seconds=30),
            now + timedelta(minutes=10, seconds=30),
            now - timedelta(minutes=2),
        ]
        times_to_next_stop = mta_processor.find_times_to_next_stop(mockNextStops)
        self.assertEqual(times_to_next_stop, [2, 10])

    def test_find_times_to_next_stops_none(self):
        now = datetime.now()
        mockNextStops = [now - timedelta(minutes=2)]
        times_to_next_stop = mta_processor.find_times_to_next_stop(mockNextStops)
        self.assertEqual(times_to_next_stop, [])

    def test_find_times_to_next_stops_zero(self):
        now = datetime.now()
        mockNextStops = [now - timedelta(seconds=30)]
        times_to_next_stop = mta_processor.find_times_to_next_stop(mockNextStops)
        self.assertEqual(times_to_next_stop, [])


if __name__ == "__main__":
    unittest.main()
