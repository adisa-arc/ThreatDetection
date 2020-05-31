#
# This the SNORT Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from syslogparticle import SyslogParticle
#
# -> SNORT JSON Event Data Structure is as follows:
#       {"event": { "syslog": { "_datetime": "Apr 29 14:24:14", "_ident": "179189403", "_type": "snort",
#   "system": { "_type": "name","__text": "localhost" },"process": { "_type": "proc","__text": "snort:" },
#   "message": { "_type": "ascii","__text": "[1:1000006:1] Nmap XMAS Tree Scan {TCP} 192.168.1.100:64174 -> 192.168.1.252:6001" }, 
#   "snort": { "_datetime": "Apr 29 14:24:14", "_ident": "1541946601", "_type": "snort",
#   "datatime": { "_type": "std","__text": "Apr 29 14:24:14" }, "system": { "_type": "name","__text": "localhost" },
#   "process": { "_type": "proc","__text": "snort:" },"version": "[1:1000006:1]", "class": "NULL","priority": "NULL",
#   "message": { "_type": "ascii","__text": "Nmap XMAS Tree" },"protocol": "TCP",
#   "sourceip": { "_type": "ipv4","__text": "192.168.1.100" }, "sourceport": "64174",
#   "destinationip": { "_type": "ipv4","__text": "192.168.1.252" }, "destinationport": "6001" } },
#   "_datetime": "Apr 29 14:24:14", "_ident": "644103964", "_type": "syslog" }  }
#
class SnortParticle(SyslogParticle):
    #
    # ->    This is the constructor function for the Class/Object-Type: SnortParticle()
    #
    def __init__(self, name, ident, datetime, system, processName,
                 processID, version, classification, priority, protocol, message,
                 src, srcPort, dst, dstPort, jsondata):
        super().__init__(name, ident, datetime, system, processName, processID, jsondata)   
                                                # This is the initialisation of the 
                                                # Syslog Particle inherited into SnortParticle.
        self._name = name                       # This is the name of the type of object: 'snort'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datatime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._system = system                   # This is the system name that genearted the Snort event
        self._process_name = processName        # This is the process name that genearted the Snort event
        self._process_id = processID            # This is the process id that genearted the Snort event
        self._version = version                 # This is the rule version information of the Snort Event
        self._classification = classification   # This is the priority of the classification Event
        self._priority = priority               # This is the priority of the Snort Event
        self._protocol = protocol               # This is the identified protocol for the Snort Event
        self._message = message                 # This is the message data for the Snort Event
        self._src = src                         # This is the source IP address
        self._srcport = srcPort                 # This is the source port
        self._dst = dst                         # This is the destination IP address
        self._dstport = dstPort                 # This is the destination port
        self._jsondata = jsondata               # This is the JSON data for the Snort Event
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
# -> This is the End of the SnortParticle() Object: Last Edited - Date:   19th April 2019
#
