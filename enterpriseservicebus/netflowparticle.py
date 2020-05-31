#
# This the NetFlow Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
from eventparticle import EventParticle
#
# -> NetFlow JSON Event Data Structure is as follows:
#       {"event": { "netflow": { "_datetime": "Mar 28 19:23:07", "_ident": "1029384756", "_type": "netflow",
#       "duration": "00:57:37", "protocol": "TCP", "sourceip": "192.168.30.142", "sourceport": "22", 
#       "destinationip": "192.168.30.142", "destport": "22", "packets": "1029", "bytes": "901827" }, 
#       "_datetime": "Mar 28 19:23:07", "_ident": "1029384757", "_type": "netflow"} }
#
class NetFlowParticle(EventParticle): 
    #
    # ->    This is the constructor function for the Class/Object-Type: NetFlowParticle()
    #
    def __init__(self, name, ident, datetime, duration, protocol, sourceip, sourceport, destinationip, destport, packets, pbytes):
        self._name = name                            # This is the name of the type of object: 'netflow'.
        self._ident = ident                          # This is the unique identifier for the object.
        self._datetime = datetime                    # This is the date and time the event was observed.
        self._sub_type = 'NULL'                      # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                        # This is the unique identifier of the sub type object: NULL.
        self._super_type = ''                        # This is the the super type object: NULL.
        self._super_id = ''                          # This is the unique identifier of the super type object: NULL.
        self._duration = duration                    # This is the duration of the flow.
        self._protocol = protocol                    # This is the protocol used by the flow.
        self._sourceip = sourceip                    # This is the source ip address of the flow.
        self._sourceport = sourceport                # This is the source port of the flow.
        self._destinationip = destinationip          # This is the destination ip address of the flow.
        self._destport = destport                    # This is the destination port of the flow.
        self._packets = packets                      # This is the number of packets in the flow.
        self._pbytes = pbytes                        # This is the number of Bytes in the Flow.
        self._data = 'NetFlow'                       # This is the data in the Flow.
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
# -> This is the End of the NetFlowParticle() Object: Last Edited - Date:   19th April 2019
#
