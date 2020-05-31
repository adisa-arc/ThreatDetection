#
# This the Event Base/Meta Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from baseparticle import BaseParticle
#
# -> Event Base/Meta Object/Particle JSON Event Data Structure is as follows:
#       {"event": { "_datetime": "Apr 29 13:13:35", "_ident": "13126815", "_type": "event",
#       "message": { "_type": "ascii","__text": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" }  }  }
#
class EventParticle(BaseParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: EventParticle()
    #
    def __init__(self, name, ident, datetime, subtype, data):
        super().__init__()                      # This is the initialiszation of the Super Inhertited Particle.
        self._name = name                       # This is the name of the type of object: 'Event'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datatime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._data = data                       # This is the data asscoaited withe the base/meta event object/particle
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: EventParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: EventParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: EventParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: EventParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the EventParticle() Object: Last Edited - Date:   19th April 2019
#
