#
# This the TCP Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
# -> TCP JSON Event Data Structure is as follows:
#       { "event" : { "_datetime" : "May 13 17:0:30", "_ident" : "10499974391557763230", 
#       "_type" : "ipv4", "ipv4": { "_datetime" : " May 13 17:0:30", 
#       "_ident" : "14338298741557763230", "_type" : "tcp", "version" : "4", "ihl" : "5", 
#       "tos" : "0", "tlen" : "16384", "ident" : "0", "fragoff" : "64", "ttl" : "255", 
#       "protocol" : "6", "hcs" : "39849", "sourceip" : "192.168.1.100", 
#       "destinationip" : "8.8.8.8", "tcp": { "_datetime" : "  13 17:0:30", 
#       "_ident" : "14646893311557763230", "_type" : "tcp", "sourport" : "31181", 
#       "destport" : "21505", "sequnum" : "131200348", "acknum" : "0", "winsize" : "65535", 
#       "checksum" : "8321", "urgptr" : "0", "dataoffset" : "11", "ackflag" : "0", "cwrflag" : "0", 
#       "synflag" : "1", "pushflag" : "0", "ecnflag" : "0", "finflag" : "0", "rstflag" : "0", 
#       "urgflag" : "0" } } } }
#
class TCPParticle():
    #
    # ->    This is the constructor function for the Class/Object-Type: TCPParticle()
    #a
    def __init__(self, name, ident, datetime, sourport, destport, sequnum, acknum, winsize, checksum,
                    urgptr, dataoffset, ackflag, cwrflag, synflag, pushflag, ecnflag, finflag, rstflag, urgflag):
        self._name = name                       # This is the name of the type of object: 'tcp'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datatime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._sourport = sourport               # This is the Source Port of the TCP Flow.
        self._destport = destport               # This is the Destination Port of the TCP Flow.
        self._sequnum = sequnum                 # This is the sequence number of the TCP Flow.
        self._acknum = acknum                   # This is the acknowledgement number of the TCP Flow.
        self._winsize = winsize                 # This is the windows size of the TCP Flow.
        self._checksum = checksum               # This is the checksum of the TCP Flow.
        self._urgptr = urgptr                   # This is the Urent point/status of the TCP Flow.
        self._dataoffset = dataoffset           # This is the data of set of the TCP Flow.
        self._ackflag = ackflag                 # This is the Acknowledgement Flag from the TCP State Chart.
        self._cwrflag = cwrflag                 # This is the CWR Flag.
        self._synflag = synflag                 # This is the Syncronisation Flag from the TCP State Chart.
        self._pushflag = pushflag               # This is the PUsh Data Flag from the TCP State Chart.
        self._ecnflag = ecnflag                 # This is the ECN Flag.
        self._finflag = finflag                 # This is the Finish Flag from the TCP State Chart.
        self._rstflag = rstflag                 # This is the Reset Flag from the TCP State Chart.
        self._urgflag = urgflag                 # This is the Urgent Flag from the TCP State Chart.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: TCPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: TCPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: TCPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: TCPParticle()
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
