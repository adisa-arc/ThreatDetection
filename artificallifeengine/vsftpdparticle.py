#
# This the VSFTPD Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from syslogparticle import SyslogParticle
#
# -> VSFTPD JSON Event Data Structure is as follows:
#       {"event": { "syslog": { "_datetime": "Apr 29 15:03:19", "_ident": "1951126555", "_type": "vsftpd",
#       "system": { "_type": "name","__text": "localhost" },"process": { "_type": "papid","__text": "vsftpd[17468]" },
#       "message": { "_type": "ascii","__text": "[ftp] FTP response: Client ::ffff:192.168.1.100, 221 Goodbye." }, 
#       "vsftpd": { "_datetime": "Apr 29 15:03:19", "_ident": "2199338593", "_type": "vsftpd","username": "ftp", 
#       "commandtype": "FTP response","sourceip": "192.168.1.100", "message": "221 Goodbye."  }  },
#       "datetime": "Apr 29 15:03:19", "_ident": "248212037", "_type": "syslog" }  }
#
class VSFTPDParticle(SyslogParticle): 
    #
    # ->    This is the constructor function for the Class/Object-Type: VSFTPDParticle()
    #
    def __init__(self, name, ident, datetime, sourceaddr, username, commandtype, data):
        super().__init__(name, ident, datetime, sourceaddr, 'vsftpd', '', data)   
                                                # This is the initialisation of the 
                                                # Syslog Particle inherited into VSFTPDParticle.
        self._name = name                       # This is the name of the type of object: 'vsftpd'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datatime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._username = username               # This is the username used to authenticate to the VSFTP Server    
        self._commandtype = commandtype         # This is the command that we sen to the VSFTP Server      
        self._sourceaddr = sourceaddr           # This is the Source IP Address that connected to the VSFTP Server.
        self._data = data                       # This is the responce form the VSFTP Server.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: IPV4Particle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: IPV4Particle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: IPV4Particle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: IPV4Particle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the VSFTPDParticle() Object: Last Edited - Date:   19th April 2019
#
