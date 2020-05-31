#
# This the SSHD Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from syslogparticle import SyslogParticle
#
# -> SSHD JSON Event Data Structure is as follows:
#       {"event": { "syslog": { "_datetime": "Apr 29 13:13:35", "_ident": "13126815", "_type": "sshd",
#       "system": { "_type": "name","__text": "localhost" },"process": { "_type": "papid","__text": "sshd[11690]:" },
#       "message": { "_type": "ascii","__text": "pam_unix(sshd:session): session closed for user ajcblyth" }, 
#       "sshd" : {"_datetime": "Apr 29 13:13:35","_ident": "3780745859","_type": "sshd", 
#       "system": { "_type": "name","__text": "localhost" },"process": { "_type": "papid","__text": "sshd[11690]:" },
#       "sourceaddr": { "_type": "ipv4","__text": "NULL" },"sourceport": "NULL","username": "NULL",
#       "message": { "_type": "ascii","__text": "pam_unix(sshd:session): session closed for user ajcblyth" } }  }, 
#       "_datetime": "Apr 29 13:13:35","_ident": "3767619043","_type": "syslog" }  }
#
class SSHDParticle(SyslogParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: SSHDParticle()
    #
    def __init__(self, name, ident, datetime, system, process,
                 sourceaddr, sourceport, username, data):
        super().__init__(name, ident, datetime, system, process, '', data)   
                                                # This is the initialisation of the 
                                                # Syslog Particle inherited into SSHDParticle.
        self._name = name                       # This is the name of the type of object: 'sshd'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datetime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._system = system                   # This is the system that generated the SSHD event
        self._process = process                 # This is the process that generated the SSHD event
        self._sourceaddr = sourceaddr           # This is the Source IP Address of the connection
        self._sourceport = sourceport           # This is the Source Port Address of the connection
        self._username = username               # This is the Username that is being used for authentication
        self._data = data                       # This is the SSHD log message.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: SSHDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: SSHDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: SSHDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: SSHDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the SSHDParticle() Object: Last Edited - Date:   19th April 2019
#
