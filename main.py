from chest_cancer_project import logger
from chest_cancer_project.pipeline.stage_01_data_ingestion import  DataIngestionTrainingPipeline
from chest_cancer_project.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline 
STAGE_NAME="data_ingestion "


try:
    logger.info(f">>>>> stage{STAGE_NAME} started <<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e) 
    raise e   



STAGE_NAME ="Prepare base model"

try:
    logger.info(f">>>>> stage{STAGE_NAME} started <<<<<")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")
except Exception as e:
    logger.exception(e)
    raise e    
