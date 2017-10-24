import logging

logging.basicConfig(filename='test.log', filemode='w', level=logging.INFO)
logging.info('Started')
logging.info('Finished')