#
# This the Base Parctile Definition
#           Date:  20th June 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
import json
#
class BaseParticle():
    #
    # ->    This is the constructor function for the Class/Object-Type: CEFParticle()
    #
    def __init__(self):
        self._name = 'NULL'                     # This is the name of the type of particle.
        self._ident = 'NULL'                    # This is the unique identifier for the object.
        self._datatime = 'NULL'                 # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._x = 0                             # This is the X location in the vector space.
        self._y = 0                             # This is the y location in the vector space.
        self._z = 0                             # This is the z location in the vector space.
        self._force = (0,0,0, 0)                # This is the gravitaional force expressed as a vector (force, x, y, z).
        self._predictionID = 'NULL'             # This is the Prediction Particle ID that this particle relates to
    #
    #  ->   This is the getPredictionID(self) function for the Class/Object-Type: BaseParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #    
    def getPredictionID(self):
        return self._predictionID 
    #
    #  ->   This is the setPredictionID(self, predictionID) function for the Class/Object-Type: BaseParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               predictionID -   This refers to the Prediction Partcile ID.
    #    
    def setPredictionID(self, predictionID):
        self._predictionID = predictionID
        return True
    #
    #  ->   This is the setForceD(self, forceVector) function for the Class/Object-Type: BaseParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               forceVector -   This refers to the Gravitaional Force Vector that is acting on the Particle.
    #    
    def setForce(self, forceVector):
        self._force = forceVector
        return True
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: BaseParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: BaseParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: BaseParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: BaseParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
    #
    #  ->   This is the toJSON(self) function for the Class/Object-Type: BaseParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    # 
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

#
# -> This is the End of the BaseParticle() Object: Last Edited - Date:   19th April 2019
#
