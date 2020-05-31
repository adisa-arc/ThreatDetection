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
import sys
import requests
import json
from showparticle import showPartcile
#
#
#
def version():
    print('\n                Python Swarm Debugger - version 0.1\n')
#
#
#
def help():
    print('\nThe following is the list of command available at the Command Line\n')
    print(' -v           -   This displays the version information on the debugger.')
    print(' -h/?         -   This displays the help information on the debugger.')
    print(' -c command   -   This will executed a debugger command from the command line.\n')
    print('                  For example: $debugger.py -c \"lt snort\"')
    print('\nThe following is the list of command available to the Debugger:\n')
    print('    help/h/?  -   This is the help page for the swarm debugger.')
    print('    version/v -   This displays the version information on the debugger.')
    print('    exit/quit -   This exists / quits the debugger application.')
    print('    ls type / list type       -   The function that is list all partciles of')
    print('                                  a partcile type.')
    print('                  The list types are as follows:')
    print('                  -> event. For example: Debugger:> list events')
    print('                  -> syslog. For example: Debugger:> ls syslog')
    print('                  -> snort. For example: Debugger:> list snort')
    print('    sh type id / show type id  -   The function that shows a specific partcile')
    print('                                    of a specific type.')
    print('                  The list types are as follows:')
    print('                  -> event. For example: Debugger:> show event 0192819128')
    print('                  -> syslog. For example: Debugger:> st syslog 5364716253')
    print('                  -> snort. For example: Debugger:> show snort 7160271628\n')
#
#
#
def parseCommandLine():
    if (len(sys.argv) < 2):
        return (True, True)
    else:
        counter = 0
        for i in  sys.argv:
            counter = counter + 1
            if (i == '-v'):
                version()
                sys.exit()
            if (i == '-h' or i == '-?'):
                help()
                sys.exit()
            if (i == '-c'):
                return (False, sys.argv[counter])
#
#
#
def runDebugger():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}
    jsonrpcid = 1
    command = ""
    version()
    print("\nDebugge Information\n")
    print("  :> JSON RPC URL: ", url)
    print("  :> JSON Headers: ", headers)
    (value, command) = parseCommandLine()
    while True:
        if (value):
            command = input("\nDebugger:> ")
        commandlist = command.split(' ')
        if (commandlist[0] == 'version' or commandlist[0] == 'v'): version()
        elif (commandlist[0] == 'help'): help()
        elif (commandlist[0] == 'h'): help()
        elif (commandlist[0] == '?'): help()
        elif (commandlist[0] == 'exit'):
            print("\n")
            sys.exit()
        elif (commandlist[0] == 'quit'):
            print("\n")
            sys.exit()
        elif (commandlist[0] == 'q'):
            print("\n")
            sys.exit()
        elif (commandlist[0] == 'sh' or commandlist[0] == 'show'):
            _ = showPartcile(commandlist)
        elif (commandlist[0] == 'list' or commandlist[0] == 'ls'):
            if (len(commandlist) < 2):
                print('Error:> The ist command needs extra argument.')
            elif (len(commandlist) > 2):
                print('Error:> The ist command has to many arguments.')
            else:
                # 
                if (commandlist[1] == 'prediction'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list prediction"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result']) 
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [PREDICTION] -------------------------------------------------------')
                        print('No PREDICTION Particles in Swarm.')
                    else:
                        print('\n')
                        for i in x['data']:
                            print('---- Event Type := [PREDICTION] -------------------------------------------------------')
                            print(' ID Chain := [PREDICTION:',x['data'][i]['identifier'],']')
                            print('PREDICTION Type        :=', x['data'][i]['type'])
                            print('PREDICTION Identifier  :=', x['data'][i]['identifier'])
                            print('PREDICTION Date & Time :=', x['data'][i]['datetime'])
                            print('PREDICTION References  :=', x['data'][i]['references'])
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'stix'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list stix"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result']) 
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [STIX] -------------------------------------------------------')
                        print('No STIX Particles in Swarm.')
                    else:
                        print('\n')
                        for i in x['data']:
                            print('---- Event Type := [STIX] -------------------------------------------------------')
                            print(' ID Chain := [STIX:',x['data'][i]['identifier'],']')
                            print('STIX Type              :=', x['data'][i]['type'])
                            if (x['data'][i]['name'] != 'NONE'):
                                print('STIX Name              :=', x['data'][i]['name'])
                            if (x['data'][i]['identifier'] != 'NONE'):
                                print('STIX Identifier        :=', x['data'][i]['identifier'])
                            if (x['data'][i]['description'] != 'NONE'):
                                print('STIX Description       :=', x['data'][i]['description'])
                            if (x['data'][i]['cdatetime'] != 'NONE'):
                                print('STIX Creation Time     :=', x['data'][i]['cdatetime'])
                            if (x['data'][i]['mdatetime'] != 'NONE'):
                                print('STIX Modification Time :=', x['data'][i]['mdatetime'])
                            if (x['data'][i]['description'] != 'NONE'):
                                print('STIX Description       :=', x['data'][i]['description'])
                            if (x['data'][i]['pattern'] != 'NONE'):
                                print('STIX Pattern           :=', x['data'][i]['pattern'])
                            if (x['data'][i]['killchainphase'][2:6] != 'NONE'):
                                print('STIX Kill Chain Phase  :=', x['data'][i]['killchainphase'])
                            if (x['data'][i]['lables'][2:6] != 'NONE'):
                                print('STIX Labels            :=', x['data'][i]['lables'])
                            if (x['data'][i]['externalrefs'][2:6] != 'NONE'):
                                print('STIX External Refs     :=', x['data'][i]['externalrefs'])
                            if (x['data'][i]['relationship_type'] != 'NONE'):
                                print('STIX Relationship Type :=', x['data'][i]['relationship_type'])
                            if (x['data'][i]['source_ref'] != 'NONE'):
                                print('STIX Source Reference  :=', x['data'][i]['source_ref'])
                            if (x['data'][i]['target_ref'] != 'NONE'):
                                print('STIX Target Reference  :=', x['data'][i]['target_ref'])
                    #  
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'event'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list events"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result']) 
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT] -------------------------------------------------------')
                        print('No Event Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT] -------------------------------------------------------')
                            print(' ID Chain := [EVENT:',x['data'][i]['identifier'],']')
                            print('Event Identifier      :=', x['data'][i]['identifier'])
                            print('Event Date and Time   :=', x['data'][i]['datetime'])
                            print('Event Sub Type        :=', x['data'][i]['subtype'])
                            print('Event Sub Type Ident  :=', x['data'][i]['subtype_id'], '\n')
                    #
                    print('--------------------------------------------------------------------------------')
                if (commandlist[1] == 'syslog'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list syslog"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[SYSLOG] -------------------------------------------')
                        print('No SYSLOG Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[SYSLOG] -------------------------------------------')
                            print(' ID Chain := [EVENT:',x['data'][i]['super_id'],']->[SYSLOG:',x['data'][i]['identifier'],']')
                            print(' Identifier             :=', x['data'][i]['identifier'])
                            print(' Date and Time          :=', x['data'][i]['datetime'])
                            print(' Super Type[Identifier] :=', x['data'][i]['suptype'], '[', x['data'][i]['suptype_id'], ']')
                            print(' Sub Type[Identifier]   :=', x['data'][i]['subtype'], '[', x['data'][i]['subtype_id'], ']')
                            print(' System                 :=', x['data'][i]['system'])
                            print(' Process[Identifier]    :=', x['data'][i]['process_name'],'[', x['data'][i]['process_id'], ']')
                            print(' Message                :=', x['data'][i]['data'], '\n')
                    #
                    print('---------------------------------------------------------------------------------')
                if (commandlist[1] == 'snort'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list snort"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[SYSLOG]->[SNORT] -----------------------------------')
                        print('No SNORT Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[SYSLOG]->[SNORT] -----------------------------------')
                            print(' ID Chain := [SYSLOG:',x['data'][i]['super_id'],']->[SNORT:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' System              :=', x['data'][i]['system'])
                            print(' Version             :=', x['data'][i]['version'])
                            print(' Classification      :=', x['data'][i]['classification'])
                            print(' Priority            :=', x['data'][i]['priority'])
                            print(' |----> Protocol             :=', x['data'][i]['protocol'])
                            print(' |----> Snort Alert Message  :=', x['data'][i]['message'])
                            print(' |----> SRC IP Address       :=', x['data'][i]['src'])
                            print(' |----> SRC Port Address     :=', x['data'][i]['srcport'])
                            print(' |----> DST IP Address       :=', x['data'][i]['dst'])
                            print(' |----> DST Port Address     :=', x['data'][i]['dstport'])
                    #
                    print('--------------------------------------------------------------------------------')
                if (commandlist[1] == 'sshd'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list sshd"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    try:    
                        x = json.loads(result['result'])
                        if (x['data'] == 'NONE'):
                            print('---- Event Type := [EVENT]->[SYSLOG]->[SSHD] -----------------------------------')
                            print('No CEF Particles in Swarm.')
                        else:
                            for i in x['data']:
                                print('---- Event Type := [EVENT]->[SYSLOG]->[SSHD] -----------------------------------')
                                print(' ID Chain := [SYSLOG:',x['data'][i]['super_id'],']->[SSHD:',x['data'][i]['identifier'],']')
                                print(' Identifier          :=', x['data'][i]['identifier'])
                                print(' Date and Time       :=', x['data'][i]['datetime'])
                                print(' System              :=', x['data'][i]['system'])
                                print(' Process             :=', x['data'][i]['process'])
                                print(' Source IP Address   :=', x['data'][i]['sourceaddr'])
                                print(' Source Port         :=', x['data'][i]['sourceport'])
                                print(' Username            :=', x['data'][i]['username'])
                                print(' Raw Data            :=', x['data'][i]['data'])
                        #
                        print('--------------------------------------------------------------------------------')
                    except:
                        print('Error Processing JSON RPC.')
                if (commandlist[1] == 'vsftpd'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list vsftpd"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json() 
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[SYSLOG]->[VSFTPD] -----------------------------------')
                        print('No VSFTPD Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[SYSLOG]->[VSFTPD] -----------------------------------')
                            print(' ID Chain := [SYSLOG:',x['data'][i]['super_id'],']->[VSFTPD:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' Username            :=', x['data'][i]['username'])
                            print(' Command Type        :=', x['data'][i]['commandtype'])
                            print(' Source Address      :=', x['data'][i]['sourceaddr'])
                            print(' Raw Data            :=', x['data'][i]['data'])
                    #
                    print('--------------------------------------------------------------------------------')
                if (commandlist[1] == 'tcpd'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list tcpd"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json() 
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[SYSLOG]->[TCPD] -----------------------------------')
                        print('No TCPD Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[SYSLOG]->[TCPD] -----------------------------------')
                            print(' ID Chain := [SYSLOG:',x['data'][i]['super_id'],']->[TCPD:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' System              :=', x['data'][i]['system'])
                            print(' Process             :=', x['data'][i]['process'])
                            print(' Connection          :=', x['data'][i]['connection'])
                    #
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'cef'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list cef"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[SYSLOG]->[CEF] -----------------------------------')
                        print('No CEF Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[SYSLOG]->[CEF] -----------------------------------')
                            print(' ID Chain := [SYSLOG:',x['data'][i]['super_id'],']->[CEF:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' Version             :=', x['data'][i]['version'])
                            print(' Device Info         :=', x['data'][i]['deviceinfo'])
                            print(' Source IP Address   :=', x['data'][i]['sourceip'])
                            print(' CEF Signature       :=', x['data'][i]['signature'])
                            print(' Severity            :=', x['data'][i]['severity'])
                            print(' CEF Exenstions      :=', x['data'][i]['exenstions'])
                    #
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'nsca'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list nsca"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[NCSA] ------------------------------------------')
                        print('No NSCA Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[NSCA] -----------------------------------------')
                            print(' ID Chain := [EVENT:',x['data'][i]['super_id'],']->[NSCA:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' Client              :=', x['data'][i]['client'])
                            print(' User ID             :=', x['data'][i]['userid'])
                            print(' User                :=', x['data'][i]['user'])
                            print(' NSCA Request        :=', x['data'][i]['request'])
                            print(' Status Code         :=', x['data'][i]['statuscode'])
                            print(' The Size            :=', x['data'][i]['size'])
                    #
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'dns'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list dns"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[DNS] -------------------------------------------')
                        print('No DNS Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[DNS] ------------------------------------------')
                            print(' ID Chain := [EVENT:',x['data'][i]['super_id'],']->[DNS:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' Requester           :=', x['data'][i]['requester'])
                            print(' DNS Request         :=', x['data'][i]['request'])
                            print(' DNS Request Type    :=', x['data'][i]['requesttype'])
                    #
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'netflow'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list netflow"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[NETFLOW] ----------------------------------------')
                        print('No NetFlow Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[NETFLOW] ---------------------------------------')
                            print(' ID Chain := [EVENT:',x['data'][i]['super_id'],']->[NETFLOW:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' Duration of Flow    :=', x['data'][i]['duration'])
                            print(' Protocol            :=', x['data'][i]['protocol'])
                            print(' Source IP Addrress  :=', x['data'][i]['sourceip'])
                            print(' Source Port         :=', x['data'][i]['sourceport'])
                            print(' Dest IP Address     :=', x['data'][i]['destinationip'])
                            print(' Destination Port    :=', x['data'][i]['destport'])
                            print(' No of Packets       :=', x['data'][i]['packets'])
                            print(' No of Bytes in Flow :=', x['data'][i]['pbytes'])
                    #
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'ftpd'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list ftpd"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[FTPD] ----------------------------------------')
                        print('No FTPD Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[FTPD] ---------------------------------------')
                            print(' ID Chain := [EVENT:',x['data'][i]['super_id'],']->[FTPC:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' Transfer Time       :=', x['data'][i]['transfertime'])
                            print(' Remote Host         :=', x['data'][i]['remotehost'])
                            print(' Filesize            :=', x['data'][i]['filesize'])
                            print(' FTP Filename        :=', x['data'][i]['filename'])
                            print(' Transfer Type       :=', x['data'][i]['transfertype'])
                            print(' Action Flag         :=', x['data'][i]['actionflag'])
                            print(' FTP Direction       :=', x['data'][i]['direction'])
                            print(' Access Mode         :=', x['data'][i]['accessmode'])
                            print(' Username            :=', x['data'][i]['username'])
                            print(' Service Name        :=', x['data'][i]['servicename'])
                            print(' Auth Method         :=', x['data'][i]['authmethod'])
                            print(' Authuser ID         :=', x['data'][i]['authuserid'])
                            print(' FTP Status Code     :=', x['data'][i]['status'])
                    #
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'evt'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list evt"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[WINDOWS EVENT] ----------------------------------------')
                        print('No Windows Event Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[WINDOWS EVENT]---------------------------------------')
                            print(' ID Chain := [EVENT:',x['data'][i]['super_id'],']->[WINDOWS EVENT:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' EVT Source          :=', x['data'][i]['source'])
                            print(' Event ID            :=', x['data'][i]['eventid'])
                            print(' EVT Date & Time     :=', x['data'][i]['evtdatetime'])
                            print(' User                :=', x['data'][i]['user'])
                            print(' Computer            :=', x['data'][i]['computer'])
                            print(' Process ID          :=', x['data'][i]['processid'])
                            print(' Thread ID           :=', x['data'][i]['threadid'])
                            print(' EVT Keywords        :=', x['data'][i]['keywords'])
                    #
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'ipv4'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list ipv4"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[IPV4] ----------------------------------------')
                        print('No IPV4 Event Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[IPV4]---------------------------------------')
                            print(' ID Chain := [EVENT:',x['data'][i]['super_id'],']->[IP:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' IP Version          :=', x['data'][i]['version'])
                            print(' Inet Header Length  :=', x['data'][i]['ihl'])
                            print(' Type of Service     :=', x['data'][i]['tos'])
                            print(' Total Packet Length :=', x['data'][i]['tlen'])
                            print(' Packet ID           :=', x['data'][i]['packident'])
                            print(' Fargmentation Offset:=', x['data'][i]['fragoff'])
                            print(' Time to Live        :=', x['data'][i]['ttl'])
                            print(' Protocol            :=', x['data'][i]['protocol'])
                            print(' Header Check Sum    :=', x['data'][i]['hcs'])
                            print(' Source IP Address   :=', x['data'][i]['sourceip'])
                            print(' Dest IP Address     :=', x['data'][i]['destinationip'])
                    #
                    print('--------------------------------------------------------------------------------')
                # 
                if (commandlist[1] == 'tcp'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list tcp"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[IP]->[TCP] ----------------------------------------')
                        print('No TCP Event Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[IP]->[TCP]---------------------------------------')
                            print(' ID Chain := [IP:',x['data'][i]['super_id'],']->[TCP:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' TCP Source Port     :=', x['data'][i]['sourport'])
                            print(' TCP Destination Port:=', x['data'][i]['destport'])
                            print(' Sequence Number     :=', x['data'][i]['sequnum'])
                            print(' Acknowledgement Num :=', x['data'][i]['acknum'])
                            print(' Windows Size        :=', x['data'][i]['winsize'])
                            print(' Check Sum           :=', x['data'][i]['checksum'])
                            print(' Urgent Pointer      :=', x['data'][i]['urgptr'])
                            print(' Data Offset         :=', x['data'][i]['dataoffset'])
                            print('TCP Flags:')
                            print('    :-> [SYN:',x['data'][i]['synflag'] ,']/[ACK:',x['data'][i]['ackflag'],
                                        ']/[PSH:',x['data'][i]['pushflag'] , ']/[FIN:',x['data'][i]['finflag'] ,']')
                            print('    :-> [URG:',x['data'][i]['urgflag'],']/[CWR:',x['data'][i]['cwrflag']
                                        ,']/[ECN:',x['data'][i]['ecnflag'],']/[RST:',x['data'][i]['rstflag'],']')     
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'udp'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list udp"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[IP]->[UDP] ----------------------------------------')
                        print('No UDP Event Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[IP]->[UDP]---------------------------------------')
                            print(' ID Chain := [IP:',x['data'][i]['super_id'],']->[UDP:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' Packey Checksum     :=', x['data'][i]['checksum'])
                            print(' Packet Length       :=', x['data'][i]['length'])
                            print(' UDP Source Port     :=', x['data'][i]['sourport'])
                            print(' UDP Dest Port       :=', x['data'][i]['destport'])
                    #
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'icmp'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list icmp"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[IP]->[ICMP] ----------------------------------------')
                        print('No ICMP Event Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[IP]->[ICMP]---------------------------------------')
                            print(' ID Chain := [IP:',x['data'][i]['super_id'],']->[ICMP:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' ICMP Packetr Type   :=', x['data'][i]['type'])
                            print(' ICMP Code           :=', x['data'][i]['code'])
                            print(' Packet Checksum     :=', x['data'][i]['checksum'])
                    # 
                    print('--------------------------------------------------------------------------------')
                #
                if (commandlist[1] == 'tcphttp'):
                    #
                    payload = {
                        "method": "addParticle",
                        "params":  ['{"event":"debugger", "command":"list tcphttp"}'],
                        "jsonrpc": "2.0",
                        "id": jsonrpcid, }
                    jsonrpcid = jsonrpcid + 1
                    #
                    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
                    x = json.loads(result['result'])
                    if (x['data'] == 'NONE'):
                        print('---- Event Type := [EVENT]->[IP]->[TCP]->[HTTP] ----------------------------------------')
                        print('No TCP->HTTP Event Particles in Swarm.')
                    else:
                        for i in x['data']:
                            print('---- Event Type := [EVENT]->[IP]->[TCP]->[HTTP]---------------------------------------')
                            print(' ID Chain := [TCP:',x['data'][i]['super_id'],']->[HTTP:',x['data'][i]['identifier'],']')
                            print(' Identifier          :=', x['data'][i]['identifier'])
                            print(' Date and Time       :=', x['data'][i]['datetime'])
                            print(' HTTP Method         :=', x['data'][i]['method'])
                            print(' HTTP User Agent     :=', x['data'][i]['useragent'])
                            print(' HTTP Cookie         :=', x['data'][i]['cookie'])
                            print(' The Full URL        :=', x['data'][i]['fullurl'])
                    #
                    print('--------------------------------------------------------------------------------')
        if (not value): sys.exit()
    return True
#
# classification
#
if __name__ == '__main__':
    runDebugger()
#
#
#
