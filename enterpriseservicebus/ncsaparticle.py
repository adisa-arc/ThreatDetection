#
# This the NCSA Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from eventparticle import EventParticle
#
# -> NCSA JSON Event Data Structure is as follows:
#       {"event": { "nsca": { "_datetime": "[01/Jan/2017:09:00:00 +0000]", "_ident": "1242662182", "_type": "nsca",
#       "client": { "_type": "ipv4", "__text": "66.249.66.1"  }, "userid": "-", "user": "-", 
#       "request": { "_type": "ascii", "__text": "GET /contact.html"  }, "protocol": "HTTP/1.1", "statuscode": "200", 
#       "size": "250"  }, "_datetime": "[01/Jan/2017:09:00:00 +0000]", "_ident": "406332477", "_type": "nsca" }  }
#
class NCSAParticle(EventParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: NCSAParticle()
    #
    def __init__(self, name, ident, datetime, client, userid, user, request, protocol, statuscode, size):
        self._name = name                       # This is the name of the type of object: 'nsca'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datetime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = ''                   # This is the the super type object: NULL.
        self._super_id = ''                     # This is the unique identifier of the super type object: NULL.
        self._client = client                   # This is the web browser that the client is using
        self._userid = userid                   # This is the user id that the client is using
        self._user = user                       # This is the username that the client is using
        self._request = request                 # This is the URL request
        self._statuscode = statuscode           # This is the status code of the request
        self._size = size                       # This is the size of data returned
        self._data = request                    # This is the data of data returned
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: NCSAParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: NCSAParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: NCSAParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: NCSAParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the NCSAParticle() Object: Last Edited - Date:   19th April 2019
#
