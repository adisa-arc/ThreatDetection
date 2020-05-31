#
# This the Simulation Engine Definition
#           Date:   1st June 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
import xmltodict
import os.path
import sys
import time
import random
import subprocess
#
#
#
class Simulation():
    #
    # ->    This is the constructor(__init__) function for the Class/Object-Type: Simulation()
    #
    def __init__(self):
        self._simulationList    = []
        self._timsatampList     = []
        self._fileName          = ''
        self._XMLFile           = ''
        self._MAXSimEvents      = 999999999
        self._startTime         = 0
    # 
    # 
    # 
    def __monthToNumber__(self, Month):
        if (Month == 'Jan'): return 1
        if (Month == 'Feb'): return 2
        if (Month == 'Mar'): return 3
        if (Month == 'Apr'): return 4
        if (Month == 'May'): return 5
        if (Month == 'Jun'): return 6
        if (Month == 'Jul'): return 7
        if (Month == 'Aug'): return 8
        if (Month == 'Sep'): return 9
        if (Month == 'Oct'): return 10
        if (Month == 'Nov'): return 11
        if (Month == 'Dec'): return 12
        return 0
    # 
    # 
    # 
    def __processEvent__(self, eEvent, tCount, eType, eIngestor):
        event = ''
        myTime = self._startTime
        event = str(time.asctime(time.gmtime(myTime))[4:-4])
        #
        if (eType == 'snort'):
            if (int(eEvent['observer']['@pid']) != 0):
                event = event + eEvent['observer']['#text'] + ' ' +eEvent['observer']['@process'] + '[' + eEvent['observer']['@pid'] + ']: '
            else:
                event = event + eEvent['observer']['#text'] + ' ' +eEvent['observer']['@process'] + ': '
            event = event + eEvent['data']
            print('                   |-SNORT---->', event)
        #
        if (eType == 'syslog'):
            if (int(eEvent['observer']['@pid']) != 0):
                event = event + eEvent['observer']['#text'] + ' ' +eEvent['observer']['@process'] + '[' + eEvent['observer']['@pid'] + ']: '
            else:
                event = event + eEvent['observer']['#text'] + ' ' +eEvent['observer']['@process'] + ': '
            event = event + eEvent['data']
            print('                   |-SYSLOG--->', event)
        #
        if (eType == 'tcpd'):
            event = event + eEvent['observer']['#text'] + ' ' +eEvent['observer']['@process'] + ': '
            event = event + eEvent['data']
            print('                   |-TCPD----->', event)
        #
        if (eType == 'sshd'):
            event = event + eEvent['observer']['#text'] + ' ' +eEvent['observer']['@process'] + ': '
            event = event + eEvent['data']
            print('                   |-SSHD----->', event)
        #
        if (eType == 'cef'):
            event = event + eEvent['observer']['#text'] + ' ' +eEvent['data']
            print('                   |-CEF------>', event)
        # 
        if (eType == 'vsftpd'):
            event = event + eEvent['observer']['#text'] + ' ' + eEvent['observer']['@process'] + ': '
            event = event + eEvent['data']
            print('                   |-VSFTPD--->', event)
        # 
        if (eType == 'dns'):
            x = time.asctime(time.gmtime(myTime)).split(' ')
            event = x[2] + '-' + x[1] + '-' + x[4] + ' ' + x[3] + ' '
            event = event + eEvent['data']
            print('                   |-DNS------>', event)
        # 
        if (eType == 'ncsa'):
            xTime = time.asctime(time.gmtime()).split(' ')
            event = eEvent['observer']['#text'] + ' - ' + eEvent['observer']['@pid'] + ' [' + xTime[2] + '/' + xTime[1] + '/' + xTime[4] 
            event = event + ':' + xTime[3] + ' ' + eEvent['observer']['@process'] + '] ' + eEvent['data'] 
            print('                   |-NSCA----->', event)
        # 
        if (eType == 'ftpd'):
            xTime = time.asctime(time.gmtime()).split(' ')
            event = xTime[0] + ' ' + xTime[1] + ' ' + xTime[2] + ' ' + xTime[3] + ' ' + xTime[4]
            event = event + ' ' + eEvent['observer']['@process'] + ' ' + eEvent['observer']['#text'] + ' ' + eEvent['observer']['@pid']
            event = event + ' ' + eEvent['data']  
            print('                   |-FTPD----->', event)
        # 
        if (eType == 'netflow'):
            xTime = time.asctime(time.gmtime()).split(' ')
            event = '<?xml version="1.0" encoding="UTF-8"?><event><netflow datetime="' + xTime[1] + ' ' + xTime[2] + ' ' + xTime[3]
            event = event + '" ident=\"' + (str(int(random.random()*100000000000000000)) + '0000000000000000')[:17] + '" type="netflow">'
            event = event + '<datetime>' + xTime[1] + ' ' + xTime[2] + ' ' + xTime[3] + '</datetime>'
            event = event + '<duration>' + eEvent['data']['netflow']['duration'] + '</duration>'
            event = event + '<protocol>' + eEvent['data']['netflow']['protocol'] + '</protocol>'
            event = event + '<sourceip>' + eEvent['data']['netflow']['sourceip'] + '</sourceip>'
            event = event + '<sourceport>' + eEvent['data']['netflow']['sourceport'] + '</sourceport>'
            event = event + '<destinationip>' + eEvent['data']['netflow']['destinationip'] + '</destinationip>'
            event = event + '<destinationport>' + eEvent['data']['netflow']['destinationport'] + '</destinationport>'
            event = event + '<packets>' + eEvent['data']['netflow']['packets'] + '</packets>'
            event = event + '<bytes>' + eEvent['data']['netflow']['bytes'] + '</bytes>'
            event = event + '</netflow></event>'
            # 
            output = '<netflow datetime="' + xTime[1] + ' ' + xTime[2] + ' ' + xTime[3]
            output = output + '" ident=\"' + (str(int(random.random()*100000000000000000)) + '0000000000000000')[:17] + '" type="netflow"> . . .'
            print('                   |-NETFLOW--->', output)
        # 
        if (eType == 'evtx'):
            xTime = time.asctime(time.gmtime()).split(' ')
            event = '<?xml version="1.0" encoding="UTF-8"?><event><evt datetime="' + xTime[1] + ' ' + xTime[2] + ' ' + xTime[3]
            event = event + '" ident=\"' + (str(int(random.random()*100000000000000000)) + '0000000000000000')[:17] + '" type="evt">'
            event = event + '<datetime>' + xTime[4] + '-' + str(self.__monthToNumber__(xTime[1])) + '-' + xTime[2] + 'T' + xTime[3] + '</datetime>'
            event = event + '<source>' + eEvent['data']['evt']['source'] + '</source>'
            event = event + '<eventid>' + eEvent['data']['evt']['eventid'] + '</eventid>'
            event = event + '<user>' + eEvent['data']['evt']['user'] + '</user>'
            event = event + '<computer>' + eEvent['data']['evt']['computer'] + '</computer>'
            event = event + '<processid>' + eEvent['data']['evt']['processid'] + '</processid>'
            event = event + '<threadid>' + eEvent['data']['evt']['threadid'] + '</threadid>'
            event = event + '<keywords>' + eEvent['data']['evt']['keywords'] + '</keywords>'
            event = event + '</evt></event>'
            #
            output = '<evt datetime="' + xTime[1] + ' ' + xTime[2] + ' ' + xTime[3]
            output = output + '" ident=\"' + (str(int(random.random()*100000000000000000)) + '0000000000000000')[:17] + '" type="evt"> . . .'
            print('                   |-EVTX----->', output)
        # 
        #
        #
        if (eType == 'netflow' or eType == 'evtx'):
            filename   = 'simulation/' + (str(int(random.random()*100000000000000000)) + '0000000000000000')[:17] + ".xml"
            fileObject = open(filename,"w+")
            fileObject.write(event)
            fileObject.close()
            ingestor = '../' + eIngestor + '/' + eIngestor + '.py'
            subprocess.run(['/usr/bin/python',ingestor, filename ])
        else: 
            filename   = 'simulation/' + (str(int(random.random()*100000000000000000)) + '0000000000000000')[:17] + ".dat"
            fileObject = open(filename,"w+")
            fileObject.write(event)
            fileObject.close()
            ingestor = '../' + eIngestor + '/' + eIngestor + '.py'
            subprocess.run(['/usr/bin/python',ingestor,'-n', '1', filename ])
        #
        return True
    #
    #  
    # 
    def __execute__(self):
        print('Simulation [simulation] - Version 1.0 - andrew.blyth@adisa.global\n')
        self._simulationList = []
        self._XMLFile = open(self._fileName,'r')
        self._startTime = time.time()
        print('\nLoadling Simulation.........................................................[OK]')
        self._simulationList = xmltodict.parse(self._XMLFile.read())
        print('Success Loadling XML Simulation Definition File.............................[OK]')
        print('Simulation Information/Details:')
        print('   |')
        print('   |--->Version Number        :', self._simulationList['simulation']['@version'])
        if (self._simulationList['simulation']['@time'] == '0'):
            print('   |--->Simulation Start Time :', self._simulationList['simulation']['@time'], ' == ', time.asctime(time.gmtime(self._startTime)), ' == ', self._startTime)
        else:
            self._startTime = int(self._simulationList['simulation']['@time'])
            print('   |--->Simulation Start Time :', self._simulationList['simulation']['@time'], ' == ', time.asctime(time.gmtime(self._startTime)), ' == ', self._startTime)
        #
        print('           |')
        simList = self._simulationList['simulation']['timestamp']
        if type(simList) != list: simList = [simList]
        #
        for tStamp in simList:
            self._startTime = self._startTime + int(tStamp['@tcount'])
            print('           |--->Event(s) Times Stamp Time Units / Time Stamp: ', tStamp['@unit'], ' / ', self._startTime)
            #time.sleep(int(tStamp['@tcount'])/100)
            print('                   |')
            if ( str(type(tStamp['event'])) == '<class \'collections.OrderedDict\'>'):
                self.__processEvent__(tStamp['event'], tStamp['@tcount'], tStamp['event']['@type'], tStamp['event']['@ingestor'])
            else:
                for event in tStamp['event']: 
                    self.__processEvent__(event, tStamp['@tcount'], event['@type'], event['@ingestor'])
        #
        return True
    #
    #
    #
    #
    def help(self):
        print('SIMULATOR [simulation] - Version 1.0 - andrew.blyth@adisa.global\n')
        print('USAGE: simulation /path/filename\n') 
        print('Examples of Usage:\n')
        print('       simulation sim01.xml           - This will read and process all enties.\n')
        print('       simulation sim01.xml sim02.xml - This will read and process all enties.\n')
    #
    #
    #
    def run(self):
        if (len(sys.argv) == 2):
            exists = os.path.isfile(sys.argv[1])
            self._fileName = sys.argv[1]
        else:
            print('Simulation [simulation] - Version 1.0 - andrew.blyth@adisa.global\n')
            print(":- ERROR: Insufficent command line arguments.\n\n")
            self.help()
            sys.exit()
        #   
        if not exists:
            print('Simulation [simulation] - Version 1.0 - andrew.blyth@adisa.global\n')
            print(":- ERROR: Filename '" + self._fileName + "' not found or unaccessable.\n")
            sys.exit()
            return True
        #
        #
        #
        return self.__execute__()
        #
        #
        #
#
#
#
if __name__ == "__main__":
    sim = Simulation()
    sim.run()
    print('   |')
    print('   |--->Simulation Complete: [OK]\n')
    sys.exit(0)
#
#
#