#
# This the UDP Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
# -> UDP JSON Event Data Structure is as follows:
#       { "event" : { "_datetime" : "May 13 9:15:41", "_ident" : "8233788401557735341", 
#       "_type" : "ipv4", "ipv4": { "_datetime" : "  13 9:15:41", "_ident" : "1435426121557735341", 
#       "_type" : "udp", "version" : "4", "ihl" : "5", "tos" : "0", "tlen" : "25088", 
#       "ident" : "31815", "fragoff" : "0", "ttl" : "255", "protocol" : "17", "hcs" : "26321", 
#       "sourceip" : "192.168.1.4", "destinationip" : "224.0.0.251", "udp": { "_datetime" : "  13 9:15:41", 
#       "_ident" : "8965443031557735341", "_type" : "udp", "checksum" : "32165", "length" : "19968", 
#       "sourport" : "59668", "destport" : "59668" } } } }
#
class UDPParticle():
    #
    # ->    This is the constructor function for the Class/Object-Type: UDPParticle()
    #a
    def __init__(self, name, ident, datetime, checksum, length, sourport, destport):
        self._name = name                       # This is the name of the type of object: 'udp'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datatime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._checksum = checksum               # This is the checksum of the UDP header.
        self._length = length                   # This is the Length of the UDP packet.
        self._sourport = sourport               # This is the source port of the UDP Flow.
        self._destport = destport               # This is the destination port of the UDP Flow.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: UDPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: UDPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: UDPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: UDPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the UDPParticle() Object: Last Edited - Date:   19th April 2019
#
