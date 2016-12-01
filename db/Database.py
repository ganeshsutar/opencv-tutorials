import MySQLdb as mysql
import logging

class Database:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.db = None

    def connect(self):
        self.close()
        self.db = mysql.connect(self.host, self.user, self.password, self.dbname)

    def close(self):
        if(self.db != None):
            self.db.close()
        self.db = None

    def addPerson(self, person_name):
        logging.debug('Adding person %s', person_name)
        sql = "INSERT INTO persons VALUES (default, '%s')" % (person_name)
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        cursor.close()

    def addImage(self, person_id, image_path):
        logging.debug('Adding image %d => %s', person_id, image_path)
        sql = "INSERT INTO person_faces VALUES(default, %d, '%s')" % (person_id, image_path)
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        cursor.close()

    def getPersons(self):
        logging.debug('Getting list of persons')
        sql = "SELECT id, name FROM persons"
        cursor = self.db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        persons = {}
        for row in results:
            persons[row[0]] = row[1]
        return persons

    def getImages(self, person_id):
        logging.debug('Getting images for person %d', person_id)
        sql = "SELECT image_path FROM person_faces WHERE person_id = %d" % (person_id)
        cursor = self.db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        images = []
        for row in results:
            images.append(row[0])
        return images
