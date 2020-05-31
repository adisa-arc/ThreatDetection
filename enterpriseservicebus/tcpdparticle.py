#
# This the TCPD Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from syslogparticle import SyslogParticle
#
# -> TCPD JSON Event Data Structure is as follows:
#       {"event": { "syslog": { "_datetime": "Mar 28 19:23:11", "_ident": "2573242221", "_type": "tcpd",
#       "system": { "_type": "name","__text": "server-03" },
#       "process": { "_type": "papid","__text": "in.telnetd[1140]:" },
#       "message": { "_type": "ascii","__text": "Connect from 10.63.148.185" }, 
#       "tcpd": { "datetime": { "_type": "std","__text": "Mar 28 19:23:11" }, 
#       "system": { "_type": "ascii","__text": "server-03" }, 
#       "process": { "_type": "papid","__text": "in.telnetd[1140]:" }, 
#       "message": { "_type": "ascii","__text": "10.63.148.185" }, 
#       "_datetime": "Mar 28 19:23:11", "_ident": "95084021", "_type": "tcpd" } } ,
#       "_datetime": "Mar 28 19:23:11", "_ident": "4173290109", "_type": "syslog" }  }
#
class TCPDParticle(SyslogParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: TCPDParticle()
    #
    def __init__(self, name, ident, datetime, system, process, connection):
        data = 'Connect from ' + str(connection)
        super().__init__(name, ident, datetime, system, process, '', data)   
                                                # This is the initialisation of the 
                                                # Syslog Particle inherited into SnortParticle.
        self._name = name                       # This is the name of the type of object: 'tcpd'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datetime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._system = system                   # This is the system that hosting the TCPD capability.
        self._process = process                 # This is the process that TCPD was invoking.
        self._connection = connection           # This is the IP address that connect to the system 
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: TCPDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: TCPDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: TCPDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: TCPDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the TCPDParticle() Object: Last Edited - Date:   19th April 2019
#
