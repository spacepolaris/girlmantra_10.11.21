import random
import threading
import datetime
from csv import writer

import firebase_admin
from firebase_admin import credentials, firestore

cred_registrationapi = credentials.Certificate("girlmantra-beta.json")
ini_registrationapi = firebase_admin.initialize_app(cred_registrationapi, name="girlmantra_beat_registration")
registrationapi_db = firestore.client(ini_registrationapi)

# registration_status = 1
class saveStartOnboarding():

    def __init__(self, serializer):
        self.mobile_no = serializer.data['mobile']

    def save_to_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        data = {"registration_status": 1}
        try:
            doc_ref.update(data)
            self.return_data = data
            self.return_data["return_type"] = "success"
        except:
            try:
                doc_ref.set(data)
                self.return_data = data
                self.return_data["return_type"] = "success"
            except Exception as e:
                self.return_data = {
                    "return_type": "error",
                    "error": "Class: saveStartOnboarding - Function: read_from_fb1 - Error - fb save",
                    "exception": e
                }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.save_to_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: saveStartOnboarding - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data
        
# registration_status = 2
class savePersonalInfo():
    def __init__(self, serializer):
        self.mobile_no = serializer.data['mobile']
        self.name = serializer.data['name']
        self.age = serializer.data['age']

    def save_to_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        data = {
            "registration_status": 2,
            "name": self.name,
            "age": self.age
        }
        try:
            doc_ref.update(data)
            self.return_data = data
            self.return_data["return_type"] = "success"
        except Exception as e:
            self.return_data = {
                "return_type": "error",
                "error": "Class: savePersonalInfo - Function: save_to_fb1 - Error - fb save",
                "exception": e
            }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.save_to_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: savePersonalInfo - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data

# registration_status = 3
class saveGoals():
    def __init__(self, serializer):
        self.serializer = serializer
        self.mobile_no = serializer.data['mobile']

    def create_goal_list(self):
        self.goal_list = self.serializer.data['goals'].split("#")

    def save_to_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        data = {
            "registration_status": 3,
            "goals": self.goal_list
        }
        try:
            doc_ref.update(data)
            self.return_data = data
            self.return_data["return_type"] = "success"

        except Exception as e:
            self.return_data = {
                "return_type": "error",
                "error": "Class: saveGoal - Function: save_to_fb1 - Error - fb save",
                "exception": e
            }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.create_goal_list)
            t1.start()
            t1.join()
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: saveGoals - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data
        # Thread 2
        try:
            t1 = threading.Thread(target=self.save_to_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: saveGoal - Function: start_process - Error - Thread2",
                "exception": "None"
            }
            return self.return_data

# registration_status = 4
class saveProblems():
    def __init__(self, serializer):
        self.serializer = serializer
        self.mobile_no = serializer.data['mobile']

    def create_goal_list(self):
        self.problem_list = self.serializer.data['problems'].split("#")

    def save_to_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        data = {
            "registration_status": 4,
            "problems": self.problem_list
        }
        try:
            doc_ref.update(data)
            self.return_data = data
            self.return_data["return_type"] = "success"

        except Exception as e:
            self.return_data = {
                "return_type": "error",
                "error": "Class: saveProblems - Function: save_to_fb1 - Error - fb save",
                "exception": e
            }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.create_goal_list)
            t1.start()
            t1.join()
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: saveProblems - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data
        # Thread 2
        try:
            t1 = threading.Thread(target=self.save_to_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: saveGoal - Function: start_process - Error - Thread2",
                "exception": "None"
            }
            return self.return_data

# registration_status = 5 - Registration Completed
class savePreferredTimes():
    def __init__(self, serializer):
        self.serializer = serializer
        self.mobile_no = serializer.data['mobile']

    def create_goal_list(self):
        self.preferred_time_list = self.serializer.data['preferred_time'].split("#")

    def create_registration_data(self):
        self.now = datetime.datetime.now()
        self.registration_date_str = self.now.strftime("%d-%b-%Y [%I:%M %p]")


    def save_to_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        data = {
            "registration_status": 5,
            "preferred_time": self.preferred_time_list,
            "registration_data": self.now,
            "registration_date_str": self.registration_date_str
        }
        try:
            doc_ref.update(data)
            self.return_data = data
            self.return_data["return_type"] = "success"

        except Exception as e:
            self.return_data = {
                "return_type": "error",
                "error": "Class: savePreferredTimes - Function: save_to_fb1 - Error - fb save",
                "exception": e
            }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.create_goal_list)
            t2 = threading.Thread(target=self.create_registration_data)
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: savePreferredTimes - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data
        # Thread 2
        try:
            t1 = threading.Thread(target=self.save_to_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: savePreferredTime - Function: start_process - Error - Thread2",
                "exception": "None"
            }
            return self.return_data

# Get Full User Status
class getUserFullStatus():

    def __init__(self, serializer):
        self.mobile_no = serializer.data['mobile']

    def read_from_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        doc = doc_ref.get()
        if doc.exists:
            try:
                dict = doc.to_dict()
                self.return_data = dict
                self.return_data['return_type'] = "success"
            except Exception as e:
                self.return_data = {
                    "return_type": "error",
                    "error": "Class: getUserFullStatus - Function: read_from_fb1 - Error - fb read",
                    "exception": e
                }
        else:
            self.return_data = {
                "return_type": "error",
                "error": "Class: getUserFullStatus - Function: read_from_fb1 - Error - not exists",
                "exception": None
            }


    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.read_from_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: getUserFullStatus - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data

# Get only User Registration Status
class getUserRegistrationStatusOnly():

    def __init__(self, serializer):
        self.mobile_no = serializer.data['mobile']

    def read_from_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        doc = doc_ref.get()
        if doc.exists:
            try:
                dict = doc.to_dict()
                self.return_data = {"registration_status": dict['registration_status']}
                self.return_data['return_type'] = "success"
            except Exception as e:
                self.return_data = {
                    "return_type": "error",
                    "error": "Class: getUserRegistrationStatusOnly - Function: read_from_fb1 - Error - fb read",
                    "exception": e
                }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.read_from_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: savePreferredTime - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data

# Get personal info
class getPersonalInfo():

    def __init__(self, serializer):
        self.mobile_no = serializer.data['mobile']

    def read_from_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        doc = doc_ref.get()
        if doc.exists:
            try:
                dict = doc.to_dict()
                self.return_data = {
                    "return_type": "success",
                    "name": dict['name'],
                    "age": dict['age']
                }

            except Exception as e:
                self.return_data = {
                    "return_type": "error",
                    "error": "Class: getPersonalInfo - Function: read_from_fb1 - Error - fb read",
                    "exception": e
                }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.read_from_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: getPersonalInfo - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data

# Get personal info
class getGoals():

    def __init__(self, serializer):
        self.mobile_no = serializer.data['mobile']

    def read_from_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        doc = doc_ref.get()
        if doc.exists:
            try:
                dict = doc.to_dict()
                goals = dict['goals']
                self.return_data = {
                    "return_type": "success",
                    "goals": goals
                }
            except Exception as e:
                self.return_data = {
                    "return_type": "error",
                    "error": "Class: getGoals - Function: read_from_fb1 - Error - fb read",
                    "exception": e
                }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.read_from_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: getGoals - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data

# Get problems info
class getProblems():

    def __init__(self, serializer):
        self.mobile_no = serializer.data['mobile']

    def read_from_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        doc = doc_ref.get()
        if doc.exists:
            try:
                dict = doc.to_dict()
                problems = dict['problems']
                self.return_data = {
                    "return_type": "success",
                    "problems": problems
                }
            except Exception as e:
                self.return_data = {
                    "return_type": "error",
                    "error": "Class: getProblems - Function: read_from_fb1 - Error - fb read",
                    "exception": e
                }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.read_from_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: getProblems - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data

# Get preferred time info
class getPreferredTimes():

    def __init__(self, serializer):
        self.mobile_no = serializer.data['mobile']

    def read_from_fb1(self):
        doc_ref = registrationapi_db.collection("users").document(self.mobile_no)
        doc = doc_ref.get()
        if doc.exists:
            try:
                dict = doc.to_dict()
                preferred_time = dict['preferred_time']
                self.return_data = {
                    "return_type": "success",
                    "preferred_time": preferred_time
                }
            except Exception as e:
                self.return_data = {
                    "return_type": "error",
                    "error": "Class: getPreferredTimes - Function: read_from_fb1 - Error - fb read",
                    "exception": e
                }

    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.read_from_fb1)
            t1.start()
            t1.join()
            return self.return_data
        except:
            self.return_data = {
                "return_type": "error",
                "error": "Class: getPreferredTimes - Function: start_process - Error - Thread1",
                "exception": "None"
            }
            return self.return_data


