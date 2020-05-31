#
# This the Utility Function Definition
#           Date:   19th April 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
# 
# 
# -> This is the import section for the required Python system function.
import random
import math
import xmltodict
import os.path
import json
import sys
import ast
import binascii
import requests
# -> This is the import section for the required Swarm Partciles function.
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
#
# -> This the Utility Function Definition
#
class Utility():
    #
    # ->    This is the constructor function for the Class/Object-Type: Utility ()
    #
    def __init__(self):
        self._DEBUG     = False 
        self._utility   = 0
        self._dirName   = '' 
        self._G         = 6.67408 * math.pow(10, -11)
        self._xdoc      = {}
        self._server    = '127.0.0.1'
        self._port      = 4000
        self._rpc       = 'jsonrpc'
        self._url       = 'http://' + self._server + ':' + str(self._port) + '/' + self._rpc
        self._headers   = {'content-type': 'application/json'}
        self._jsonrpcid = 1
        self._stack     = []
        self._dataPList = []
    #
    # ->    This is the reset function for the Class/Object-Type: Utility ()
    #
    def reset(self):
        self._DEBUG     = False 
        self._utility   = 0
        self._dirName   = '' 
        self._G         = 6.67408 * math.pow(10, -11)
        self._server    = '127.0.0.1'
        self._port      = 4000
        self._rpc       = 'jsonrpc'
        self._url       = 'http://' + self._server + ':' + str(self._port) + '/' + self._rpc
        self._headers   = {'content-type': 'application/json'}
        self._jsonrpcid = 1
        self._stack     = []
        #
        return True
    # 
    # ->    This is the __LoadDataParticleList__ function for the Class/Object-Type: Utility ()
    # 
    def __LoadDataParticleList__(self):
        self._dataPList = self.jsonRPC('{}','getDataParticleList')
        return True

    # 
    # ->    This is the __XMLLoad__ function for the Class/Object-Type: Utility ()
    #
    def __XMLLoad__(self):
        with open(self._dirName + '/utility.xml') as fd:
            try:
                self._xdoc = xmltodict.parse(fd.read())
                print('XML Utility File Successfully Loaded..............................[OK]')
                return True
            except:
                print('XML Utility File Successfully Loaded............................[FAIL]')
                return False
    #
    # ->    This is the __setDirname__ function for the Class/Object-Type: Utility ()
    #
    def __setDirName__(self,dName): 
        self._dirName =  dName
        if (os.path.exists(self._dirName + '/utility.xml')): self.__XMLLoad__()
    #
    # ->    This is the distance function for the Class/Object-Type: Utility ()
    #
    def __distance__(self, x1, y1, x2, y2): 
        return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    # 
    # 
    # 
    # ->    This is the jsonRPC function for the Class/Object-Type: Utility().
    #       Where: 
    #               jsonparams           -   Is the RPC parameters.
    #               rpcName              -   Is the RPC Name.
    #
    def jsonRPC(self, jsonparams, rpcName):
        # -> Marshall the JSON RPC Components
        payload = {
            "method": rpcName,
            "params": [jsonparams],
            "jsonrpc": "2.0",
            "id": self._jsonrpcid, }
        self._jsonrpcid = self._jsonrpcid + 1
        # -> Make/execute the JSON RPC
        if (self._DEBUG ): print(payload)
        response = requests.post(self._url, data=json.dumps(payload), headers=self._headers).json()
        #
        return response
    # 
    # ->    This is the _getOpDataPrediction function for the Class/Object-Type: Utility ()
    #       Where: 
    #               opAttribute         -   Is the partcile attribute to return.
    #               jsonEventData       -   Is the JSON prediction/STIX particle data.
    # 
    def _getOpDataPrediction(self, opAttribute, jsonPredictionData):
        #
        resultList = []
        #
        if (opAttribute in jsonPredictionData.keys()): resultList.append(jsonPredictionData[opAttribute])
        #
        else : 
            for xRef in jsonPredictionData['_references']:
                if (opAttribute in xRef.keys()): resultList.append(xRef[opAttribute])
        #
        return resultList
    # 
    # ->    This is the _getOpData function for the Class/Object-Type: Utility ()
    #       Where: 
    #               opAttribute         -   Is the partcile attribute to return.
    #               jsonEventData       -   Is the JSON event particle data.
    # 
    def _getOpDataEvent(self, opAttribute, jsonData):
        #
        jData = jsonData
        jKeys = jsonData.keys()
        resultList = []
        #
        while(len(jKeys) != 0):
            if (opAttribute in jKeys):  
                resultList.append(jData[opAttribute])
            try:
                jData = jData['_jsondata']
                jKeys = jData.keys()
            except:
                jKeys = []
        #
        return resultList
    #
    # ->    This is the _evalMatch function for the Class/Object-Type: Utility ()
    #       Where: 
    #               xMatch              -   Is the XML Match Statement.
    #               jsonPredictionData  -   Is the JSON prediction particle.
    #               jsonEventData       -   Is the JSON event particle.
    # 
    def _evalMatch(self, xMatch, jsonPredictionData, jsonEventData):
        try:
            opObject    = xMatch['@oprand'].split(':-')[0]    # The Object is    : data
            opAttribute = xMatch['@oprand'].split(':-')[1]    # The Attribute is : external_id
            opFunction  = xMatch['@op']                       # The Function is  : EQU
            opType      = xMatch['@type']                     # The OP Type is   : string
            opValue     = xMatch['#text']                     # The Value is     : Windows 10
            # 
            # Is the opObject type an 'event' or a 'prediction' partcile?
            if (opObject == 'event' or opObject == 'pred'):
                if (opObject == 'event'): 
                    opDataList = self._getOpDataEvent(opAttribute, jsonEventData)
                else:
                    opDataList = self._getOpDataPrediction(opAttribute, jsonPredictionData)
                # 
                for opData in opDataList:
                    if ( str(type(opData)) == '<class \'dict\'>'):
                        opType = opData['_type']
                        opData = opData['__text']
                    # 
                    # Is the oprand being evaluated of type IPPV4 Python type
                    if (opType == 'ipv4'):
                        # 
                        # Is the Operand data EQUAL to the Operand Value?
                        if (opFunction == 'EQU'): 
                            if (str(opData) == str(opValue)): return True
                    #
                    # Is the oprand being evaluated of type INTEGER Python type
                    if (opType == 'int'):
                        #
                        # Concvert NULL integers into the value -1
                        if opData == 'NULL': opData = -1
                        if opValue == 'NULL': opValue = -1
                        #
                        # Is the Operand data EQUAL to the Operand Value?
                        if (opFunction == 'EQU'):  
                            return (int(opData) == int(opValue))
                        # 
                        # Is the Operand data NOT EQUAL to the Operand Value?
                        if (opFunction == 'NQU'): 
                            if (str(opData) != str(opValue)): return True 
                        # 
                        # Is the Operand data LESS THAN to the Operand Value?
                        if (opFunction == 'LES'): return (int(opData) < int(opValue))
                        # 
                        # Is the Operand data LESS THAN AND EQUAL TO to the Operand Value?
                        if (opFunction == 'LSE'): return (int(opData) <= int(opValue))
                        # 
                        # Is the Operand data GREATER THAN to the Operand Value?
                        if (opFunction == 'GRT'): return (int(opData) > int(opValue))
                        # 
                        # Is the Operand data GREATER THAN AND QUAL TOc to the Operand Value?
                        if (opFunction == 'GTE'): return (int(opData) >= int(opValue))
                    # 
                    # Is the oprand being evaluated of type STRING Python Type
                    elif (opType == 'string'):
                        # 
                        # Is the Operand data EQUAL to the Operand Value?
                        if (opFunction == 'EQU'): 
                            if (str(opData) == str(opValue)): return True    
                        # 
                        # Is the Operand data NOT EQUAL to the Operand Value?
                        if (opFunction == 'NQU'): 
                            if (str(opData) != str(opValue)): return True    
                    # Is the oprand being evaluated of type FLOAT Python type
                    elif (opType == 'float'):
                        #
                        # Concvert NULL integers into the value -1
                        if opData == 'NULL': opData = -1
                        if opValue == 'NULL': opValue = -1
                        # 
                        # Is the Operand data EQUAL to the Operand Value?
                        if (opFunction == 'EQU'): return (float(opData) == float(opValue))
                        # 
                        # Is the Operand data NOT EQUAL to the Operand Value?
                        if (opFunction == 'NQU'): return (float(opData) != float(opValue))
                        # 
                        # Is the Operand data LESS THAN to the Operand Value?
                        if (opFunction == 'LES'): return (float(opData) < float(opValue))
                        # 
                        # Is the Operand data LESS THAN AND EQUAL TO to the Operand Value?
                        if (opFunction == 'LSE'): return (float(opData) <= float(opValue))
                        # 
                        # Is the Operand data GREATER THAN to the Operand Value?
                        if (opFunction == 'GRT'): return (float(opData) > float(opValue))
                        # 
                        # Is the Operand data GREATER THAN AND QUAL TOc to the Operand Value?
                        if (opFunction == 'GTE'): return (float(opData) >= float(opValue))
                #
                #
                return False
            #
            # Is the opObject type an 'data' partcile? 
            elif (opObject == 'data'):
                #
                result = False
                if (opAttribute == 'external_id'): opAttribute = '_data'
                astJSON = ast.literal_eval(self._dataPList['result'])
                #
                for dataPartcile in astJSON:
                    jData = json.loads(dataPartcile)
                    JD = binascii.unhexlify(jData[opAttribute].encode('utf-8')).decode('utf-8')
                    #
                    if (opFunction == 'EQU'):                           # A EQU B -> A == B
                        for dataP in ast.literal_eval(JD):
                            if (opValue == dataP): result = True
                    if (opFunction == 'NQU'):                           # A NQU B -> A != B
                        for dataP in ast.literal_eval(JD):
                            if (opValue != dataP): result = True
                #
                return result
            else: 
                #
                return result
        # 
        # -> Catch exceptions in the execution o fthe _evalMatch and return FALSE.
        except:
            return False
    #
    # ->    This is the _buildStack function for the Class/Object-Type: Utility ()
    #       Where: 
    #               xGuard              -   Is the XML Guard Statement.
    #               jsonPredictionData  -   Is the JSON prediction particle.
    #               jsonEventData       -   Is the JSON event particle.
    #               stack               -   This is the execution stack.
    #
    def _buildStack(self, xGuard, jsonPredictionData, jsonEventData):
        # -> Lopp through the XML operators in xGuard.
        for xOP in xGuard:
            # -> place the op code on the stack.
            if (xGuard[xOP] == 'AND'): self._stack.append('AND')
            if (xGuard[xOP] == 'OR'): self._stack.append('OR')
            if (xGuard[xOP] == 'ID'): self._stack.append('ID')
            # -> Check for a <guard> tag and execute operators.   
            if (xOP == 'guard'):
                if (isinstance(xGuard[xOP],list)): 
                    for xGuard in xGuard[xOP]:
                        # -> Make recursice call for self._buildStack for xGuard from list
                        self._buildStack(xGuard, jsonPredictionData, jsonEventData)
                else:
                    # -> Make recursice call for self._buildStack for xGuard[xOP]
                    self._buildStack(xGuard[xOP], jsonPredictionData, jsonEventData)
            # -> Check for a <match> tag and execute operators.
            if (xOP == 'match'):
                if (isinstance(xGuard[xOP],list)): 
                    for xOP in xGuard[xOP]:
                        # -> Make call to place _evalMatch(..) from list on stack
                        self._stack.append(self._evalMatch(xOP, jsonPredictionData, jsonEventData))
                else:
                    # -> Make call to place _evalMatch(..) on stack
                    self._stack.append(self._evalMatch(xGuard[xOP], jsonPredictionData, jsonEventData))
        # -> return the stack.
        return self._stack
    #
    #
    # ->    This is the _evalStack function for the Class/Object-Type: Utility ()
    #       Where:  
    #               xStack              -   Is the execuatble Stack.
    #
    def _evalStack(self, xStack):
        #
        if xStack == True: return True
        if xStack == False: return False
        #
        while len(xStack) != 0:
            xItem = xStack.pop(0)
            if xItem == True: return True
            if xItem == False: return False
            if xItem == 'ID': 
                return self._evalStack(xStack.pop(0))
            if xItem == 'AND':
                result = True
                yItem = xStack.pop(0)
                while (yItem != 'ID' and yItem !='AND' and yItem !='OR' and len(xStack) != 0):
                    result = yItem and result
                    yItem = xStack.pop(0)
                xStack.insert(0,yItem)
                return result and self._evalStack(xStack)
            if xItem == 'OR':
                result = False
                yItem = xStack.pop(0)
                while (yItem != 'ID' and yItem !='AND' and yItem !='OR'and len(xStack) != 0):
                    result = yItem or result
                    yItem = xStack.pop(0)
                xStack.insert(0,yItem)
                return result or self._evalStack(xStack)
        return False
    #
    #
    #
    # ->    This is the _guard function for the Class/Object-Type: Utility ()
    #       Where:  
    #               xGuard              -   Is the execuatble XML Guard Statement.
    #               jsonPredictionData  -   Is the JSON prediction particle.
    #               jsonEventData       -   Is the JSON event particle.
    #
    def _guard(self, xGuard, jsonPredictionData, jsonEventData):
        # -> Call the _buildStack to build the executable stack structure.
        xStack = self._buildStack(xGuard, jsonPredictionData, jsonEventData)
        # -> Return the evaluation of the XML Stack structure
        result = self._evalStack(xStack)
        return result
    #
    #
    #
    # ->    This is the action function for the Class/Object-Type: Utility ()
    #       Where: 
    #               xAction             -   Is the XML Action Statement.
    #               jsonEventData       -   Is the JSON event particle.
    #
    def  _action(self, xAction,  jsonEventData):
        if (xAction['@op'] == 'RET'):
            xValue = xAction['#text']
            x1 = xValue.split(':-')
            if (x1[0] =='event'): return float(self._getOpDataEvent(x1[1], jsonEventData)[0])
            else: return float(x1[0])
        else:
            return 0
    #
    #
    #
    # ->    This is the utility function for the Class/Object-Type: Utility ()
    #       Where: 
    #               eT   -   Is the Event Partcile Type.
    #               eID  -   Is the Event Partcile  Identifier.
    #               pT   -   Is the Prediction Partcile Type.
    #               pID  -   Is the Prediction Partcile Identifier.
    #
    def utility(self, Ep, eT, eID):
        (pT, pID) = Ep
        params = "{\"particleType\" : \"" + pT + "\", \"particleID\" : \"" + pID + "\"}"
        pjList = self.jsonRPC(str(params), 'getParticle')
        jsonPredictionData = json.loads(pjList['result'])
        params = "{\"particleType\" : \"" + eT + "\", \"particleID\" : \"" + eID + "\"}"
        pjList = self.jsonRPC(str(params), 'getParticle')
        jsonEventData = json.loads(pjList['result'])
        #
        # -> If the length of the parsed XML document is Zero then an error has occurewd.
        if (len(self._xdoc) == 0):
            print('ERROR: Failed to process XML File - Error in XML File detected..[FAIL]')
            sys.exit(0)
        #
        # -> Loop through the self._xdoc['utf']['clause'] elements on the XML Document
        for xClause in self._xdoc['utf']['clause']:
            #
            # -> Zero/Empty the executable Stack 
            self._stack = []
            #
            # -> This is the test to check that the <clause> tag is for the defined 
            #       prediction and event partciles.
            if (xClause['@src'] == jsonEventData['_name'] and 
                xClause['@dst'] == jsonPredictionData['_ident'].split('-')[0]):
                #
                # -> Test for a <guard> tag in the XML loop structure
                if self._guard(xClause['guard'], jsonPredictionData, jsonEventData): 
                    #
                    # -> If the Guard is True then execute/return the action.
                    self._utility = self._action(xClause['action'], jsonEventData)
        #
        # -> return the value of the utility function self._utility
        return self._utility
#
# -> This is the End of the Utility() Object: Last Edited - Date:   19th April 2019
#