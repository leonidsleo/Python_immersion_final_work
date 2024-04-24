import argparse
from object_search_function import checking_object
from logging_function import logger_in_fail

parser = argparse.ArgumentParser(description="Путьк нашей директории")
parser.add_argument('-a', metavar='a', help="Необходимо указать путь до директории")

args = parser.parse_args()
print(args)

log_directory = checking_object(args.a)
logger_in_fail(log_directory)

r"""
команда для запуска в терминале:
python .\final_task.py -a C:\Users\LyonR\Documents\Обучение\26_26_Погружение_в_python
python .\final_task.py -a C:\Users\LyonR\Documents\Обучение\26_26_Погружение_в_python\cod 
"""