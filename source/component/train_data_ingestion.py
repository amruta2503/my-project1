import os
import pandas
from source.exception import SalesPriceException
from pymongo.mongo_client import MongoClient

class DataIngestion():

    def __init__(self,train_config):
        self.train_config = train_config

    def export_data_into_feature_store(self):
        try:
            pass
        except:
            pass

    def split_data_test_train(self):
        pass

    def initiate_data_ingestion(self):
        self.export_data_into_feature_store()
        self.split_data_test_train()