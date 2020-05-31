#
# This the Artifical Life Engine Definition
#           Date:   1st June 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
import xmltodict
import os.path
import requests 
import json
import ast
import os
#
from utility import Utility
#
#
#
class ArtificalLifeEngine():
    #
    # ->    This is the __XMLLoad__ function for the Class/Object-Type: ArtificalLifeEngine()
    #
    def __XMLLoad__(self):
        with open(self._directoryName + '/functions.xml') as fd:
            xdoc = xmltodict.parse(fd.read())
            for _ , ltag in xdoc.items():
                for _ , mtag in ltag.items():
                    for xtag in mtag:
                        self.__filter__[xtag['@particle']].append([xtag['@type'],xtag['#text']])
        return True
    #
    # ->    This is the constructor(__init__) function for the Class/Object-Type: ArtificalLifeEngine()
    #
    def __init__(self, directoryName):
        self._server                        = '127.0.0.1'
        self._port                          = 4000
        self._rpc                           = 'jsonrpc'
        self._url                          = 'http://' + self._server + ':' + str(self._port) + '/' + self._rpc
        self._headers                       = {'content-type': 'application/json'}
        self._jsonrpcid                     = 1
        #
        self._directoryName                 = directoryName
        self._DEBUG                         = False
        #
        self.__filter__                     = {}
        self.__filter__['event']            = []
        self.__filter__['syslog']           = []
        self.__filter__['snort']            = []
        self.__filter__['sshd']             = []
        self.__filter__['tcpd']             = []
        self.__filter__['cef']              = []
        self.__filter__['vsftpd']           = []
        self.__filter__['dns']              = []
        self.__filter__['nsca']             = []
        self.__filter__['evt']              = [] 
        self.__filter__['netflow']          = [] 
        self.__filter__['ftpd']             = []
        self.__filter__['ip']               = []
        self.__filter__['tcp']              = []
        self.__filter__['udp']              = []
        self.__filter__['icmp']             = []
        self.__filter__['tcp-http-request'] = []
        self.__filter__['prediction']       = []
        #
        if (os.path.exists(self._directoryName + '/functions.xml')): self.__XMLLoad__()
    #
    # ->    This is the jsonRPC function for the Class/Object-Type: ArtificalLifeEngine()
    #
    def jsonRPC(self, jsonparams, rpcName):
        #
        #
        # -> Marshall the JSON RPC Components
        payload = {
            "method": rpcName,
            "params": [jsonparams],
            "jsonrpc": "2.0",
            "id": self._jsonrpcid, }
        #
        #
        # -> Make/execute the JSON RPC
        if (self._DEBUG ): print(payload)
        response = requests.post(self._url, data=json.dumps(payload), headers=self._headers).json()
        #
        #
        # 
        return response
    #
    # ->    This is the filter function for the Class/Object-Type: ArtificalLifeEngine()
    #
    def filter(self, eT, eID, predList):
        rList = []
        eList = self.__filter__[eT]
        if (len(eList) != 0 ):
            for eL in eList:
                for (x,y,z, pID) in predList.keys():
                    params = "{\"particleType\" : \"prediction\", \"particleID\" : \"" + pID + "\"}"
                    pList = self.jsonRPC(str(params), 'GetPredictionParticlParameters')['result']
                    for r in pList:
                        if (eL[0] == r['source_name'] and  eL[1] == r['external_id']):
                            rList.append(('prediction', pID))
        return rList
    #
    # ->    This is the run function for the Class/Object-Type: ArtificalLifeEngine().
    #       -> This function executes the swarm intelligence algorithm.
    #
    def run(self):
        print('.')
        print('Artifical Life Engine Starting Up.................................[OK]')
        uT = Utility()
        uT.__setDirName__(self._directoryName)
        uT.__LoadDataParticleList__()
        #
        # -> Loop until True = False
        #
        while(True):
            #
            #
            # -> This is the set of all Event Type Particles
            allEventParticles = self.jsonRPC('{}', 'vectorSpaceGetAllEventParticle')
            if (self._DEBUG ): print('******* :-> allEventParticles :', allEventParticles['result'])
            #
            #
            # -> This is the set of all STIX/Prediction Type Particles
            allSTIXParticles = self.jsonRPC('{}', 'vectorSpaceGetAllSTIXParticle')
            if (self._DEBUG ): print('******* :-> allSTIXParticles:',allSTIXParticles['result'])
            #
            #
            # -> For all Prediction Particles Update their Position in the GlobalVectorSpaceMatrix
            preddictlist = ast.literal_eval(allSTIXParticles['result'])
            for (x,y,z, t) in preddictlist.keys():
                for (pT, pID) in preddictlist[(x,y,z,t)]:
                    if (self._DEBUG ): 
                        print('------------------------------------------------------------------------------------------------------------------')
                        print('Particle Type <--> Partcile Identifier', pT ,' <--> ', pID)
                        print(' :---> X , Y , Z :', x , ' , ', y ,' , ', z)
                    params = "{\"particleType\" : \"" + pT + "\", \"particleID\" : \"" + pID + "\"}"
                    _ = self.jsonRPC(str(params), 'updatePredictionPartcile') 
            #
            #
            # -> For all Event Particles Update
            dictlist = ast.literal_eval(allEventParticles['result'])
            for (x,y,z) in dictlist.keys():
                for (pT, pID) in dictlist[(x,y,z)]:
                    #
                    #
                    # -> For An Event Particles Filter the prediction partciles 
                    filterset = self.filter(pT, pID, preddictlist)
                    Ue = []
                    Me = []
                    if (self._DEBUG):
                        print('\n######################################################################################')
                        print('Event Particle Type     : ',pT)
                        print('Event Particle ID       : ',pID)
                        print('Filter Set for Particle : ', filterset)
                        print('->######################################################################################')
                    #
                    #
                    # -> For All Filtered Prediction Particles Calculate the Utility Function.
                    for Ep in filterset:
                        # -> Calculate the Utility Function via the Utility object
                        #    -> uT is Utility object used to calculate the utility function
                        #    -> Ep is the prediction particle
                        #    -> (pT,pID) is the event partcile
                        uT.reset() 
                        Ue.append((uT.utility(Ep, pT, pID), Ep, pT, pID))
                        if (self._DEBUG ):
                            print('######################################################################################')
                            print('The Max Matrix/Vector Ue is : ',Ue)
                            print('->######################################################################################')
                    #
                    #
                    # -> Calculate the Maximum Utiliy from the Matrix/List Ue.
                    #    -> Ut is Utility value for the two particles
                    #    -> pT is the Prediction  Partcile Type
                    #    -> pID is the Unique ID of the Particle Partcile
                    #    -> eT is the Event Particle Type
                    #    -> pID is the Unique ID of the Event Partcile
                    MaxUT = 0
                    for (Ut, (pT, pID), eT, eID) in Ue:
                        if (Ut > MaxUT):
                            MaxUT = Ut
                            Me = [(Ut, (pT, pID), (eT, eID))]
                        elif (Ut == MaxUT):
                            Me.append((Ut, (pT, pID), (eT, eID)))
                    if (self._DEBUG ):
                        print('######################################################################################')
                        print('The Max Utility Me is : ',Me)
                        print('->######################################################################################')
                    #
                    #
                    # -> Update the Vector Space for every Event Partcile in the list Me.
                    #    -> Ut is Utility value for the two particles
                    #    -> pT is the Prediction  Partcile Type
                    #    -> pID is the Unique ID of the Particle Partcile
                    #    -> eT is the Event Particle Type
                    #    -> pID is the Unique ID of the Event Partcile
                    for (Ut, (pT, pID), (eT, eID)) in Me:
                        params = "{\"utility\" : \"" + str(Ut)
                        params = params + "\", \"predictionID\" : \"" + pID 
                        params = params + "\", \"particleType\" : \"" + eT 
                        params = params + "\", \"particleID\" : \"" + eID 
                        params = params + "\"}"
                        if (self._DEBUG ):
                            print('######################################################################################')
                            print('Invoking the vectorMatrixUpdateEventParticle RPC function with  : ',params)
                            print('->######################################################################################')
                        _ = self.jsonRPC(str(params), 'vectorMatrixUpdateEventParticle')
                    #
                    #
                    # -> Update the Vector Space for the decay function for the event particle.
                    #    -> eT is the Event Particle Type
                    #    -> pID is the Unique ID of the Event Partcile
                    params = "{\"particleType\" : \"" + pT + "\", \"particleID\" : \"" + pID + "\"}"
                    if (self._DEBUG ):
                        print('######################################################################################')
                        print('Invoking the vectorSpaceDecayParticle RPC function with  : ',params)
                        print('->######################################################################################')
                    _ = self.jsonRPC(str(params), 'vectorSpaceDecayParticle')
        #
        #
        #
        return True
#
#
#

