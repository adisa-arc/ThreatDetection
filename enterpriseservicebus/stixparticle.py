#
# This the STIX Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
from baseparticle import BaseParticle
#
class STIXParticle(BaseParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: SyslogParticle()
    #
    def __init__(self, stype, name, ident, cdatetime, mdatetime, description, pattern, killchainphase,
                    lables, externalrefs, relationlist, relationtype, sref, tref):
        self._type = stype                      # This is the type of STIX object: 'STIX'.
        self._name = name                       # This is the name of the object: 'STIX'.
        self._ident = ident                     # This is the unique identifier for the STIX object.
        self._cdatetime = cdatetime             # This is the date and time the STIX object was created.
        self._mdatetime = mdatetime             # This is the date and time the STIX object was modified.
        self._description = description         # This is the description of the STIX object.
        self._pattern = pattern                 # This is the LIST of patterns for the STIX object.
        self._killchainphase = killchainphase   # This is the LIST of kill chain phases for the STIX object.
        self._lables = lables                   # This is the LIST of labels for the STIX object.
        self._externalrefs = externalrefs       # This is the LIST of external references for the STIX object.
        self._relationship_type = relationtype  # This is the relationship type
        self._source_ref = sref                 # This is the source of the relationship 
        self._target_ref = tref                 # This is the target/destination of the relationship      
        #
        self._sub_type = 'NULL'                 # This is the sub type STIX object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type STIX object: NULL.
        self._super_type = 'NULL'               # This is the super type STIX object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type STIX object: NULL.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: STIXParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: STIXParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: STIXParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: STIXParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the STIXParticle() Object: Last Edited - Date:   19th April 2019
#
