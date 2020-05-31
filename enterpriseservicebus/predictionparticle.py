#
# This the Prediction Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
from baseparticle import BaseParticle
#
#
#
class PredictionParticle(BaseParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: PredictionParticle()
    #
    def __init__(self, ptype, name, ident, datetime):
        self._type = ptype                      # This is the type of object: 'PredictionParticle'.
        self._name = name                       # This is the name of the type of object: 'PredictionParticle'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datetime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._references = []                   # This is the list of refences that define the nature of the  
                                                #   PredictionParticle. List is; [(source_name, source_id),...]
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: PredictionParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: PredictionParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: PredictionParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: PredictionParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the PredictionParticle() Object: Last Edited - Date:   19th April 2019
#
