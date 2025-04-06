from chest_cancer_project import logger
from chest_cancer_project.pipeline.stage_01_data_ingestion import STAGE_NAME, DataIngestionTrainingPipeline
STAGE_NAME="data_ingestion "

try:
    logger.info(f">>>>> stage{STAGE_NAME} started <<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e) 
    raise e   