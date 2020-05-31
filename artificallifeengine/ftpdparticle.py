#
# This the FTPD Event Parctile Definition 
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from eventparticle import EventParticle
#
# -> FTPD JSON Event Data Structure is as follows:
#       {"event": { "ftpd": { "_datetime": "Mar 28 19:59:31", "_ident": "136661321", "_type": "ftpd", 
#       "transfertime": "5057", "remotehost": { "_type": "ipv4","__text": "192.168.20.10" }, "filesize": "8196242", 
#       "filename": "/home/ajcblyth/datalog2.tar.gz", "transfertype": "b", "actionflag": "_", "direction": "o", 
#       "accessmode": "r", "username": "ajcblyth", "servicename": "ftp", "authmethod": "0", "authuserid": "*", 
#       "status": "c" }, "_datetime": "Mar 28 19:59:31", "_ident": "1290283528", "_type": "ftpd" }  }
#
class FTPDParticle(EventParticle):  
    #
    # ->    This is the constructor function for the Class/Object-Type: FTPDParticle()
    #
    def __init__(self, name, ident, datetime, transfertime, remotehost, filesize, filename, transfertype, actionflag,
                    direction, accessmode, username, servicename, authmethod, authuserid, status ):
        self._name = name                       # This is the name of the type of object: 'ftpd'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datetime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = ''                   # This is the the super type object: NULL.
        self._super_id = ''                     # This is the unique identifier of the super type object: NULL.
        self._transfertime  = transfertime      # This is the time the transfer request was made.
        self._remotehost = remotehost           # This is the IP address of the remote host that made the request.'
        self._filesize = filesize               # This is the size of the file that we requested.
        self._filename = filename               # This is the file name that was requested.
        self._transfertype = transfertype       # This is the transfer type of the FTP request.
        self._actionflag = actionflag           # This is the action floag of the FTP request.
        self._direction = direction             # This is the direction of the flow of data from the FTP request.
        self._accessmode = accessmode           # This is the access mode used by the FTP request. (read/write)
        self._username = username               # This is the username used for authentication by the FTP request.
        self._servicename = servicename         # This is the service name used by the FTP request, i.e. 'ftp'
        self._authmethod = authmethod           # This is the authroisation method used by the FTP request.
        self._authuserid = authuserid           # This is the authroisation id of the FTP request.
        self._status = status                   # This is the status code of the FTP request.
        self._data = filename                   # This is the data of the FTP request.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: FTPDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: FTPDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: FTPDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: FTPDParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the FTPDParticle() Object: Last Edited - Date:   19th April 2019
#
