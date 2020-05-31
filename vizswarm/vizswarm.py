#
#
#
#
#
#
#
#
#
#
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
#
import requests
import json
import sys 
import ast
#
#
#
class RPCEngine():
    def __init__(self):
        self._server    = '127.0.0.1'
        self._port      = 4000
        self._rpc       = 'jsonrpc'
        self._url       = 'http://' + self._server + ':' + str(self._port) + '/' + self._rpc
        self._headers   = {'content-type': 'application/json'}
        self._DEBUG     = False
        
    #
    #
    #
    def RPC(self, rpcName, jsonparams, jsonrpcid):
        #
        payload = {
                "method": rpcName,
                "params": [jsonparams], 
                "jsonrpc": "2.0",
                "id": jsonrpcid, }
        #
        if (self._DEBUG ): print(payload)
        #
        return requests.post(self._url, data=json.dumps(payload), headers=self._headers).json()
    #
    # 
    # 
    def createPredictionDict(self):
        predictionDict = {}
        pjList = self.RPC('getAllSTIXParticles', '{}', 0)
        dictlist01 = ast.literal_eval(pjList['result'])
        for xlistItem in dictlist01:
            jdata = json.loads(xlistItem)
            predictionDict[jdata['_ident']] = jdata['_name']
        return predictionDict
#
#
#
#
#
#
class myGraph():
    def __init__(self):
        self.rpc    = RPCEngine()
        self.Title      = 'Swarm Cyber Partcile Collider - SCPC'
        self.posX       = []
        self.posY       = []
        self.fig        = ''
        self.axes       = ''
        self.rpc        = RPCEngine()
        self.predID     = []
        self.eventX     = []
        self.eventY     = []
        self.lineX      = []
        self.lineY      = []
        self.eventName  = {}
        self.eventID    = []
        self.itemKey    = {'snort': 'yo', 'cef' : 'go', 'evtx' : 'yo', 'ncsa' : 'co', 'tcpd' : 'blue', 'syslog' : 'blue', 'sshd' : 'bo'}
        self.lineKey    = {'snort': 'yellow', 'cef' : 'green', 'evtx' : 'yo', 'ncsa' : 'co', 'tcpd' : 'blue', 'syslog' : 'blue', 'sshd' : 'blue'}
    #
    #
    #
    def getData(self):    
        #
        request = self.rpc.RPC('vectorSpaceGetAllSTIXParticle', '{}', 1)['result']
        dictlist = ast.literal_eval(request)
        self.posX = []
        self.posY = []
        self.predID = []
        self.eventX = []
        self.eventY = []
        self.eventType = []
        self.lineX = []
        self.lineY = []
        self.eventName = {}
        self.eventID = []
        for (x, y, _, id) in dictlist:  
            self.posX.append([x])
            self.posY.append([y])
            self.predID.append(id)
        #
        self.width = []
        for _ in range(len(self.posX)): self.width.append(5)
        #
        request = self.rpc.RPC('vectorSpaceGetAllEventParticle', '{}', 2)['result']
        dictlist = ast.literal_eval(request)
        for (x, y, z) in dictlist: 
            if (x != 0 and y != 0 and x != 0):
                # -> get the event partcile that we looking at
                for (pT, pID) in dictlist[(x, y, z)]:
                    jParameters = '{ \"particleType\" : \"' + pT + '\", \"particleID\" : \"' + pID + '\" }'
                    request = self.rpc.RPC('getParticle', jParameters, 3)['result']
                    dictlist01 = ast.literal_eval(request)
                    self.eventID.append(dictlist01['_ident'])
                    self.eventName[dictlist01['_ident']] = dictlist01['_name']
                    # -> get the prediction partcile associated with the event particle
                    jParameters = '{ \"particleType\" : "prediction", \"particleID\" : \"' + dictlist01['_predictionID'] + '\" }'
                    (pX, pY, _, pID) = self.rpc.RPC('vectorSpaceGetParticlePosition', jParameters, 4)['result']
                    # -> update the object location particle lists
                    self.eventX.append([x])
                    self.eventY.append([y])
                    self.lineX.append([pX])
                    self.lineY.append([pY])
                    index = self.predID.index(pID)
                    self.width[index] = self.width[index] + 2

        #
        return True
    #
    #  
    # 
    def animate(self,i):
        self.getData() 
        self.fig.clear()
        self.axes = self.fig.add_axes([0.085,0.085,0.85,0.85])
        #
        plt.title('Swarm Cyber Partcile Collider\n')
        plt.xlabel('X - Distance')
        plt.ylabel('Y - Distance')
        plt.xlim(-1500,1500)
        plt.ylim(-1500,1500)
        #
        for index in range(len(self.lineX)):
            xList = [self.eventX[index]]
            yList = [self.eventY[index]]
            eName = self.eventName[self.eventID[index]]
            xList.append(self.lineX[index])
            yList.append(self.lineY[index])
            self.axes.plot( xList, yList, color=self.lineKey[eName], linewidth=1)
        #
        for ind in range(len(self.posX)):
            posX = [self.posX[ind]]
            posY = [self.posY[ind]]
            self.axes.text(posX[0][0] + 15, posY[0][0] + 15, self._predName[self.predID[ind]])
            self.axes.plot( posX, posY, 'ro', markersize= 2 * self.width[ind])
        for ind in range(len(self.eventX)):
            posX  = [self.eventX[ind]]
            posY  = [self.eventY[ind]]
            eName = self.eventName[self.eventID[ind]]
            self.axes.text(posX[0][0] + 15, posY[0][0] + 15, eName)
            self.axes.plot( posX[0][0], posY[0][0], self.itemKey[eName], markersize=5)

       
    # 
    # 
    #
    def run(self):
        self.getData()   
        self.fig = plt.figure(figsize=(12,12))
        self.axes = self.fig.add_axes([0.085,0.085,0.85,0.85])
        self.axes.plot( self.posX, self.posY, 'ro')
        plt.title('Swarm Cyber Particle Collider.\n')
        plt.xlabel('X - Distance')
        plt.ylabel('Y - Distance')
        plt.xlim(-1500,1500)
        plt.ylim(-1500,1500)
        _ = animation.FuncAnimation(self.fig, self.animate, interval = 100)
        plt.show()
        return True
    #
    # 
    #  
    def getPredIndex(self):
        self._predName = {}
        request = self.rpc.RPC('getAllSTIXParticles', '{}', 0)['result']
        dictlist = ast.literal_eval(request)
        for item in dictlist:
            jData  = json.loads(item)
            self._predName[jData['_ident']] = jData['_name']
        return True
#
# 
# 
if __name__ == '__main__':
    style.use('dark_background')
    graph = myGraph()
    graph.getPredIndex()
    graph.run()
#
#
#