import logging
import logging.config

logging.config.fileConfig('log.conf')

logger = logging.getLogger('Test_Logger')

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
logger.error('error message')
logger.error('error message')
logger.error('error message')
