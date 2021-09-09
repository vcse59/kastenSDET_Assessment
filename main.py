import pandas as pd
import requests
import json

BASEURL = 'http://vivek.tj.dev.do.kasten.io'
API_PATH = '/api/pets1'

class CHttpClass:
    '''
    This class process http request get/post/put
    '''
    def __init__(self, cfgReaderObj=None):
        '''
        Initializing class member variables in constructor
        '''
        self._httpSession                   = None
        self._contentType                   = 'application/json'; 

    def getHttpSession(self):
        '''
        Returns current http session[SINGLETON object]
        :return:
        '''
        try:
            if self._httpSession is None:
                self._httpSession = requests.session()
                self._httpSession.headers.update({'Content-Type' : self._contentType})
            return self._httpSession
        except Exception as e:
            print ("Exception in CHttpClass::getHttpSession")
            raise

    def get(self, requestURL):
        '''
        Process get http method
        :param requestURL:
        :return:
        '''
        try:
            response = None
            response = self.getHttpSession().get(requestURL)
            return response
        except Exception as e:
            print ("Exception in CHttpClass::get")
            raise

    def put(self, putURL, values=None):
        '''
        Process put http method
        :param putURL:
        :param values:
        :return:
        '''
        try:
            response = None
            response = self.getHttpSession().put(putURL, data = values)
            return response
        except Exception as e:
            print ("Exception in CHttpClass::put")
            raise

    def post(self, postURL, values=None):
        '''
        Process post http method
        :param postURL:
        :param values:
        :return:
        '''
        try:
            response = None
            response = self.getHttpSession().post(postURL, data=values)
            return response
        except Exception as e:
            print ("Exception in CHttpClass::post")
            raise

    def delete(self, deleteURL, values=None):
        '''
        Process post http method
        :param postURL:
        :param values:
        :return:
        '''
        try:
            response = None
            response = self.getHttpSession().delete(deleteURL, data=values)
            return response
        except Exception as e:
            print ("Exception in CHttpClass::delete")
            raise

def findPets(requestURL, values=None, pHttpClassObj = None):

    try:
        if (pHttpClassObj is None):
            pHttpClassObj = CHttpClass()

        response = pHttpClassObj.get(requestURL)
        if (response.status_code != 200):
            print("findPets: Error code %s message %s" %(response.json()['code'], response.json()['message']))
            return response.status_code, None
        else:
            print("findPets: Received successful response")
            return response.status_code, response.json()
    except Exception as e:
        print ("Exception in findPets")
        raise

def addPet(requestURL, pHttpClassObj = None, values = None):

    try:
        if (pHttpClassObj is None):
            pHttpClassObj = CHttpClass()

        response = pHttpClassObj.post(requestURL, values=values)
        if (response.status_code != 200):
            print("addPet: Error code %s message %s" %(response.json()['code'], response.json()['message']))
            return response.status_code, None
        else:
            print("addPet: Received successful response")
            return response.status_code, response.json()
    except Exception as e:
        print ("Exception in addPet")
        raise

def findPetByID(requestURL, pHttpClassObj = None, petID = None):

    try:
        if (pHttpClassObj is None):
            pHttpClassObj = CHttpClass()

        completeRequestURL = requestURL

        if (petID != None):
            completeRequestURL = completeRequestURL + '/' + str(petID)

        response = pHttpClassObj.get(completeRequestURL)
        if (response.status_code != 200):
            print("findPetByID: Error code %s message %s" %(response.json()['code'], response.json()['message']))
            return response.status_code, None
        else:
            print("findPetByID: Received successful response")
            return response.status_code, response.json()
    except Exception as e:
        print ("Exception in findPetByID")
        raise

def deletePetByID(requestURL, pHttpClassObj = None, petID = None):

    try:
        if (pHttpClassObj is None):
            pHttpClassObj = CHttpClass()

        completeRequestURL = requestURL

        if (petID != None):
            completeRequestURL = completeRequestURL + '/' + str(petID)

        print(completeRequestURL)

        response = pHttpClassObj.delete(completeRequestURL)
        if (response.status_code != 204):
            print("deletePetByID: Error code %s message %s" %(response.json()['code'], response.json()['message']))
            return response.status_code
        else:
            print("deletePetByID: Received successful response")
            return response.status_code
    except Exception as e:
        print ("Exception in deletePetByID")
        raise

def ScenarioExecution1():
    '''
    1 - Retrieve all the records
    2 - Add single record
    3 - Retrieve record by record id
    4 - Delete record by record id
    '''

    isSuccess = None

    try:
        # Fetch data
        code, resp = findPets(BASEURL + API_PATH, pHttpClassObj = httpClassObj)
        if (code == 200):
            isSuccess = True
        else:
            isSuccess = False

        # Add data
        value = json.dumps({"id" : 2, "name" : "Rabbit", "status" : "available"})
        code, resp = addPet(BASEURL + API_PATH, pHttpClassObj = httpClassObj, values = value)
        contentID = None
        if (code == 200):
            isSuccess = True
            contentID = resp['id']
        else:
            isSuccess = False

        # Find Data by ID
        code, resp = findPetByID(BASEURL + API_PATH, pHttpClassObj = httpClassObj, petID = contentID)
        if (code == 204):
            isSuccess = True
            print("Record is succeessfully found for %s" %(contentID))
        else:
            isSuccess = False

        # Delete Data
        contentID = 23
        code = deletePetByID(BASEURL + API_PATH, pHttpClassObj = httpClassObj, petID = contentID)
        if (code == 204):
            isSuccess = True
            print("Record with id : %s is succeessfully deleted" %(contentID))
        else:
            isSuccess = False

        if isSuccess is False:
            print ("\033[44;41mScenarion Execution 1 is failed\033[0m")
        else:
            print ("\033[44;42mScenarion Execution 1 is passed\033[0m")

        return isSuccess
    except Exception as e:
        print ("Exception in SceanrioExecution1")
        raise

def ScenarioExecution2():
    '''
    1 - Try to call wrong API path in findPets API
    '''

    isSuccess = None

    try:
        # Fetch data
        code, resp = findPets(BASEURL + '/api/path', pHttpClassObj = httpClassObj)
        if (code == 200):
            print ("\033[44;41mScenarion Execution 2 is failed\033[0m")
            isSuccess = False
        else:
            print ("\033[44;42mScenarion Execution 2 is passed\033[0m")
            isSuccess = True

        return isSuccess
    except Exception as e:
        print ("Exception in SceanrioExecution2")
        raise

def ScenarioExecution3():
    '''
    1 - Try to call wrong API path in deletePet API
    '''

    isSuccess = None 
    try:
        code = deletePetByID(BASEURL + '/api/path', pHttpClassObj = httpClassObj, petID = 3)
        if (code == 204):
            print ("\033[44;41mScenarion Execution 3 is failed\033[0m")
            isSuccess = False
        else:
            print ("\033[44;42mScenarion Execution 3 is passed\033[0m")
            isSuccess = True

        return isSuccess
    except Exception as e:
        print ("Exception in SceanrioExecution3")
        raise

def ScenarioExecution4():
    '''
    1 - Add a record
    2 - Check Individual field of recently inserted records
    '''

    isSuccess = False

    try:
        # Add data
        name = "Rabbit123"
        status = "available"
        value = json.dumps({"id" : 2, "name" : name, "status" : status})
        code, resp = addPet(BASEURL + API_PATH, pHttpClassObj = httpClassObj, values = value)
        contentID = None
        if (code == 200):
            isSuccess = True
            contentID = resp['id']
        else:
            isSuccess = False

        # Find Data by ID
        code, resp = findPetByID(BASEURL + API_PATH, pHttpClassObj = httpClassObj, petID = contentID)
        if (code == 200):
            isSuccess = True
            print("Record is succeessfully found for %s" %(contentID))

            # Test Case Verification
            if (name == resp['name']) and (status == resp['status']) and (contentID == resp['id']):
                print ("\033[44;42mScenarion Execution 4 is passed\033[0m")
                isSuccess = True
            else:
                print ("\033[44;41mScenarion Execution 4 is failed\033[0m")
                isSuccess = False
        else:
            print ("\033[44;41mScenarion Execution 4 is failed\033[0m")
            isSuccess = False

        return isSuccess
    except Exception as e:
        print ("Exception in SceanrioExecution4")
        raise

if __name__ == '__main__':

    try:
        httpClassObj = CHttpClass()

        # Scenario 1
        print("******************************************Scenario 1***********************************************")
        '''
        1 - Retrieve all the records
        2 - Add single record
        3 - Retrieve record by record id
        4 - Delete record by record id
        '''
        ScenarioExecution1()
        print("****************************************************************************************************")

        print("\n")

        # Scenario 2
        print("******************************************Scenario 2***********************************************")
        '''
        1 - Try to call wrong API path in findPets API
        '''
        ScenarioExecution2()
        print("****************************************************************************************************")

        print("\n")

        # scenario 3
        print("******************************************scenario 3***********************************************")
        '''
        1 - Try to call wrong API path in deletePet API
        '''
        ScenarioExecution3()
        print("****************************************************************************************************")

        print("\n")

        # scenario 4
        print("******************************************scenario 4***********************************************")
        '''
        1 - Add a record
        2 - Check Individual field of recently inserted records
        '''
        ScenarioExecution4()
        print("****************************************************************************************************")
    except Exception as e:
        print ("Exception in main")
        raise
