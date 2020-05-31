#
# This the ICMP Event Parctile Definition
#           Date:   1st June 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
# -> ICMP JSON Event Data Structure is as follows:
#       { "event" : { "_datetime" : "May 13 9:25:7", "_ident" : "9849436581557735907", 
#       "_type" : "ipv4", "ipv4": { "_datetime" : "  13 9:25:7", "_ident" : "11441089301557735907", 
#       "_type" : "icmp", "version" : "4", "ihl" : "5", "tos" : "72", "tlen" : "21504", 
#       "ident" : "58470", "fragoff" : "0", "ttl" : "121", "protocol" : "1", 
#       "hcs" : "24840", "sourceip" : "8.8.8.8", "destinationip" : "192.168.1.100", 
#       "icmp": { "_datetime" : "  13 9:25:7", "_ident" : "4702112721557735907", 
#       "_type" : "icmp", "type" : "0", "code" : "0", "checksum" : "1308" } } } }
#
class ICMPParticle():
    #
    # ->    This is the constructor function for the Class/Object-Type: ICMPParticle()
    #a
    def __init__(self, name, ident, datetime, ptype, code, checksum):
        self._name = name                       # This is the name of the type of object: 'icmp'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datatime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._type = ptype                      # This is the ICMP Packet Type of the ICMP Flow.
        self._code = code                       # This is the ICMP Packet Code of the ICMP Flow.
        self._checksum = checksum               # This is the ICMP Packet Checksum of the ICMP Flow.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: ICMPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: ICMPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: ICMPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: ICMPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the ICMPParticle() Object: Last Edited - Date:   1st June April 2019
#
