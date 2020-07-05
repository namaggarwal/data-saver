import unittest
from unittest.mock import MagicMock, patch
from datasaver import DataSaver
from datasaver.parser import Parser
from datasaver.extractor import Extractor, ExtractorFactory
from datasaver.service import Service


class TestDataSaver(unittest.TestCase):

    def test_save_success(self):
        p = Parser()
        df = [
            {
                "id": 1,
                "url": "naman"
            }
        ]
        p.parse = MagicMock(return_value=df)

        ext = Extractor()
        ext.extract = MagicMock(return_value="abc")

        e = ExtractorFactory()
        e.getExtractor = MagicMock(return_value=ext)

        s = Service()
        s.getEvent = MagicMock(return_value={"id": 1})
        s.updateEvent = MagicMock()

        ds = DataSaver(p, e, s)
        ds.save("path")

        p.parse.assert_called_with("path")
        e.getExtractor.assert_called_with("naman")

    def test_save(self):

        ds = DataSaver(None, None, None)
        ret = ds.sum(2, 2)
        self.assertEqual(4, ret)

        ret = ds.sum(3, 2)
        self.assertEqual(5, ret)

        ret = ds.sum(0, 2)
        self.assertEqual(2, ret)
