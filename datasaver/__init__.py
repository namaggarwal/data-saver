from datasaver.parser import ExcelParser
from datasaver.extractor import ExtractorFactory
from datasaver.service import DataSaverService, DataArchiver
from sqlalchemy import create_engine


def save(path):
    excelParser = ExcelParser()
    extractorFactory = ExtractorFactory()
    dataArchiver = DataArchiver()
    engine = create_engine(
        'mysql+mysqlconnector://root@localhost:3306/library')
    conn = engine.connect()
    dataService = DataSaverService(dataArchiver, conn)
    ds = DataSaver(excelParser, extractorFactory, dataService)
    ds.save(path)


class DataSaver(object):

    def __init__(self, parser, extractorFactory, service):
        self.parser = parser
        self.extractorFactory = extractorFactory
        self.service = service

    def save(self, path):
        df = self.parser.parse(path)
        for df_row in df:
            # url = df_row["url"]
            # extractor = self.extractorFactory.getExtractor(url)
            # text = extractor.extract(url)
            # df_row["text"] = text
            row = self.service.getEvent(df_row["id"])

            if row:
                self.service.updateEvent(df_row)
                return

            self.service.insertEvent(df_row)

    def sum(self, a, b):
        return a + b
