import random
import threading
import datetime
from csv import writer

import firebase_admin
from firebase_admin import credentials, firestore

cred_testapi = credentials.Certificate("girlmantra-beta.json")
ini_testapi = firebase_admin.initialize_app(cred_testapi, name="girlmantra_beat_testapi")
testapi_db = firestore.client(ini_testapi)

class testGet():

    def __init__(self, serializer):
        self.test_id = serializer.data['test_id']

    def read_from_fb1(self):
        doc_ref = testapi_db.collection("test_data").document(self.test_id)
        doc = doc_ref.get()
        if doc.exists:
            try:
                dict = doc.to_dict()
                self.return_data = dict
                self.return_data['return_type'] = "success"
            except:
                self.return_data = {
                    "return_type": "error",
                    "error": "Class: testGet - Function: read_from_fb1 - Error - fb read"
                }
        else:
            self.return_data = {
                "return_type": "error",
                "error": "Class: testGet - Function: read_from_fb1 - Error - not exists"
            }


    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.read_from_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except Exception as e:
            return_data = {
                "return_type": "error",
                "error": "Class: testGet - Thread - 1 ",
                "exception": e
            }
            return return_data


class testPost():

    def __init__(self, serializer):
        self.serializer = serializer

    def calculate_time(self):
        self.now = datetime.datetime.now()
        self.datestr = self.now.strftime("%d-%m-%y-[%H:%M:%S:%f]")
        self.id = self.now.strftime("%d%m%y%H%M%S%f") + str(random.randint(1000, 9999))


    def save_to_fb1(self):
        doc_ref1 = testapi_db.collection("test_data").document(self.id)
        data1 = {
            "name": self.serializer.data['name'],
            "email": self.serializer.data['email'],
            "mobile": self.serializer.data['mobile'],
            "value1": self.serializer.data['value1'],
            "value2": self.serializer.data['value2'],
            "date_str": self.datestr,
            "date": self.now
        }
        try:
            doc_ref1.update(data1)
        except:
            doc_ref1.set(data1)

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.calculate_time)
            t1.start()
            t1.join()
        except Exception as e:
            return_data = {
                "return_type": "error",
                "error": "Class: testGet - Thread - 1 ",
                "exception": e
            }
            return return_data

        # Thread 2
        try:
            t2 = threading.Thread(target=self.save_to_fb1)
            t2.start()
            t2.join()

            return_data = {
                "return_type": "success",
                "database_type": self.serializer.data['database_type'],
                "firebase": "girlmantra-" + self.serializer.data['database_type'],
                "name": self.serializer.data['name'],
                "email": self.serializer.data['email'],
                "mobile": self.serializer.data['mobile'],
                "value1": self.serializer.data['value1'],
                "value2": self.serializer.data['value2'],
                "date": self.datestr,
                "test_id": self.id
            }

            return return_data

        except Exception as e:
            return_data = {
                "return_type": "error",
                "error": "Class: testGet - Thread - 2 ",
                "exception": e
            }
            return return_data


class testDelete():

    def __init__(self, serializer):
        self.test_id = serializer.data['test_id']

    def delete_fb(self):
        try:
            testapi_db.collection("test_data").document(self.test_id).delete()
            self.return_data = {
                "return_type": "success",
                "test_id": self.test_id
            }
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: testDelete - Function:delete_fb - error: fb delete "
            }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.delete_fb)
            t1.start()
            t1.join()
            return self.return_data
        except Exception as e:
            return_data = {
                "return_type": "error",
                "error": "Class: testDelete - Thread 1 ",
                "exception": e
            }
            return return_data


class testPut():

    def __init__(self, serializer):
        self.serializer = serializer

    def update_fb(self):
        try:
            doc_ref = testapi_db.collection("test_data").document(self.serializer.data['test_id'])
            data = {
                "name": self.serializer.data["name"],
                "email": self.serializer.data["email"],
                "mobile": self.serializer.data["mobile"]
            }
            doc_ref.update(data)
            self.return_data = self.serializer
            self.return_data['return_type'] = "success"
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: testPut - Function:update_fb - error: fb update "
            }
    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.update_fb)
            t1.start()
            t1.join()
            return self.return_data
        except Exception as e:
            return_data = {
                "return_type": "error",
                "error": "Class: testPut - Thread 1 ",
                "exception": e
            }
            return return_data