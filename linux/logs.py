import logging

def logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.getLogger(__name__)
    logging.debug("Program debuged by user")
    logging.info("Program info")
    logging.warning("Program warning")
    logging.error("Program error")
    logging.critical("Program critical")
    
