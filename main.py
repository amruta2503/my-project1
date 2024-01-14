from source.entity.config_entity import TrainingPipelineConfig
from source.utility.utility import generate_global_timestamp
from source.logger import setuplogger
from source.logger import logging
from source.pipeline.train_pipeline import TrainPipeline

if __name__ == '__main__':

    global_timestamp = generate_global_timestamp()

    setuplogger(global_timestamp)
    logging.info("Logger setup is complete")

    #train_pipeline_config_obj = TrainingPipelineConfig()
    #print(train_pipeline_config_obj.__dict__)

    train_pipeline_obj = TrainPipeline(global_timestamp)
    train_pipeline_obj.run_train_pipeline()