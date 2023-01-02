import unittest
import mta_processor
import gtfs_realtime_pb2

class TestMTAProcessor(unittest.TestCase):
    def test_find_stop_on_ace_empty(self):
        no_stops = mta_processor.find_stop_on_ace(feed="",target_stop_id="A44N")
        self.assertEqual(no_stops,[])
    
    def test_find_stop_on_ace_results(self):
        feed = gtfs_realtime_pb2.FeedMessage()
        test_file = open("test-data/example-ace-results","rb")
        example_feed = test_file.read()
        test_file.close()
        feed.ParseFromString(example_feed)
        print(feed)
        four_stops = mta_processor.find_stop_on_ace(feed=feed, target_stop_id="A44N")
        self.assertEqual(four_stops,[])


if __name__ == '__main__':
    unittest.main()