#
# This the IPv4 Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
# -> IPv4 JSON Event Data Structure is as follows:
#       { "event" : { "_datetime" : "May 13 15:4:16", "_ident" : "168071557756256", "_type" : "ipv4", 
#       "ipv4": { "_datetime" : " May 13 15:4:16", "_ident" : "2824752491557756256", "_type" : "ipv4", 
#       "version" : "4", "ihl" : "5", "tos" : "0", "tlen" : "9216", "ident" : "35273", "fragoff" : "0", 
#       "ttl" : "1", "protocol" : "17", "hcs" : "15269", "sourceip" : "192.168.1.11", 
#       "destinationip" : "224.168.168.168" } } }
#
class IPV4Particle(): 
    #
    # ->    This is the constructor function for the Class/Object-Type: IPV4Particle()
    #
    def __init__(self, name, ident, _datetime, version, ihl, tos, tlen, packident, fragoff, ttl,
                    protocol, hcs, sourceip, destinationip):
        self._name = name                           # This is the name of the type of object: 'ipv4'.
        self._ident = ident                         # This is the unique identifier for the object.
        self._datatime = _datetime                  # This is the date and time the event was observed.
        self._sub_type = 'NULL'                     # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                       # This is the unique identifier of the sub type object: NULL.
        self._super_type = ''                       # This is the the super type object: NULL.
        self._super_id = ''                         # This is the unique identifier of the super type object: NULL.
        self._version = version                     # This is the IP Version Number. For this object always: 4.
        self._ihl = ihl                             # This is the Internet Header Length.
        self._tos = tos                             # This is the Type of Service.
        self._tlen = tlen                           # This is the Total packet Length.
        self._packident = packident                 # This is the Packet Identifier.
        self._fragoff = fragoff                     # This is the Fragmentation Offset.
        self._ttl = ttl                             # This is the Time to Live.
        self._protocol = protocol                   # This is the Protocol i.e TCP/UDP or ICMP.
        self._hcs = hcs                             # This is the Header Check Sum.
        self._sourceip = sourceip                   # This is the Source IP Address.
        self._destinationip = destinationip         # This is the DEstination IP Address.
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
# -> This is the End of the IPV4Particle() Object: Last Edited - Date:   19th April 2019
#
