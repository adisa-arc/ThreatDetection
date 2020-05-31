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
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import random
import sys
import requests
import json
import ast
import time
import numpy as np
#
#
#
class RPCEngine():
    def __init__(self):
        self._server                        = '127.0.0.1'
        self._port                          = 4000
        self._rpc                           = 'jsonrpc'
        self._url                           = 'http://' + self._server + ':' + str(self._port) + '/' + self._rpc
        self._headers                       = {'content-type': 'application/json'}
        self._DEBUG                         = True
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
class DataGraph():
    def __init__(self):
        self.data = []
        self.data1 = []
        self.dataPlot = 0
        self.rpc = 'None'
        self.title = 'None'
        self.interval = 1
        self.rpcval = 1
        self.ViewBox = 0
    #
    # 
    # 
    def ConvertDate(self, month):
        if (month == 'Jan'): return 1
        if (month == 'Feb'): return 2
        if (month == 'Mar'): return 3
        if (month == 'Apr'): return 4
        if (month == 'May'): return 5
        if (month == 'Jun'): return 6
        if (month == 'Jul'): return 7
        if (month == 'Aug'): return 8
        if (month == 'Sep'): return 9
        if (month == 'Oct'): return 10
        if (month == 'Nov'): return 11
        if (month == 'Dec'): return 12
        return 0
    # 
    # 
    # 
    def GraphLogData(self, rpcNAme):
        #
        rpc1 = RPCEngine()
        data1 = rpc1.RPC(rpcNAme, '{}', self.rpcval )
        astJSON1 = ast.literal_eval(data1['result'])
        syslogTimeDict1 = {}
        for syslogItem1 in astJSON1:
            #
            syslogJData1 = json.loads(syslogItem1)
            #
            if (str(type(syslogJData1['_data'])) == '<class \'str\'>'):
                syslogIndex1 = syslogJData1['_datetime']
            else:
                syslogIndex1 = syslogJData1['_data']['_datetime']
            #
            if (syslogIndex1 in syslogTimeDict1):
                syslogTimeDict1[syslogIndex1].append(syslogItem1)
            else:
                syslogTimeDict1[syslogIndex1] = []
                syslogTimeDict1[syslogIndex1].append(syslogItem1)
        #
        self.rpcval = self.rpcval + 1
        if (self.rpcval  > 32769): self.rpcval = 1
        #
        t1 = []
        for intval in range(self.interval): t1.append(intval)
        x1 = []
        x1.append(t1)    
        y1 = [] 
        z1 = []
        #
        xtime1 = time.time()
        for syslogTime1 in t1:
            timeSyslog1 = time.asctime(time.gmtime(xtime1 - syslogTime1))
            if (timeSyslog1[4:-5] in syslogTimeDict1.keys()): 
                z1.append(len(syslogTimeDict1[timeSyslog1[4:-5]]))
            else: 
                if (rpcNAme == 'getAllEvtXParticles'):
                    evtData = timeSyslog1.split()
                    tsmp = evtData[4] + '-' + str(self.ConvertDate(evtData[1])) + '-' + evtData[2]
                    tsmp = tsmp + 'T' +evtData[3]
                    if (tsmp in syslogTimeDict1.keys()):
                        z1.append(len(syslogTimeDict1[tsmp]))
                    else:
                        z1.append(0)
                elif (rpcNAme == 'getAllNCSAParticles'):
                    NCSAData = timeSyslog1.split(' ')
                    tsmp = '[' +NCSAData[2] + '/' +  NCSAData[1] + '/' + NCSAData[4] + ':' +  NCSAData[3] + ' +0700]'
                    if (tsmp in syslogTimeDict1.keys()):
                        z1.append(len(syslogTimeDict1[tsmp]))
                    else:
                        z1.append(0)
                elif (rpcNAme == 'getAllDNSParticles'):
                    tStamp = timeSyslog1[4:].split(' ')
                    tsmp = tStamp[1] + '-' + tStamp[0] + '-' + tStamp[3] + ' ' + tStamp[2]
                    if (tsmp in syslogTimeDict1.keys()):
                        z1.append(len(syslogTimeDict1[tsmp]))
                    else:
                        z1.append(0)
                else:
                    z1.append(0)
        #
        y1.append(z1)
        #
        return (x1,y1)
    # 
    # 
    # 
    def GraphUpdate(self): 
        pen01 = pg.mkPen(width=3, color=(0, 0, 0))
        self.dataPlot.plot(self.data[0][0],self.data[1][0], pen=pen01, name='DNS')
        self.dataPlot1.plot(self.data1[0][0],self.data1[1][0], pen=pen01, name='FTPD')
        self.dataPlot2.plot(self.data2[0][0],self.data2[1][0], pen=pen01, name='NetFlow')
        self.dataPlot3.plot(self.data3[0][0],self.data3[1][0], pen=pen01, name='NCSA')
        self.dataPlot4.plot(self.data4[0][0],self.data4[1][0], pen=pen01, name='EVTX')
        self.data  = self.GraphLogData('getAllDNSParticles')
        self.data1 = self.GraphLogData('getAllFTPDParticles')
        self.data2 = self.GraphLogData('getAllNetFlowParticles')
        self.data3 = self.GraphLogData('getAllNCSAParticles')
        self.data4 = self.GraphLogData('getAllEvtXParticles')
        pen02 = pg.mkPen(width=1, color=(255, 0, 0))
        self.dataPlot.plot(self.data[0][0],self.data[1][0], pen=pen02, name='DNS')
        pen03 = pg.mkPen(width=1, color=(0, 255, 0))
        self.dataPlot1.plot(self.data1[0][0],self.data1[1][0], pen=pen03, name='FTPD')
        pen04 = pg.mkPen(width=1, color=(255, 0, 255))
        self.dataPlot2.plot(self.data2[0][0],self.data2[1][0], pen=pen04, name='NetFlow')
        pen05 = pg.mkPen(width=1, color=(255, 255, 0))
        self.dataPlot3.plot(self.data3[0][0],self.data3[1][0], pen=pen05, name='NCSA')
        pen06 = pg.mkPen(width=1, color=(0, 255, 255))
        self.dataPlot4.plot(self.data4[0][0],self.data4[1][0], pen=pen06, name='EVTX')
        #
    #
    # 
    # 
    def help(self):
        print('Swarm Particle Arrival Rate Vizualisation [viznlog] - Version 1.0 - andrew.blyth@adisa.global\n')
        print('USAGE: viznlog time-internal') 
        print('WHERE:')
        print('      time-internal     - Specifies the time interval that will be display:.\n')
        print('Examples of Usage:\n')
        print('       viznlog 30        - This will graph the last 30 seconds worth of non-syslog related partciles.\n')
        print('       viznlog 3600      - This will graph the last 1 hours worth of non-syslog related partciles.\n')
    # 
    # 
    # 
    def main(self):
        _ = QtGui.QApplication([])
        if (len(sys.argv) != 2): 
            self.help()
            sys.exit(0)
        self.interval = int(sys.argv[1])
        #
        self.title = " Swarm Cyber Particle Collider (SCPC)"
        win = pg.GraphicsWindow(title=self.title)
        win.resize(1000,1200)
        win.setWindowTitle(self.title)
        #
        pg.setConfigOptions(antialias=True)
        #
        self.dataPlot = win.addPlot(title="<font size=\"3\">DNS Arrival Rates - Last " + str(self.interval) + " Seconds</font>")
        self.data = self.GraphLogData('getAllDNSParticles')
        self.Graph = self.dataPlot.plot()
        self.dataPlot.setYRange(0, 10)
        self.dataPlot.showGrid(x=True, y=True)
        #
        win.nextRow()
        self.dataPlot1 = win.addPlot(title="<font size=\"3\">FTPD Arrival Rates - Last " + str(self.interval) + " Seconds</font>")
        self.data1 = self.GraphLogData('getAllFTPDParticles')
        self.Graph1 = self.dataPlot1.plot()
        self.dataPlot1.setYRange(0, 10)
        self.dataPlot1.showGrid(x=True, y=True)
        #
        win.nextRow()
        self.dataPlot2 = win.addPlot(title="<font size=\"3\">Netflow Arrival Rates - Last " + str(self.interval) + " Seconds</font>")
        self.data2 = self.GraphLogData('getAllNetFlowParticles')
        self.Graph2 = self.dataPlot2.plot()
        self.dataPlot2.setYRange(0, 10)
        self.dataPlot2.showGrid(x=True, y=True)
        #
        win.nextRow()
        self.dataPlot3 = win.addPlot(title="<font size=\"3\">NSCA Arrival Rates - Last " + str(self.interval) + " Seconds</font>")
        self.data3 = self.GraphLogData('getAllNCSAParticles')
        self.Graph3 = self.dataPlot3.plot()
        self.dataPlot3.setYRange(0, 10)
        self.dataPlot3.showGrid(x=True, y=True)
        #
        win.nextRow()
        self.dataPlot4 = win.addPlot(title="<font size=\"3\">EVTX Arrival Rates - Last " + str(self.interval) + " Seconds</font>")
        self.data4 = self.GraphLogData('getAllEvtXParticles')
        self.Graph4 = self.dataPlot4.plot()
        self.dataPlot4.setYRange(0, 10)
        self.dataPlot4.showGrid(x=True, y=True)
        #
        timer = QtCore.QTimer()
        timer.timeout.connect(self.GraphUpdate)
        timer.start(50)
        #
        #
        #
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()
# 
# -> This will invoke 
#
if __name__ == '__main__':
    graph = DataGraph()
    graph.main()
#
#
#
