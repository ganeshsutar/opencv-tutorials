from Database import *
import config
import logging

host = config.props['datasource.host']
username = config.props['datasource.username']
password = config.props['datasource.password']
database = config.props['datasource.database']

logging.debug('Connecting database host=%s, username=%s, database=%s', host, username, database)
conn = Database(host, username, password, database)
conn.connect()
logging.debug('Connected to database')
