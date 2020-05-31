#
# This the Windows Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from eventparticle import EventParticle
#
# -> EVT JSON Event Data Structure is as follows:
#       {"event": { "evt": { "_datetime": "2019-03-28T19:23:07.182918260Z", "_ident": "7856384756", 
#       "_type": "evt", "source": "Security", "eventid": "4624", "datetime": "2019-03-28T19:23:07.182918260Z", 
#       "user": "ajcblyth", "computer": "dc1.adisa.global", "processid": "61762", "threadid": "1920", 
#       "keywords": "logon" },  "_datetime": "Mar 28 19:23:07", "_ident": "7856384757", "_type": "evt"} }
#
class EVTParticle(EventParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: EVTParticle()
    #
    def __init__(self, name, ident, datetime, source, eventid, evtdatetime, user, computer, processid, 
                        threadid, keywords):
        self._name = name                       # This is the name of the type of object: 'EVT'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datetime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = ''                   # This is the the super type object: NULL.
        self._super_id = ''                     # This is the unique identifier of the super type object: NULL.
        self._source = source                   # This is the windows subsystem source of the event. Eg 'security'
        self._eventid = eventid                 # This is the event id that tells us what the type fo the event is
        self._evtdatetime = evtdatetime         # This is the date and time that the event was detected.
        self._user = user                       # This is the user (SID) that generated the event
        self._computer = computer               # This is the computer that generated the event
        self._processid = processid             # This is the process id that generated the event
        self._threadid = threadid               # This is the thread id that generated the event
        self._keywords = keywords               # This are keywords associated with the event
        self._data = keywords                   # This are data associated with the event
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: EVTParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: EVTParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: EVTParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: EVTParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the EVTParticle() Object: Last Edited - Date:   19th April 2019
#
