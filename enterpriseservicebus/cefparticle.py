#
# This the CEF Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from syslogparticle import SyslogParticle
#
# -> CEF JSON Event Data Structure is as follows:
#       {"event": { "syslog": { "_datetime": "Mar 28 19:23:07", "_ident": "4109161523", "_type": "cef", 
#       "system": { "type": "name", "__text": "server-01" }, "process": { "type": "proc", "__text": "CEF:0" }, 
#       "message": { "type": "proc", "__text": "CEF:0|security|threatmanager|1.0|100|poison ivy trojan 
#       infection successfully stopped|10|src=10.0.0.1 dst=2.1.2.2 " }, 
#       "cef": { "_datetime": "Mar 28 19:23:07", "_ident": "7238971310", "_type": "cef", "version": "CEF:0", 
#       "deviceinfo": "security threatmanager 1.0", "signature": "100", 
#       "name": { "type": "ascii", "__text": "poison ivy trojan infection successfully stopped" }, 
#       "severity": "10", "exenstions": { "type": "ascii", "__text": "src=10.0.0.1 dst=2.1.2.2 " } } }, 
#       "_datetime": "Mar 28 19:23:07", "_ident": "3129809786", "_type": "syslog" } }
#
class CEFParticle(SyslogParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: CEFParticle()
    #
    def __init__(self, name, ident, datetime, version, deviceinfo, sourceip, signature, severity, exenstions):
        data = str(deviceinfo) + '|' + str(deviceinfo) + '|' + str(signature) + '|' + str(severity) + '|' + str(exenstions) + '|'
        super().__init__(name, ident, datetime, sourceip, version, '', data)   
                                                # This is the initialisation of the 
                                                # Syslog Particle inherited into CEFParticle.
        self._name = name                       # This is the name of the type of object: 'cef'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datetime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = ''                   # This is the the super type object: NULL.
        self._super_id = ''                     # This is the unique identifier of the super type object: NULL.
        self._version = version                 # This is the version number of the type of CEF event. eg. "CEF:0"
        self._deviceinfo = deviceinfo           # This is the device information for the CEF event.
        self._sourceip = sourceip               # This is the Source Ip address of the CEF event.
        self._signature = signature             # This is the Signature of the CEF event.
        self._severity = severity               # This is the severity of the CEF event.
        self._exenstions = exenstions           # This is the extensions information for the CEF event.
    ##
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: CEFParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: CEFParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: CEFParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: CEFParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the CEFParticle() Object: Last Edited - Date:   19th April 2019
#
