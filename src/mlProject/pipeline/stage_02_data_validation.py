from mlProject.config.configuration import DataValidationConfigurationManager
from mlProject.components.data_validation import DataValiadtion
from mlProject import logger


STAGE_NAME = 'Data Validation Stage '


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = DataValidationConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e