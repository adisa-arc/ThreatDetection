#
# This the DNS Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from eventparticle import EventParticle
#
# -> DNS JSON Event Data Structure is as follows:
#       {"event": { "dns": { "_datetime": "27-Mar-2019 17:00:36.097", "_ident": "3347987721", "_type": "dns", 
#       "requester": "10.63.148.85", "request": "www.adisa.global", "requesttype": "A" }, 
#       "_datetime": "27-Mar-2019 17:00:36.097", "_ident": "1514625769", "_type": "dns" } }
#
class DNSParticle(EventParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: DNSParticle()
    #
    def __init__(self, name, ident, datetime, requester, request, requesttype):
        self._name = name                       # This is the name of the type of object: 'dns'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datetime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = ''                   # This is the the super type object: NULL.
        self._super_id = ''                     # This is the unique identifier of the super type object: NULL.
        self._requester = requester             # This is the computer susyem making the request.
        self._request = request                 # This is the DNS request
        self._requesttype = requesttype         # This is the DNS request type. For example, A, SOA or MX, etc.
        self._data = self._requester + ' ' + self._request + ' ' + self._requesttype # This is the DNS DATA
        #
        super().__init__(name, ident, datetime, self._sub_type, self._data)         # This is the initialisation 
                                                                                     # of the EventParticle 
                                                                                     # inherited into DNSParticle.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: DNSParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: DNSParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: DNSParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: DNSParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the DNSParticle() Object: Last Edited - Date:   19th April 2019
#
