import unittest
from streamshift.stream import *



class StreamTest(unittest.TestCase):

    def test_buffer_listen_purge(self):
        stream = Stream(
            "http://stream3.polskieradio.pl:8904/",
            ChunkManager(
                "./data/",
                "http://stream3.polskieradio.pl:8904/"
            )
        )
#        stream.buffer()
        t = time.time()
