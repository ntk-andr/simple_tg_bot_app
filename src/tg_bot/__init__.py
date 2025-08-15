# import logging
# from core.logger_wrapper import LoggerWrapper
# from settings import settings

# DATE_FORMAT = settings.DATE_FORMAT
# LOG_FORMAT = settings.LOG_FORMAT
# LOG_LEVEL = logging.INFO
# LOG_LEVEL = settings.LOG_LEVEL

# logging.basicConfig(
#     format=LOG_FORMAT, datefmt=DATE_FORMAT,
#     level=LOG_LEVEL
# )
# logger = logging.getLogger(__name__)


from tg_bot.bot import main
