#
#
#
#
#
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
#
from stixparticle import STIXParticle
#
import json
import hashlib
import random
#
from Database import DB
from Debuggy import debugger
#
DEBUG = False
#
#
# -> This is the addSTIX JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def addSTIX(request):
    result = "{ 'retrunValue' : 'True' }"
    jdata = json.loads(request)
    for j in jdata['objects']:
        _ = DataBase.insertSTIX(j, j['id'])
    return result 
#
#  -> This is the addParticle JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def addParticle(request):
    result = "{ 'retrunValue' : 'True' }"
    jdata = json.loads(request)
    if str(jdata) != '{}':
        if (jdata['event'] == 'debugger'):
            result = debugger(jdata, DataBase) 
        else:
            eventdigest = jdata['event']['_ident']
            _ = DataBase.insertEvent(jdata, eventdigest)
            #
            #
            #
            if (jdata['event']['_type'] == 'syslog'):
                jdata = jdata['event']
                syslogdigest = jdata['syslog']['_ident'] + str(random.random())[2:]
                _ = DataBase.insertSyslog(jdata, syslogdigest)
                _ = DataBase.setSubParticle('event', eventdigest, syslogdigest, 'syslog')
                _ = DataBase.setSuperParticle('syslog', syslogdigest, eventdigest, 'event')
                #
                #
                #
                if (jdata['syslog']['_type'] == 'snort'):
                    jndata = jdata['syslog']['snort']
                    snidentifier = jdata['syslog']['snort']['_ident'] + str(random.random())[2:]
                    _ = DataBase.insertSnort(jndata, snidentifier)
                    _ = DataBase.setSubParticle('syslog', syslogdigest, snidentifier, 'snort')
                    _ = DataBase.setSuperParticle('snort', snidentifier, syslogdigest, 'syslog')
                #
                #
                #
                elif (jdata['syslog']['_type'] == 'sshd'):
                    jndata = jdata['syslog']['sshd']
                    sshidentifier = jdata['syslog']['sshd']['_ident'] + str(random.random())[2:]
                    _ = DataBase.insertSSHD(jndata, sshidentifier)
                    _ = DataBase.setSubParticle('syslog', syslogdigest, sshidentifier, 'sshd')
                    _ = DataBase.setSuperParticle('sshd', sshidentifier, syslogdigest, 'syslog')
                #
                #
                #
                elif (jdata['syslog']['_type'] == 'vsftpd'):
                    jndata = jdata['syslog']['vsftpd']
                    jndata = jdata['syslog']['vsftpd']
                    vsftpdidentifier = jdata['syslog']['vsftpd']['_ident'] + str(random.random())[2:]
                    _ = DataBase.insertVSFTPD(jndata, vsftpdidentifier)
                    _ = DataBase.setSubParticle('syslog', syslogdigest, vsftpdidentifier, 'vsftpd')
                    _ = DataBase.setSuperParticle('vsftpd', vsftpdidentifier, syslogdigest, 'syslog')
                #
                #
                #
                elif (jdata['syslog']['_type'] == 'tcpd'):
                    jndata = jdata['syslog']['tcpd']
                    tcpdidentifier = jdata['syslog']['tcpd']['_ident'] + str(random.random())[2:]
                    _ = DataBase.insertTCPD(jndata, tcpdidentifier) 
                    _ = DataBase.setSubParticle('syslog', syslogdigest, tcpdidentifier, 'tcpd')
                    _ = DataBase.setSuperParticle('tcpd', tcpdidentifier, syslogdigest, 'syslog')
                #
                #
                #
                elif (jdata['syslog']['_type'] == 'cef'):
                    jndata = jdata['syslog']['cef']
                    cefidentifier = jdata['syslog']['cef']['_ident'] + str(random.random())[2:]
                    _ = DataBase.insertCEF(jndata, cefidentifier) 
                    _ = DataBase.setSubParticle('syslog', syslogdigest, cefidentifier, 'cef')
                    _ = DataBase.setSuperParticle('cef', cefidentifier, syslogdigest, 'syslog')
            #
            #
            #
            elif (jdata['event']['_type'] == 'dns'):
                jndata = jdata['event']['dns']
                dnsidentifier = jdata['event']['dns']['_ident'] + str(random.random())[2:]
                eventdigest = jdata['event']['_ident']
                _ = DataBase.insertDNS(jndata, dnsidentifier) 
                _ = DataBase.setSubParticle('event', eventdigest, dnsidentifier, 'dns')
                _ = DataBase.setSuperParticle('dns', dnsidentifier, eventdigest, 'event')
            #
            #
            #
            elif (jdata['event']['_type'] == 'ftpd'):
                jndata = jdata['event']['ftpd']
                ftpdidentifier = jdata['event']['ftpd']['_ident'] + str(random.random())[2:]
                eventdigest = jdata['event']['_ident']
                _ = DataBase.insertFTPD(jndata, ftpdidentifier)
                _ = DataBase.setSubParticle('event', eventdigest, ftpdidentifier, 'ftpd')
                _ = DataBase.setSuperParticle('ftpd', ftpdidentifier, eventdigest, 'event')
            #
            #
            #
            elif (jdata['event']['_type'] == 'nsca'):
                jndata = jdata['event']['nsca']
                nscaidentifier = jdata['event']['nsca']['_ident'] + str(random.random())[2:]
                eventdigest = jdata['event']['_ident']
                _ = DataBase.insertNSCA(jndata, nscaidentifier)
                _ = DataBase.setSubParticle('event', eventdigest, nscaidentifier, 'nsca')
                _ = DataBase.setSuperParticle('nsca', nscaidentifier, eventdigest, 'event')
            #
            #
            #
            elif (jdata['event']['_type'] == 'netflow'):
                jndata = jdata['event']['netflow']
                netflowidentifier = jdata['event']['netflow']['_ident'] + str(random.random())[2:]
                eventdigest = jdata['event']['_ident']
                _ = DataBase.insertNetFlow(jndata, netflowidentifier)
                _ = DataBase.setSubParticle('event', eventdigest, netflowidentifier, 'netflow')
                _ = DataBase.setSuperParticle('netflow', netflowidentifier, eventdigest, 'event')
            #
            #
            #
            elif (jdata['event']['_type'] == 'evt'):
                jndata = jdata['event']['evt']
                evtidentifier = jdata['event']['evt']['_ident'] + str(random.random())[2:]
                eventdigest = jdata['event']['_ident']
                _ = DataBase.insertWindowsEvent(jndata, evtidentifier)
                _ = DataBase.setSubParticle('event', eventdigest, evtidentifier, 'evt')
                _ = DataBase.setSuperParticle('evt', evtidentifier, eventdigest, 'event')
            #
            #
            #
            elif (jdata['event']['_type'] == 'ipv4'):
                jndata = jdata['event']
                ipv4identifier = jdata['event']['_ident'] + str(random.random())[2:]
                eventdigest = jdata['event']['_ident']
                print(eventdigest , ' :-> ', ipv4identifier)
                _ = DataBase.insertIPv4(jndata, ipv4identifier)
                _ = DataBase.setSubParticle('event', eventdigest, ipv4identifier, 'ipv4')
                _ = DataBase.setSuperParticle('ipv4', ipv4identifier, eventdigest, 'event')
                #
                #
                #
                if (jndata['ipv4']['_type'] == 'tcp'):
                    jndata = jndata['ipv4']['tcp']
                    tcpidentifier = jndata['_ident'] + str(random.random())[2:]
                    _ = DataBase.insertIPTCP(jndata, tcpidentifier)
                    _ = DataBase.setSubParticle('ipv4', ipv4identifier, tcpidentifier, 'tcp')
                    _ = DataBase.setSuperParticle('tcp', tcpidentifier, ipv4identifier, 'ipv4')
                    #
                    #
                    #
                    if (jndata['_type'] == 'http'):
                        jndata = jndata['http']
                        httpidentifier = jndata['_ident'] + str(random.random())[2:]
                        _ = DataBase.insertIPTCPHTTP(jndata, httpidentifier)
                        _ = DataBase.setSubParticle('tcp', tcpidentifier, httpidentifier, 'tcphttp')
                        _ = DataBase.setSuperParticle('tcphttp', httpidentifier, tcpidentifier, 'tcp')
                #
                #
                #
                elif (jndata['ipv4']['_type'] == 'udp'):
                    jndata = jndata['ipv4']['udp']
                    udpidentifier = jndata['_ident'] + str(random.random())[2:]
                    _ = DataBase.insertIPUDP(jndata, udpidentifier)
                    _ = DataBase.setSubParticle('ipv4', ipv4identifier, udpidentifier, 'udp')
                    _ = DataBase.setSuperParticle('udp', udpidentifier, ipv4identifier, 'ipv4')
                #
                #
                #
                elif (jndata['ipv4']['_type'] == 'icmp'):
                    jndata = jndata['ipv4']['icmp']
                    icmpidentifier = jndata['_ident'] + str(random.random())[2:]
                    _ = DataBase.insertIPICMP(jndata, icmpidentifier)
                    _ = DataBase.setSubParticle('ipv4', ipv4identifier, icmpidentifier, 'icmp')
                    _ = DataBase.setSuperParticle('icmp', icmpidentifier, ipv4identifier, 'ipv4')
    #
    # 
    #
    return result
#
# -> This is the updatePredictionPartcile JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def updatePredictionPartcile(request):
    jdata = json.loads(request)
    pT = jdata['particleType']
    pID = jdata['particleID']
    return DataBase.updatePredictionPartcile(pT, pID)
#
# -> This is the vectorSpaceGetAllSTIXParticle JSON RPC Disptach Handler function.
#
@dispatcher.add_method 
def vectorSpaceGetAllSTIXParticle(request):
    return str(DataBase.vectorSpaceGetAllSTIXParticle())
#
# -> This is the vectorSpaceGetAllEventParticle JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def vectorSpaceGetAllEventParticle(request):
    return str(DataBase.vectorSpaceGetAllEventParticle()) 
#
# -> This is the distributePredictionParticle JSON RPC Disptach Handler function.
# 
@dispatcher.add_method
def distributePredictionParticle(request):
    if (DataBase.distributePredictionParticleinGVSM()):
        result = "{ 'retrunValue' : 'True' }"
    else:
        result = "{ 'retrunValue' : 'False' }"
    return result
#
#  -> This is the vectorMatrixUpdateEventParticle JSON RPC Disptach Handler function.
# 
def vectorMatrixUpdateEventParticle(request):
    jdata = json.loads(request)
    uT = jdata['utility']
    pT = 'prediction'
    pID = jdata['predictionID']
    eT = jdata['particleType']
    eID = jdata['particleID']
    return DataBase.vectorMatrixUpdateEventParticle(uT, pT, pID, eT ,eID) 
#
# -> This is the vectorSpaceDecayParticle JSON RPC Disptach Handler function.
# 
def vectorSpaceDecayParticle(request):
    jdata = json.loads(request)
    pT = jdata['particleType']
    pID = jdata['particleID']
    return DataBase.vectorSpaceDecayParticle(pT, pID)
# 
# -> This is the getPredictionParticlParameters JSON RPC Disptach Handler function.
# 
def getPredictionParticlParameters(request):
    jdata = json.loads(request)
    pT = jdata['particleType']
    pID = jdata['particleID']
    return DataBase.getPredictionParticlParameters(pT, pID)
#
# -> This is the vectorSpaceGetParticlePosiution JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def vectorSpaceGetParticlePosition(request):
    jdata = json.loads(request)
    pT = jdata['particleType']
    pID = jdata['particleID']
    return DataBase.vectorSpaceGetParticlePosition(pT, pID)
#
# -> This is the vectorSpaceAddParticleList JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def vectorSpaceAddParticleList(request):
    _ = json.loads(request)
    result = "{ 'retrunValue' : 'True' }"
    return result
#
# -> This is the vectorSpaceDelParticleList JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def vectorSpaceDelParticleList(request):
    _ = json.loads(request)
    result = "{ 'retrunValue' : 'True' }"
    return result
# 
# -> This is the vectorSpaceUpdateParticleLocation JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def vectorSpaceUpdateParticleLocation(request):
    jdata = json.loads(request)
    #
    if (DataBase.vectorSpaceUpdateParticleLocation(jdata['x'],jdata['y'],jdata['z'],jdata['type'],jdata['id'])):
        result = "{ 'retrunValue' : 'True' }"
    else:
        result = "{ 'retrunValue' : 'False' }"
    #
    return result
# 
# -> This is the getParticle JSON RPC Disptach Handler function.
#
def getParticle(request):
    jdata = json.loads(request)
    pT = jdata['particleType']
    pID = jdata['particleID']
    return DataBase.getParticle(pT, pID)
#
#  -> This is the addDataParticle JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def addDataParticle(request):
    jdata = json.loads(request)
    DataBase.insertDataParticle(jdata) 
    result = "{ 'retrunValue' : 'True' }"
    return result
#
#  -> This is the getDataParticleList JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getDataParticleList(request):
    jdata = json.loads(request)
    result = DataBase.getDataParticleList(jdata) 
    return str(result)
#
#  -> This is the getAllSyslogParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllSyslogParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllSyslogParticles(jdata) 
    return str(result)
#
#  -> This is the getAllSnortParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllSnortParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllSnortParticles(jdata) 
    return str(result)
#
#  -> This is the getAllSSHDParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllSSHDParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllSSHDParticles(jdata) 
    return str(result)
#
#  -> This is the getAllTCPDParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllTCPDParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllTCPDParticles(jdata) 
    return str(result)
#
#  -> This is the getAllCEFarticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllCEFarticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllCEFarticles(jdata) 
    return str(result)
#
#  -> This is the getAllVSFTPDParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllVSFTPDParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllVSFTPDParticles(jdata) 
    return str(result)
#
#  -> This is getAllDNSParticles HHH JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllDNSParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllDNSParticles(jdata) 
    return str(result)
#
#  -> This is the getAllNCSAParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllNCSAParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllNCSAParticles(jdata) 
    return str(result)
#
#  -> This is the getAllNetFlowParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllNetFlowParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllNetFlowParticles(jdata) 
    return str(result)
#
#  -> This is the getAllFTPDParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllFTPDParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllFTPDParticles(jdata) 
    return str(result)
#
#  -> This is the getAllEvtXParticles JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def getAllEvtXParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllEvtXParticles(jdata) 
    return str(result)
# 
# -> This is the getAllSTIXParticles JSON RPC Disptach Handler function.
# 
def getAllSTIXParticles(request):
    jdata = json.loads(request)
    result = DataBase.getAllSTIXParticles(jdata) 
    return str(result)
#
# -> This is the cacheGarbageCollection JSON RPC Disptach Handler function.
#
@dispatcher.add_method
def cacheGarbageCollection(request):
    jdata = json.loads(request)
    result = "{ 'retrunValue' : 'True' }"
    return result
# 
# -> This is the RPC event request handler for the JSON RPC functions.
# 
@Request.application
def application(request):
    # 
    dispatcher["addParticle"] = lambda s : addParticle(s)
    dispatcher["addDataParticle"] = lambda s : addDataParticle(s)
    dispatcher["getParticle"] = lambda s : getParticle(s)
    dispatcher["addStixObject"] = lambda s : addSTIX(s)
    dispatcher["getDataParticleList"] = lambda s : getDataParticleList(s)
    dispatcher["vectorMatrixUpdateEventParticle"] = lambda s : vectorMatrixUpdateEventParticle(s)
    dispatcher["GetPredictionParticlParameters"] = lambda s : getPredictionParticlParameters(s)
    dispatcher["vectorSpaceAddParticleList"] = lambda s : vectorSpaceAddParticleList(s)
    dispatcher["vectorSpaceDelParticleList"] = lambda s : vectorSpaceDelParticleList(s)
    dispatcher["vectorSpaceGetAllEventParticle"] = lambda s : vectorSpaceGetAllEventParticle(s)
    dispatcher["vectorSpaceGetAllSTIXParticle"] = lambda s : vectorSpaceGetAllSTIXParticle(s)
    dispatcher["vectorSpaceUpdateParticle"] = lambda s : vectorSpaceUpdateParticleLocation(s)
    dispatcher["distributePredictionParticle"] = lambda s : distributePredictionParticle(s)
    dispatcher["updatePredictionPartcile"] = lambda s : updatePredictionPartcile(s)
    dispatcher["vectorSpaceDecayParticle"] = lambda s : vectorSpaceDecayParticle(s)
    dispatcher["getAllSyslogParticles"] = lambda s : getAllSyslogParticles(s)
    dispatcher["getAllSnortParticles"] = lambda s : getAllSnortParticles(s)
    dispatcher["getAllTCPDParticles"] = lambda s : getAllTCPDParticles(s)
    dispatcher["getAllSSHDParticles"] = lambda s : getAllSSHDParticles(s)
    dispatcher["getAllCEFarticles"] = lambda s : getAllCEFarticles(s)
    dispatcher["getAllVSFTPDParticles"] = lambda s : getAllVSFTPDParticles(s)
    dispatcher["getAllDNSParticles"] = lambda s : getAllDNSParticles(s)
    dispatcher["getAllNCSAParticles"] = lambda s : getAllNCSAParticles(s)
    dispatcher["getAllNetFlowParticles"] = lambda s : getAllNetFlowParticles(s)
    dispatcher["getAllFTPDParticles"] = lambda s : getAllFTPDParticles(s)
    dispatcher["getAllEvtXParticles"] = lambda s : getAllEvtXParticles(s)
    dispatcher["getAllSTIXParticles"] = lambda s : getAllSTIXParticles(s)
    dispatcher["cacheGarbageCollection"] = lambda s : cacheGarbageCollection(s)
    dispatcher["vectorSpaceGetParticlePosition"] = lambda s : vectorSpaceGetParticlePosition(s)
    #
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    #
    return Response(response.json, mimetype='application/json')
#
# -> This the command to invoke the database from the command line.
# 
if __name__ == '__main__':
    DataBase = DB()
    run_simple('127.0.0.1', 4000, application)
#
# -> The End of the Request/Dispatch Handler Definitions for the JSON RPC.
#
