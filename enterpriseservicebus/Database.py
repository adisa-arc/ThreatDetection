# ------------------------------------------------------------------------------------------------- #
#   Title: This is the Particle Database Interface for the Swarm                                    #
#   Date:   1st June 2019                                                                           #
#   Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)                                      #
#                                                                                                   #
#   Description:    The role and function of the model is to define the database class              #
#                   and its associated functions. That 'Database" class/object functions            #
#                   to store the partcile and maintain and interafce into the Swarm.                #
# ------------------------------------------------------------------------------------------------- # 
# 
# -> This is the import saection for python system.                                                 #
#
import hashlib
import random
#
# -> This is the import saection for all particle types.                                            #
#
from eventparticle import EventParticle
from syslogparticle import SyslogParticle
from snortparticle import SnortParticle
from sshdparticle import SSHDParticle
from vsftpdparticle import VSFTPDParticle
from tcpdparticle import TCPDParticle
from cefparticle import CEFParticle
from dnsparticle import DNSParticle 
from ftpdparticle import FTPDParticle
from ncsaparticle import NCSAParticle 
from netflowparticle import NetFlowParticle
from evtparticle import EVTParticle
from ipv4particle import IPV4Particle
from tcpparticle import TCPParticle
from udpparticle import UDPParticle
from icmpparticle import ICMPParticle
from tcphttpparticle import TCPHTTPParticle
from stixparticle import STIXParticle
from predictionparticle import PredictionParticle
from vectorspace import VectorSpace
from dataparticle import DataParticle
#
# -> This is the import section for the JanusGraph
# 
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
# 
# -> Defines if the database object is being debugged and will turn debugging output on/off.        #
#
DEBUG = False
#
# -> Defines the Database Object (DB) and its associated database cache.                            #
#
class DB():
    # insertDataParticle                                                                            #
    # -> This is the object initialisation function for the  Database Object (DB).                  #
    #
    def __init__(self):
        self._cacheDB = {}                      # This is the dictionary for the Database Cache.    #
        self._cacheDB['data'] = {}              # This is the dictionary for the DATA particle.     #
        self._cacheDB['event'] = {}             # This is the dictionary for the EVENT particle.    #   
        self._cacheDB['ipv4'] = {}              # This is the dictionary for the IPV4 particle.     #
        self._cacheDB['tcp'] = {}               # This is the dictionary for the TCP particle.      #
        self._cacheDB['tcphttp'] = {}           # This is the dictionary for the TCPHTTP particle.  #
        self._cacheDB['udp'] = {}               # This is the dictionary for the UDP particle.      #
        self._cacheDB['icmp'] = {}              # This is the dictionary for the ICMP particle.     #
        self._cacheDB['syslog'] = {}            # This is the dictionary for the SYSLOG particle.   #
        self._cacheDB['ftpd'] = {}              # This is the dictionary for the FTPD particle.     #
        self._cacheDB['tcpd'] = {}              # This is the dictionary for the TCPD particle.     #
        self._cacheDB['snort'] = {}             # This is the dictionary for the SNORT particle.    #
        self._cacheDB['sshd'] = {}              # This is the dictionary for the SSHD particle.     #
        self._cacheDB['vsftpd'] = {}            # This is the dictionary for the VSFTPD particle.   #
        self._cacheDB['cef'] = {}               # This is the dictionary for the STIX particle.     #
        self._cacheDB['dns'] = {}               # This is the dictionary for the DNS particle.      #
        self._cacheDB['nsca'] = {}              # This is the dictionary for the NSCA particle.     #
        self._cacheDB['netflow'] = {}           # This is the dictionary for the NETFLOW particle.  #
        self._cacheDB['evt'] = {}               # This is the dictionary for the EVT particle.      #
        self._cacheDB['stix'] = {}              # This is the dictionary for the STIX particle.     #
        self._cacheDB['prediction'] = {}        # This is the dictionary for the PRED particle.     #
        self._vectorSpace = VectorSpace()       # The vector space that all particles exist in.     #
        self._graph = Graph()                   # This is the JanusGraph Graph Structure.           #
    #
    # -> This is setGraph function that sets the JanusGraph Construct in the Cache/Database.
    #
    def setJanusGraph(self, jgraph):
        self._graph = jgraph
        return True 
    # 
    # -> This is the getDataParticleList function that gest all DataParticles in the Cache/Database.
    # 
    def getDataParticleList(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['data']:
            dataParticleList.append(self._cacheDB['data'][dataParticle].toJSON())
        return dataParticleList
    # 
    # 
    # 
    def getAllSTIXParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['stix']:
            dataParticleList.append(self._cacheDB['stix'][dataParticle].toJSON())
        return dataParticleList
    # 
    # f
    # -> This is the getAllSyslogParticles function that gets all SyslogParticles in the Cache/Database. 
    # 
    def getAllSyslogParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['syslog']:
            dataParticleList.append(self._cacheDB['syslog'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllSnortParticles function that gets all SnortParticles in the Cache/Database. 
    # 
    def getAllSnortParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['snort']:
            dataParticleList.append(self._cacheDB['snort'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllTCPDParticles function that gets all TCPDParticles in the Cache/Database. 
    #  
    def getAllTCPDParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['tcpd']:
            dataParticleList.append(self._cacheDB['tcpd'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllSSHDParticles function that gets all SSHDParticles in the Cache/Database. 
    #  
    def getAllSSHDParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['sshd']:
            dataParticleList.append(self._cacheDB['sshd'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllCEFarticles function that gets all CEFParticles in the Cache/Database. 
    # 
    def getAllCEFarticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['cef']:
            dataParticleList.append(self._cacheDB['cef'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllVSFTPDParticles function that gets all VSFTPDParticles in the Cache/Database. 
    #  
    def getAllVSFTPDParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['vsftpd']:
            dataParticleList.append(self._cacheDB['vsftpd'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllDNSParticles function that gets all DNSParticles in the Cache/Database. 
    #  
    def getAllDNSParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['dns']:
            dataParticleList.append(self._cacheDB['dns'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllNCSAParticles function that gets all DNSParticles in the Cache/Database. 
    #  
    def getAllNCSAParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['nsca']:
            dataParticleList.append(self._cacheDB['nsca'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllNetFlowParticles function that gets all NetFlowParticles in the Cache/Database. 
    #  
    def getAllNetFlowParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['netflow']:
            dataParticleList.append(self._cacheDB['netflow'][dataParticle].toJSON())
        print('getAllNetFlowParticles', dataParticleList )
        return dataParticleList
    # 
    # -> This is the getAllFTPDParticles function that gets all FTPDParticles in the Cache/Database. 
    #  
    def getAllFTPDParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['ftpd']:
            dataParticleList.append(self._cacheDB['ftpd'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the getAllEvtXParticles function that gets all EVTParticles in the Cache/Database. 
    #  
    def getAllEvtXParticles(self, jdata):
        dataParticleList = []
        for dataParticle in self._cacheDB['evt']:
            dataParticleList.append(self._cacheDB['evt'][dataParticle].toJSON())
        return dataParticleList
    # 
    # -> This is the insertDataParticle function that inserts a DataParticle into the Cache/Database.
    # 
    def insertDataParticle(self, jdata):
        datetime = jdata['data']['_datetime']
        identifn = hashlib.sha224(str(jdata['data']['_ident']+str(random.random())).encode('utf-8')).hexdigest()
        datatype = jdata['data']['_type']
        dataname = jdata['data']['_name']
        external = jdata['data']['_external_id']
        # 
        self.DBInsert('data', identifn, DataParticle(datatype, identifn, datetime, dataname, external))
        #
        if (DEBUG):
            print('Identifier     :->', datetime)
            print('Datatime       :->', identifn)
            print('Data Type      :->', datatype)
            print('Data Name      :->', dataname)
            print('External ID    :->', external)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return True
    # 
    # -> This is the getParticle function that returns a partcile from the cache of type 'pT'       #
    #    and identififer 'pID'
    #
    def getParticle(self, pT, pID):
        return self._cacheDB[pT][pID].toJSON()
    #
    # -> This is the vectorSpaceDecayParticle function that implelments that particle decay       #  
    #    funtionality in the vector space.
    #
    def vectorSpaceDecayParticle(self, pT, pID):
        _ = self._vectorSpace.vectorSpaceDecayParticle(pT, pID)
        return True
    #
    # -> This is the vectorSpaceGetParticlePosiution function that implelments that particle decay       #  
    #    funtionality in the vector space.
    #
    def vectorSpaceGetParticlePosition(self, pT, pID):
        return self._vectorSpace.vectorSpaceGetParticlePosition(pT, pID)
    #
    # -> This is the vectorMatrixUpdateEventParticle function that implements the Update Event 
    #    Particle in the vector space functionality.
    # 
    def vectorMatrixUpdateEventParticle(self, uT, pT, pID, eT ,eID):
        self._cacheDB[eT][eID].setPredictionID(pID)
        return self._vectorSpace.vectorMatrixUpdateEventParticle(uT, pT, pID, eT ,eID)
    #
    # -> This is the getPredictionParticlParameters function that implements the get 
    #    Prediction Particle Parameters in the vector space functionality.
    #
    def getPredictionParticlParameters(self, particleType, particleID):
        return self._cacheDB[particleType][particleID]._references
    #
    # -> This is the updatePredictionPartcile function that implements the update 
    #    Prediction Particle in the vector space functionality.
    #
    def updatePredictionPartcile(self, particleType, particleID):
        return self._vectorSpace.updatePredictionPartcile(particleType, particleID)
    #
    # -> This is the distributePredictionParticleinGVSM function that implements the calculate 
    #    the distribution of Prediction Particle in the vector space functionality.
    #
    def distributePredictionParticleinGVSM(self):
         return self._vectorSpace.distributePredictionParticleinGVSM()
    #
    # -> This is the vectorSpaceUpdateParticleLocation function that implements the update 
    #    partcile location in the vector space functionality.
    #
    def vectorSpaceUpdateParticleLocation(self, x, y, z, particleType, particleID):
        return self._vectorSpace.updateParticleLocation(x, y, z, particleType, particleID)
    #
    # -> This is the vectorSpaceGetAllSTIXParticle function that implements the get 
    #    all STIX/Prediction particles that are in the vector space functionality.
    #
    def vectorSpaceGetAllSTIXParticle(self):
        return  self._vectorSpace.getAllSTIXParticles()
    #
    # -> This is the vectorSpaceGetAllEventParticle function that implements the get 
    #    all event types particles that are in the vector space functionality.
    #
    def vectorSpaceGetAllEventParticle(self): 
        return self._vectorSpace.getAllEventParticles() 
    #
    # -> This is the vectorSpaceGetParticleXYZ function that implements the get 
    #    all event particle that is at location x,y,z in the vector space functionality.
    # 
    def vectorSpaceGetParticleXYZ(self, x, y, z): 
        return self._vectorSpace.getParticleList(x, y, z)
    # 
    # -> This is the vectorSpaceAddParticleList function that implements add partcile form the 
    #    vector space functionality.  
    # 
    def vectorSpaceAddParticleList(self, x, y, z, particle): 
        return self._vectorSpace.addParticleList(x, y, z, particle)
    # 
    # -> This is the vectorSpaceDelParticleList function that implements delete partcile form the 
    #    vector space functionality.  
    # 
    def vectorSpaceDelParticleList(self, particle):
         return self._vectorSpace.delParticleList(particle)
    # 
    # -> This is the DBInsert function that implements the low-level insert event into database functionality.  
    #
    def DBInsert(self, particletype, digest, partcile): 
        self._cacheDB[particletype][digest] = partcile
        #self._graph.addV(particletype).property('particle',partcile)
    # 
    # -> This is the setSubParticle function that implements the set partcile sub-type functionality.  
    #
    def setSubParticle(self, particle_type, digest, sub_particle_id, sub_particle_type):
        self._cacheDB[particle_type][digest].setSubType(sub_particle_type)
        self._cacheDB[particle_type][digest].setSubTypeID(sub_particle_id)
        return True
    # 
    # -> This is the setSubParticle function that implements the set partcile super-type functionality.  
    #
    def setSuperParticle(self, particle_type, digest, super_particle_id, super_particle_type):
        self._cacheDB[particle_type][digest].setSuperType(super_particle_type)
        self._cacheDB[particle_type][digest].setSuperTypeID(super_particle_id)
        return True
    #
    # -> This is the insertEvent function that implements the insert event into database functionality. 
    #
    def insertEvent(self, jdata, digest):
        datetime = jdata['event']['_datetime']
        sub_type = jdata['event']['_type']
        eventParticle = EventParticle('event', digest, datetime, sub_type, jdata['event'])
        xVector = random.randrange(-10, 10)
        yVector = random.randrange(-10, 10)
        zVector = random.randrange(-10, 10)
        forceVector = random.randrange(0, 50)
        eventParticle.setForce((xVector, yVector, zVector, forceVector))
        self.DBInsert('event', digest, eventParticle)
        return digest
    #
    #
    #
    # -> IPV4 JSON Event Data Structure is as follows:
    #       { "event" : { "_datetime" : "May 13 15:4:21", "_ident" : "17464748191557756261", "_type" : "ipv4", 
    #       "ipv4": { "_datetime" : " May 13 15:4:21", "_ident" : "11957957371557756261", "_type" : "ipv4", 
    #       "version" : "4", "ihl" : "5", "tos" : "0", "tlen" : "10240", "ident" : "0", "fragoff" : "64", 
    #       "ttl" : "64", "protocol" : "6", "hcs" : "49329", "sourceip" : "192.168.1.100", 
    #       "destinationip" : "52.97.146.162" } } }
    #
    def insertIPv4(self, jdata, digest):
        datetime = jdata['ipv4']['_datetime']
        version = jdata['ipv4']['version']
        ihl = jdata['ipv4']['ihl']
        tos = jdata['ipv4']['tos']
        tlen = jdata['ipv4']['tlen']
        ident = jdata['ipv4']['ident']
        fragoff = jdata['ipv4']['fragoff']
        ttl = jdata['ipv4']['ttl']
        protocol = jdata['ipv4']['protocol']
        hcs = jdata['ipv4']['hcs']
        sourceip = jdata['ipv4']['sourceip']
        destinationip = jdata['ipv4']['destinationip']
        identifn = hashlib.sha224(str(digest+str(random.random())).encode('utf-8')).hexdigest()
        #
        self.DBInsert('ipv4', digest, IPV4Particle('ipv4', identifn, datetime, version, ihl, tos, tlen, ident,
                                                    fragoff, ttl, protocol, hcs, sourceip, destinationip))
        #
        self._vectorSpace.addParticleList(0,0,0,('ipv4', digest ))
        #
        if (DEBUG):
            print('Identifier     :-> IPV4/', digest)
            print('Datatime       :->', datetime)
            print('IP Version     :->', version)
            print('Inet Header Len:->', ihl)
            print('Type of Service:->', tos)
            print('Total Length   :->', tlen)
            print('Ident          :->', ident)
            print('Frag Off Set   :->', fragoff)
            print('Time to Live   :->', ttl)
            print('Protocol       :->', protocol)
            print('Header CheckSum:->', hcs)
            print('Source IP Addr :->', sourceip)
            print('Dest IP Addr   :->', destinationip)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> TCP JSON Event Data Structure is as follows:
    #       { "event" : { "_datetime" : "May 13 17:0:31", "_ident" : "16117398161557763231", "_type" : "ipv4", 
    #       "ipv4": { "_datetime" : " May 13 17:0:31", "_ident" : "1523642541557763231", "_type" : "tcp", 
    #       "version" : "4", "ihl" : "5", "tos" : "0", "tlen" : "16384", "ident" : "0", "fragoff" : "64", 
    #       "ttl" : "255", "protocol" : "6", "hcs" : "39849", "sourceip" : "192.168.1.100", 
    #       "destinationip" : "8.8.8.8", "tcp": { "_datetime" : "  13 17:0:31", "_ident" : "9855097541557763231", 
    #       "_type" : "tcp", "sourport" : "46798", "destport" : "10146", "sequnum" : "3954678030", 
    #       "acknum" : "0", "winsize" : "65535", "checksum" : "25923", "urgptr" : "0", "dataoffset" : "11", 
    #       "ackflag" : "0", "cwrflag" : "0", "synflag" : "1", "pushflag" : "0", "ecnflag" : "0", "finflag" : "0", 
    #       "rstflag" : "0", "urgflag" : "0" } } } }
    #
    def insertIPTCP(self, jdata, digest):
        datetime = jdata['_datetime']
        sourport = jdata['sourport']
        destport = jdata['destport']
        sequnum = jdata['sequnum']
        acknum = jdata['acknum']
        winsize = jdata['winsize']
        checksum = jdata['checksum']
        urgptr = jdata['urgptr']
        dataoffset = jdata['dataoffset']
        ackflag = jdata['ackflag']
        cwrflag = jdata['cwrflag']
        synflag = jdata['synflag']
        pushflag = jdata['pushflag']
        ecnflag= jdata['ecnflag']
        finflag = jdata['finflag']
        rstflag = jdata['rstflag']
        urgflag = jdata['urgflag']
        #       
        self.DBInsert('tcp', digest, TCPParticle('tcp', digest, datetime, sourport, destport, sequnum,
                                                    acknum, winsize, checksum, urgptr, dataoffset, ackflag,
                                                    cwrflag, synflag, pushflag, ecnflag, finflag, rstflag, urgflag))
        #
        self._vectorSpace.addParticleList(0,0,0,('tcp', digest ))
        #
        if (DEBUG):
            print('Identifier     :-> TCP/', digest)
            print('Datatime       :->', datetime)
            print('Source Port    :->', sourport)
            print('Dest Port      :->', destport)
            print('Sequence Number:->', sequnum)
            print('Ack Number     :->', acknum)
            print('Windows Size    :->', winsize)
            print('Check Sum       :->', checksum)
            print('Data Off Set    :->', dataoffset)
            print('Urgent Pointer  :->', urgptr)
            print('TCP Flags:')
            print('    :-> [SYN:', synflag,']/[ACK:', ackflag, ']/[PSH:', pushflag, ']/[FIN:', finflag,']')
            print('    :-> [URG:', urgflag,']/[CWR:', cwrflag, ']/[ECN:', ecnflag, ']/[RST:', rstflag,']')
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> UDP JSON Event Data Structure is as follows:
    #       { "event" : { "_datetime" : "May 14 9:53:9", "_ident" : "7845588211557823989", "_type" : 
    #       "ipv4", "ipv4": { "_datetime" : "  14 9:53:9", "_ident" : "5305119671557823989", "_type" : "udp", 
    #       "version" : "4", "ihl" : "5", "tos" : "0", "tlen" : "61952", "ident" : "0", "fragoff" : "64", 
    #       "ttl" : "64", "protocol" : "17", "hcs" : "17846", "sourceip" : "192.168.1.1", 
    #       "destinationip" : "192.168.1.100", "udp": { "_datetime" : "  14 9:53:9", "_ident" : "21100106721557823989", 
    #       "_type" : "udp", "checksum" : "38972", "length" : "56832", "sourport" : "13568", 
    #       "destport" : "15855" } } } }
    #
    def insertIPUDP(self, jdata, digest):
        datetime = jdata['_datetime']
        sourport = jdata['sourport']
        destport = jdata['destport']
        checksum = jdata['checksum']
        length = jdata['length']
        # 
        self.DBInsert('udp', digest, UDPParticle('udp', digest, datetime, checksum, length, sourport, destport))
        #
        self._vectorSpace.addParticleList(0,0,0,('udp', digest ))
        #
        if (DEBUG):
            print('Identifier     :-> UPD/', digest)
            print('Datatime       :->', datetime)
            print('Source Port    :->', sourport)
            print('Dest Port      :->', destport)
            print('Packet Checksum:->', checksum)
            print('Packet Length  :->', length)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> ICMP JSON Event Data Structure is as follows:
    #       { "event" : { "_datetime" : "May 13 9:25:7", "_ident" : "9849436581557735907", "_type" : "ipv4", 
    #       "ipv4": { "_datetime" : "  13 9:25:7", "_ident" : "11441089301557735907", "_type" : "icmp", 
    #       "version" : "4", "ihl" : "5", "tos" : "72", "tlen" : "21504", "ident" : "58470", "fragoff" : "0", 
    #       "ttl" : "121", "protocol" : "1", "hcs" : "24840", "sourceip" : "8.8.8.8", 
    #       "destinationip" : "192.168.1.100", "icmp": { "_datetime" : "  13 9:25:7", 
    #       "_ident" : "4702112721557735907", "_type" : "icmp", "type" : "0", "code" : "0", 
    #       "checksum" : "1308" } } } }
    #
    def insertIPICMP(self, jdata, digest):
        datetime = jdata['_datetime']
        ptype = jdata['type']
        code = jdata['code']
        checksum = jdata['checksum']
        #
        self.DBInsert('icmp', digest, ICMPParticle('icmp', digest, datetime, ptype, code, checksum))
        #
        self._vectorSpace.addParticleList(0,0,0,('icmp', digest ))
        #
        if (DEBUG):
            print('Identifier     :-> ICMP/', digest)
            print('Datatime       :->', datetime)
            print('ICMP Type      :->', ptype)
            print('ICMP code      :->', code)
            print('ICMP Checksum  :->', checksum)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> TCP/IP HTTP JSON Event Data Structure is as follows:
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
    def insertIPTCPHTTP(self, jdata, digest):
        datetime = jdata['_datetime']
        method = jdata['method']
        usergaent = jdata['usergaent']
        cookie = jdata['cookie']
        fullurl = jdata['fullurl']
        #
        self.DBInsert('tcphttp', digest, TCPHTTPParticle('tcphttp', digest, datetime, method, usergaent, cookie, fullurl))
        #
        self._vectorSpace.addParticleList(0,0,0,('tcphttp', digest ))
        #
        if (DEBUG):
            print('Identifier     :-> TCP/IP HTTP/', digest)
            print('Datatime       :->', datetime)
            print('HTTP Method    :->', method)
            print('HTTP User Agent:->', usergaent)
            print('HTTP Cookie    :->', cookie)
            print('The Full URL   :->', fullurl)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> SYSLOG JSON Event Data Structure is as follows:
    #       {"event": { "syslog": { "_datetime": "Apr 29 15:00:14", "_ident": "3520479944", "_type": "syslog",
    #       "system": { "_type": "name","__text": "server-192.178.67.1" },"process": { "_type": "proc","__text": "systemd:" },
    #       "message": { "_type": "ascii","__text": "Started Vsftpd ftp daemon." }  }, "_datetime": "Apr 29 15:00:14",
    #       "_ident": "2298700593","_type": "syslog" }  }
    #
    def insertSyslog(self, jdata, digest):
        datetime = jdata['syslog']['_datetime']
        system = jdata['syslog']['system']['__text']
        processname = jdata['syslog']['process']['__text'].split('[')[0]
        if ("[" in jdata['syslog']['process']['__text']):
            processid = jdata['syslog']['process']['__text'].split('[')[1].split(']')[0]
        else:
            processid = 'NULL'
        #
        self.DBInsert('syslog', digest, SyslogParticle('syslog', digest, datetime,system, processname, processid, jdata['syslog']))
        #
        self._vectorSpace.addParticleList(0,0,0,('syslog', digest ))
        #
        if (DEBUG):
            print('Identifier     :-> SYSLOG/', digest)
            print('Datatime       :->', datetime)
            print('System         :->', system)
            print('Process Name   :->', processname)
            print('Process ID     :->', processid)
            print('Message        :->', jdata['syslog'])
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> FTPD JSON Event Data Structure is as follows:
    #       {"event": { "ftpd": { "_datetime": "Mar 28 19:59:31", "_ident": "136661321", "_type": "ftpd", 
    #       "transfertime": "5057", "remotehost": { "_type": "ipv4","__text": "192.168.20.10" }, "filesize": "8196242", 
    #       "filename": "/home/ajcblyth/datalog2.tar.gz", "transfertype": "b", "actionflag": "_", "direction": "o", 
    #       "accessmode": "r", "username": "ajcblyth", "servicename": "ftp", "authmethod": "0", "authuserid": "*", 
    #       "status": "c" }, "_datetime": "Mar 28 19:59:31", "_ident": "1290283528", "_type": "ftpd" }  }
    #
    def insertFTPD(self, jdata, digest):
        datetime = jdata['_datetime']
        transfertime = jdata['transfertime']
        remotehost= jdata['remotehost']['__text']
        filesize = jdata['filesize']
        filename = jdata['filename']
        transfertype = jdata['transfertype']
        actionflag = jdata['actionflag']
        direction = jdata['direction']
        accessmode = jdata['accessmode']
        username = jdata['username']
        servicename = jdata['servicename']
        authmethod = jdata['authmethod']
        authuserid = jdata['authuserid']
        status = jdata['status']
        #
        self.DBInsert('ftpd', digest, FTPDParticle('ftpd', digest, datetime, transfertime, remotehost, remotehost,
                                                    filename, transfertype, actionflag, direction, accessmode, 
                                                    username, servicename, authmethod, authuserid, status ))
        #
        self._vectorSpace.addParticleList(0,0,0,('ftpd', digest ))
        #
        if (DEBUG):
            print('Identifier     :-> FTPD/', digest)
            print('Datatime       :->', datetime)
            print('Transfer Time  :->', transfertime)
            print('Remote Host    :->', remotehost)
            print('File Size      :->', filesize)
            print('File Name      :->', filename)
            print('Transfer Type  :->', transfertype)
            print('Action Flag    :->', actionflag)
            print('Direction      :->', direction)
            print('Access Mode    :->', accessmode)
            print('USername       :->', username)
            print('Service Name   :->', servicename)
            print('authmethod     :->', authmethod)
            print('authuserid     :->', authuserid)
            print('Status         :->', status )
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> TCPD JSON Event Data Structure is as follows:
    #       {"event": { "syslog": { "_datetime": "Mar 28 19:23:11", "_ident": "1571927734", "_type": "tcpd",
    #       "system": { "_type": "name","__text": "server-03" },"process": { "_type": "papid","__text": "in.telnetd[1140]:" },
    #       "message": { "_type": "ascii","__text": "Connect from 10.63.148.185" }, "tcpd": { "datetime": { "_type": "std",
    #       "__text": "Mar 28 19:23:11" }, "system": { "_type": "ascii","__text": "server-03" }, 
    #       "process": { "_type": "papid","__text": "in.telnetd[1140]:" }, 
    #       "message": { "_type": "ascii","__text": "10.63.148.185" }, "_datetime": "Mar 28 19:23:11", 
    #       "_ident": "95084021", "_type": "tcpd" } } ,"_datetime": "Mar 28 19:23:11", "_ident": "1577131332", 
    #       "_type": "syslog" }  }
    #
    def insertTCPD(self, jdata, digest):
        datetime = jdata['datetime']['__text']
        system = jdata['system']['__text']
        process = jdata['process']['__text']
        connection = jdata['message']['__text']
        #
        self.DBInsert('tcpd', digest, TCPDParticle('tcpd', digest, datetime, system, process, connection))
        #
        self._vectorSpace.addParticleList(0,0,0,('tcpd', digest ))
        #
        if (DEBUG):
            print('Identifier     :-> TCPD/', digest)
            print('Datatime       :->', datetime)
            print('System         :->', system)
            print('Process Name   :->', process)
            print('Connection     :->', connection)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> SNORT JSON Event Data Structure is as follows:
    #       {"event": { "syslog": { "_datetime": "Apr 29 14:24:14", "_ident": "1121724743", "_type": "snort",
    #       "system": { "_type": "name","__text": "localhost" },"process": { "_type": "proc","__text": "snort:" },
    #       "message": { "_type": "ascii","__text": "[1:1000006:1] Nmap XMAS Tree Scan {TCP} 192.168.1.100:64174 -> 
    #       192.168.1.252:6001" }, "snort": { "_datetime": "Apr 29 14:24:14", "_ident": "1739781287", 
    #       "_type": "snort","datatime": { "_type": "std","__text": "Apr 29 14:24:14" }, 
    #       "system": { "_type": "name","__text": "localhost" },"process": { "_type": "proc","__text": "snort:" },
    #       "version": "[1:1000006:1]", "class": "NULL","priority": "NULL",
    #       "message": { "_type": "ascii","__text": "Nmap XMAS Tree" },
    #       "protocol": "TCP","sourceip": { "_type": "ipv4","__text": "192.168.1.100" }, 
    #       "sourceport": "64174","destinationip": { "_type": "ipv4","__text": "192.168.1.252" }, 
    #       "destinationport": "6001" } },"_datetime": "Apr 29 14:24:14", "_ident": "1011893180", "_type": "syslog" }  }
    #
    def insertSnort(self, jdata, digest):
        datetime = jdata['_datetime']
        system = jdata['system']['__text']
        version = jdata['version']
        classification = jdata['class']
        priority = jdata['priority']
        protocol = jdata['protocol']
        srcport = jdata['sourceport']
        dstport = jdata['destinationport']
        if ("[" in jdata['process']['__text']):
            processname = jdata['process']['__text'].split('[')[0]
            processid = jdata['process']['__text'].split('[')[1].split(']')[0]
        else:
            processname = jdata['process']['__text'].split('[')[0].split(':')[0]
            processid = 'NULL'
        message = jdata['message']['__text']
        src = jdata['sourceip']['__text']
        dst = jdata['destinationip']['__text']
        #
        self.DBInsert('snort', digest, SnortParticle('snort', digest, datetime,
                                            system, processname, processid,
                                            version, classification, priority,
                                            protocol, message, src, srcport,
                                            dst, dstport, jdata))
        #
        self._vectorSpace.addParticleList(0,0,0,('snort', digest ))
        #       
        if (DEBUG):
            print('Identifier      :-> SNORT/', digest)
            print('Datatime        :->', datetime)
            print('System          :->', system)
            print('Process Name    :->', processname)
            print('Process ID      :->', processid)
            print('Version         :->', version)
            print('Classification  :->', classification)
            print('Priority        :->', priority)
            print('Protocol        :->', protocol)
            print('Message         :->', message)
            print('Src IP Address  :->', src)
            print('Src Port        :->', srcport)
            print('DST IP Address  :->', dst)
            print('Dst Port        :->', dstport)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
    #
    # -> SSHD JSON Event Data Structure is as follows:
    #       {"event": { "syslog": { "_datetime": "Apr 29 13:13:35", "_ident": "2289628760", "_type": "sshd",
    #       "system": { "_type": "name","__text": "localhost" },"process": { "_type": "papid","__text": "sshd[11690]:" },
    # ]     "message": { "_type": "ascii","__text": "pam_unix(sshd:session): session closed for user ajcblyth" }, 
    #       "sshd" : {"_datetime": "Apr 29 13:13:35","_ident": "5449253743","_type": "sshd", 
    #       "system": { "_type": "name","__text": "localhost" },"process": { "_type": "papid","__text": "sshd[11690]:" },
    #       "sourceaddr": { "_type": "ipv4","__text": "NULL" },"sourceport": "NULL","username": "NULL",
    #       "message": { "_type": "ascii","__text": "pam_unix(sshd:session): session closed for user ajcblyth" } }  }, 
    #       "_datetime": "Apr 29 13:13:35","_ident": "3159624982","_type": "syslog" }  }
    #
    def insertSSHD(self, jdata, digest): 
        datetime = jdata['_datetime']
        system = jdata['system']['__text']
        process = jdata['process']['__text']
        sourceaddr = jdata['sourceaddr']['__text']
        sourceport = jdata['sourceport']
        username = jdata['username']
        message = jdata['message']['__text']
        #
        self.DBInsert('sshd', digest, SSHDParticle('sshd', digest, datetime, system, process,
                                            sourceaddr, sourceport, username, message))
        #
        self._vectorSpace.addParticleList(0,0,0,('sshd', digest ))
        #
        if (DEBUG):
            print('Identifier      :-> SSHD/', digest)
            print('Datatime        :->', datetime)
            print('System          :->', system)
            print('Process[ID]     :->', process)
            print('Source IP Addr  :->', sourceaddr)
            print('Source Port     :->', sourceport)
            print('Username        :->', username)
            print('Message         :->', message)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return True
    #
    # -> VSFTPD JSON Event Data Structure is as follows:
    #       {"event": { "syslog": { "_datetime": "Apr 29 15:03:19", "_ident": "3176596008", "_type": "vsftpd",
    #       "system": { "_type": "name","__text": "localhost" },"process": { "_type": "papid","__text": "vsftpd[17468]" },
    #       "message": { "_type": "ascii","__text": "[ftp] FTP response: Client ::ffff:192.168.1.100, 221 Goodbye." }, 
    #       "vsftpd": { "_datetime": "Apr 29 15:03:19", "_ident": "4565185013", "_type": "vsftpd","username": "ftp", 
    #       "commandtype": "FTP response","sourceip": "192.168.1.100", "message": "221 Goodbye."  }  },
    #       "_datetime": "Apr 29 15:03:19", "_ident": "1388589004", "_type": "syslog" }  }
    #
    def insertVSFTPD(self, jdata, digest):
        datetime = jdata['_datetime']
        username = jdata['username']
        commandtype = jdata['commandtype']
        sourceip = jdata['sourceip']
        message = jdata['message']
        #
        self.DBInsert('vsftpd', digest, VSFTPDParticle('vsftpd', digest, datetime, sourceip, username,
                                        commandtype , message))
        #
        self._vectorSpace.addParticleList(0,0,0,('vsftpd', digest ))
        #
        if (DEBUG):
            print('Identifier      :-> VSFTPD/', digest)
            print('Datatime        :->', datetime)
            print('Source IP Addr  :->', sourceip)
            print('Username        :->', username)
            print('Command Typpe   :->', commandtype)
            print('Message         :->', message)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return digest
    #
    # -> CEF JSON Event Data Structure is as follows:
    #       "event": { "syslog": { "_datetime": "Mar 28 19:23:07", "_ident": "4029200141", "_type": "cef", 
    #       "system": { "type": "name", "__text": "server-01" }, "process": { "type": "proc", "__text": "CEF:0" }, 
    #       "message": { "type": "proc", "__text": "CEF:0|security|threatmanager|1.0|100|poison ivy trojan infection 
    #       successfully stopped|10|src=10.0.0.1 dst=2.1.2.2 " }, "cef": { "_datetime": "Mar 28 19:23:07", 
    #       "_ident": "7563964276", "_type": "cef", "version": "CEF:0", 
    #       "deviceinfo": "security threatmanager 1.0", "signature": "100", 
    #       "name": { "type": "ascii", "__text": "poison ivy trojan infection successfully stopped" }, "severity": "10", 
    #       "exenstions": { "type": "ascii", "__text": "src=10.0.0.1 dst=2.1.2.2 " } } }, 
    #       "_datetime": "Mar 28 19:23:07", "_ident": "3534764134", "_type": "syslog" } }
    #
    def insertCEF(self, jdata, digest):
        datetime = jdata['_datetime']
        version = jdata['version']
        deviceinfo = jdata['deviceinfo']
        signature = jdata['signature']
        name = jdata['name']['__text']
        severity = jdata['severity']
        exenstions = jdata['exenstions']['__text']

        #
        self.DBInsert('cef', digest, CEFParticle('cef', digest, datetime, version, deviceinfo,
                                        signature, name, severity, exenstions))
        #
        self._vectorSpace.addParticleList(0,0,0,('cef', digest ))
        #
        if (DEBUG):
            print('Identifier      :-> CEF/', digest)
            print('Datatime        :->', datetime)
            print('Version         :->', version)
            print('Device Info     :->', deviceinfo)
            print('Signature       :->', signature)
            print('Name            :->', name)
            print('Severity        :->', severity)
            print('Exenstion       :->', exenstions)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return digest
    #
    # -> DNS JSON Event Data Structure is as follows:
    #       {"event": { "dns": { "_datetime": "27-Mar-2019 17:00:36.097", "_ident": "3347987721", "_type": "dns", 
    #       "requester": "10.63.148.85", "request": "www.adisa.global", "requesttype": "A" }, 
    #       "_datetime": "27-Mar-2019 17:00:36.097", "_ident": "1514625769", "_type": "dns" } }
    #
    def insertDNS(self, jdata, digest):
        datetime = jdata['_datetime']
        requester = jdata['requester']
        request = jdata['request']
        requesttype = jdata['requesttype']
        #
        self.DBInsert('dns', digest, DNSParticle('dns', digest, datetime, requester, request, requesttype))
        #
        self._vectorSpace.addParticleList(0,0,0,('dns', digest ))
        #
        if (DEBUG):
            print('Identifier      :-> DNS/', digest)
            print('Datatime        :->', datetime)
            print('requester       :->', requester)
            print('request         :->', request)
            print('requesttype     :->', requesttype)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return digest
        #
        # -> NCSA JSON Event Data Structure is as follows:
        #       {"event": { "nsca": { "_datetime": "[01/Jan/2017:09:00:00 +0000]", "_ident": "1242662182", 
        #       "_type": "nsca", "client": { "_type": "ipv4", "__text": "66.249.66.1"  }, "userid": "-", "user": "-", 
        #       "request": { "_type": "ascii", "__text": "GET /contact.html"  }, "protocol": "HTTP/1.1", 
        #       "statuscode": "200",  "size": "250"  }, "_datetime": "[01/Jan/2017:09:00:00 +0000]", 
        #       "_ident": "406332477", "_type": "nsca" }  }
        #
    def insertNSCA(self, jdata, digest):
        datetime = jdata['_datetime']
        client = jdata['client']['__text']
        userid = jdata['userid']
        user = jdata['user']
        request = jdata['request']['__text']
        protocol= jdata['protocol']
        statuscode = jdata['statuscode']
        size = jdata['size']
        #
        self.DBInsert('nsca', digest, NCSAParticle('nsca', digest, datetime, client, userid, user, request, 
                                                protocol, statuscode, size))
        #
        self._vectorSpace.addParticleList(0,0,0,('nsca', digest ))
        #
        if (DEBUG):
            print('Identifier      :-> NCSA/', digest)
            print('Datatime        :->', datetime)
            print('Client          :->', client)
            print('Userid          :->', userid)
            print('User            :->', user)
            print('Request         :->', request)
            print('Protocol        :->', protocol)
            print('Statuscode      :->', statuscode)
            print('Size            :->', size)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return digest
    #
    # -> NetFlow JSON Event Data Structure is as follows:
    #       {"event": { "netflow": { "_datetime": "Mar 28 19:23:07", "_ident": "1029384756", "_type": "netflow",
    #       "duration": "00:57:37", "protocol": "TCP", "sourceip": "192.168.30.142", "sourceport": "22", 
    #       "destinationip": "192.168.30.142", "destport": "22", "packets": "1029", "bytes": "901827" },  
    #       "_datetime": "Mar 28 19:23:07", "_ident": "1029384757", "_type": "netflow"} }
    #
    def insertNetFlow(self, jdata, digest):
        datetime = jdata['_datetime']
        duration = jdata['duration']
        protocol = jdata['protocol']
        sourceip = jdata['sourceip']
        sourceport = jdata['sourceport']
        destinationip = jdata['destinationip']
        destport = jdata['destport']
        packets = jdata['packets']
        pbytes = jdata['bytes']
        #
        self.DBInsert('netflow', digest, NetFlowParticle('netflow', digest, datetime, duration, protocol, sourceip, 
                                                    sourceport, destinationip, destport, packets, pbytes))
        #
        self._vectorSpace.addParticleList(0,0,0,('netflow', digest ))
        #
        if (DEBUG):
            print('Identifier      :-> NetFlow/', digest)
            print('Datatime        :->', datetime)
            print('Duration        :->', duration)
            print('Prolocol        :->', protocol)
            print('Source IP       :->', sourceip)
            print('Source Port     :->', sourceport)
            print('Destination IP  :->', destinationip)
            print('Destination Port:->', destport)
            print('Packets         :->', packets)
            print('Bytes of Data   :->', pbytes)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return digest
    #
    # -> WindowsEvent JSON Event Data Structure is as follows:
    #       {"event": { "evt": { "_datetime": "2019-03-28T19:23:07.182918260Z", "_ident": "7856384756", "_type": "evt",
    #       "source": "Security", "eventid": "4624", "datetime": "2019-03-28T19:23:07.182918260Z", "user": "ajcblyth", 
    #       "computer": "dc1.adisa.global", "processid": "61762", "threadid": "1920", "keywords": "logon" },  
    #       "_datetime": "Mar 28 19:23:07", "_ident": "7856384757", "_type": "evt"} }
    #
    def insertWindowsEvent(self, jdata, digest):
        datetime = jdata['_datetime']
        source = jdata['source']
        eventid=  jdata['eventid']
        evtdatetime = jdata['datetime']
        user = jdata['user']
        computer = jdata['computer']
        processid = jdata['processid']
        threadid = jdata['threadid']
        keywords = jdata['keywords']
        #
        self.DBInsert('evt', digest, EVTParticle('evt', digest, datetime,source, eventid, evtdatetime, user,
                                                computer, processid, threadid, keywords))
        #
        self._vectorSpace.addParticleList(0,0,0,('evt', digest ))
        #
        if (DEBUG):
            print('Identifier      :-> Microsoft Windows Event/', digest)
            print('Datatime        :->', digest)
            print('Event Source    :->', source)
            print('Event ID        :->', eventid)
            print('Event Date/Time :->', evtdatetime)
            print('User            :->', user)
            print('Computer        :->', computer)
            print('Process ID      :->', processid)
            print('Thread ID       :->', threadid)
            print('Keyword(s)      :->', keywords)
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return digest
    #
    #
    #
    def insertSTIX(self, jdata, digest):
        jsdata = {}
        jsdata['type'] = "NONE"
        jsdata['name'] = "NONE"
        jsdata['id'] = "NONE"
        jsdata['created'] = "NONE"
        jsdata['modified'] = "NONE"
        jsdata['description'] = "NONE"
        jsdata['pattern'] = "NONE"
        jsdata['kill_chain_phases'] = ['NONE']
        jsdata['labels'] = ['NONE']
        jsdata['external_references'] = ['NONE']
        jsdata['relation_list'] = ['NONE']
        jsdata['relationship_type'] = "NONE"
        jsdata['source_ref'] = "NONE"
        jsdata['target_ref'] = "NONE"
        #
        for k in jdata.keys():
             jsdata[k] = jdata[k]
        #
        self.DBInsert('stix', jsdata['id'], STIXParticle(jsdata['type'], jsdata['name'], 
                                jsdata['id'], jsdata['created'], jsdata['modified'], 
                                jsdata['description'], jsdata['pattern'], jsdata['kill_chain_phases'],
                                jsdata['labels'], jsdata['external_references'], 
                                jsdata['relation_list'], jsdata['relationship_type'], jsdata['source_ref'],
                                jsdata['target_ref']))
        #
        if(jsdata['external_references'][0] != 'NONE'):
            prediction = PredictionParticle(jsdata['type'], jsdata['name'], jsdata['id'], jsdata['modified'])
            for (name) in jsdata['external_references']:
                if (name['source_name'] == 'CAPEC'): prediction._references.append(name)
                if (name['source_name'] == 'CVE'): prediction._references.append(name)
            self.DBInsert('prediction', jsdata['id'], prediction)
            self._vectorSpace.addParticleList(0,0,0,('prediction', digest ))
        #
        if (DEBUG):
            print('STIX Object Type:                  ', jsdata['type'])
            print('STIX Object Name:                  ', jsdata['name'])
            print('STIX Object Decsription:           ', jsdata['description'])
            print('STIX Object Identifier:            ', jsdata['id'])
            print('STIX Object Creation Time:         ', jsdata['created'])
            print('STIX Object Modified Time:         ', jsdata['modified'])
            print('STIX Object Pattern:               ', jsdata['pattern'])
            print('STIX Object Label(s):              ', jsdata['labels'])
            print('STIX Object Kill Chain Phase(s):   ', jsdata['kill_chain_phases'])
            print('STIX Object External Reference(s): ', jsdata['external_references'])
            print('STIX Object Relationship Type:     ', jsdata['relationship_type'])
            print('STIX Object Relationship Source:   ', jsdata['source_ref'])
            print('STIX Object Relationship target:   ', jsdata['target_ref'])
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #
        return digest
#
# -> END OF FILE
#
