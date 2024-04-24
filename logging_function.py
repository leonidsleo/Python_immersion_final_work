import logging

logging.basicConfig(filename='your_directory.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(' Описание директории - ')

def logger_in_fail(log_directory):
    """
    функция логирования 
    """
    for log in log_directory:
        logger.info(log)
    return log