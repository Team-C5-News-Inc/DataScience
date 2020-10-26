import pymongo
import logging
from client import client, db
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

print(client)