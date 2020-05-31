 #
# This the TCP/HTTP Event Parctile Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
# -> TCP/HTTP JSON Event Data Structure is as follows:
#       { "event": { "_datetime": "May14 10:46:59", "_ident": "20919625371557827219", "_type": "ipv4", 
#       "ipv4": { "_datetime": " May 14 10:46:59", "_ident": "10120906751557827219", "_type": "tcp", 
#       "version": "4", "ihl": "5", "tos": "0", "tlen": "16384", "ident": "0", "fragoff": "64", 
#       "ttl": "255", "protocol": "6", "hcs": "39849", "sourceip": "192.168.1.100", 
#       "destinationip": "8.8.8.8", "tcp": { "_datetime": " May 14 10:46:59", "_ident": "21374904851557827219", 
#       "_type": "http", "sourport": "33518", "destport": "772", "sequnum": "1904020587", "acknum": "0", 
#       "winsize": "65535", "checksum": "52753", "urgptr": "0","dataoffset": "11", "ackflag": "0", "cwrflag": "0", 
#       "synflag": "1", "pushflag": "0", "ecnflag": "0", "finflag": "0", "rstflag": "0", "urgflag": "0", 
#       "http": { "_datetime": " May 14 10:46:59", "_ident": "1829102019201192", "_type": "http", "method": "GET", 
#       "usergaent": "Mozilla Firefix 1.0", "cookie": "1029100929101834810380101308084745785723978", 
#       "fullurl": "https://www.adisa.com/index.html"} } } } }    
#
class TCPHTTPParticle():
    #
    # ->    This is the constructor function for the Class/Object-Type: TCPHTTPParticle()
    #
    def __init__(self, name, ident, datetime, method, usergaent, cookie, fullurl):
        self._name = name                       # This is the name of the type of object: 'tcp/ip http'.
        self._ident = ident                     # This is the unique identifier for the object.
        self._datatime = datetime               # This is the date and time the event was observed.
        self._sub_type = 'NULL'                 # This is the the sub type object: NULL.
        self._sub_id = 'NULL'                   # This is the unique identifier of the sub type object: NULL.
        self._super_type = 'NULL'               # This is the the super type object: NULL.
        self._super_id = 'NULL'                 # This is the unique identifier of the super type object: NULL.
        self._method = method                   # This is the HTTP Method used in the request (PUT/GET, etc).
        self._useragent = usergaent             # This is the User Agent of the Browser making the request.
        self._cookie = cookie                   # This is the HTTP Cookie.
        self._fullurl = fullurl                 # This is the full URL of the HTTP Request.
    #
    #  ->   This is the setSubTypeID(self, identifier) function for the Class/Object-Type: TCPHTTPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the sub type object.
    #    
    def setSubTypeID(self, identifier):
        self._sub_id = identifier
        return True
    #
    # ->    This is the setSubType(self, type) function for the Class/Object-Type: TCPHTTPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the sub type object.
    #    
    def setSubType(self, type):
        self._sub_type = type
        return True
    #
    # ->    This is the setSuperType(self, type) function for the Class/Object-Type: TCPHTTPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               type        -   This refers to the super type object.
    # 
    def setSuperType(self, type):
        self._super_type = type
        return True
    #
    #  ->   This is the setSuperTypeID(self, identifier) function for the Class/Object-Type: TCPHTTPParticle()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               identifier  -   This refers to the uniquer identifier for the super type object.
    #  
    def setSuperTypeID(self, identifier):
        self._super_id = identifier
        return True
#
# -> This is the End of the TCPHTTPParticle() Object: Last Edited - Date:   19th April 2019
#
