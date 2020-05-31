#
# This the SYSLOG Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from eventparticle import EventParticle
#
# -> SYSLOG JSON Event Data Structure is as follows:
#       {"event": { "syslog": { "_datetime": "Apr 29 15:00:14", "_ident": "163731679", "_type": "syslog",
#       "system": { "_type": "name","__text": "server-192.178.67.1" },
#       "process": { "_type": "proc","__text": "systemd:" },
#       "message": { "_type": "ascii","__text": "Started Vsftpd ftp daemon." }  }, 
#       "_datetime": "Apr 29 15:00:14","_ident": "3585948646","_type": "syslog" }  }
#
class SyslogParticle(EventParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: SyslogParticle()
    #
    def __init__(self, name, ident, datetime, system, processName, processID, data):
        super().__init__(name, ident, datetime, 'NULL', data)   # This is the initialisation of the 
                                                                # EventParticle inherited into SyslogParticle.
        self._name = name                       # This is the name of the type of object: 'syslog'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datatime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._system = system                   # This is the system that generated the syslog message.
        self._process_name = processName        # This is the process name that generated the syslog message.
        self._process_id = processID            # This is the unique process identifier that generated the syslog message.
        self._data = data                       # This is the syslog message data
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: SyslogParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: SyslogParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: SyslogParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: SyslogParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the SyslogParticle() Object: Last Edited - Date:   19th April 2019
#
