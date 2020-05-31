#
# 
# 
# 
# 
# 
import requests
import json
# 
# 
# 
def rcp(particle, pid, jsonrpcid):
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}
    payload = {
        "method": "addParticle",
        "params":  ['{"event":"debugger", "command":"get ' + particle + ' ' + pid + '"}'],
        "jsonrpc": "2.0",
        "id": jsonrpcid, }
    jsonrpcid = jsonrpcid + 1
    #
    result = requests.post(url, data=json.dumps(payload),headers=headers).json()
    return json.loads(result['result'])

# 
def showPartcile(showlist):   
    #
    jsonrpcid = 1
    #
    if (len(showlist) != 3): 
        print('\nError:> The number of arguments to the st command is incorrect.')
        print('        For example: sh syslog 5364716253\n')
        return True
    #
    if (showlist[1] == 'prediction'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- PREDICTION/Partcile Type := [STIX] ----------------------------------------')
            print('ERROR: No PREDICTION Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #  
        for i in xjson:
            print('---- Event Type := [PREDICTION] -------------------------------------------------------')
            print(' ID Chain := [PREDICTION:',xjson[i]['identifier'],']')
            print('PREDICTION Type        :=', xjson[i]['type'])
            print('PREDICTION Identifier  :=', xjson[i]['identifier'])
            print('PREDICTION Date & Time :=', xjson[i]['datetime'])
            print('PREDICTION References  :=', xjson[i]['references'])
            print('--------------------------------------------------------------------------------')

    if (showlist[1] == 'stix'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- STIX/Partcile Type := [STIX] --------------------------------------------')
            print('ERROR: No STIX Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #  
        for i in xjson:
            print('\n---- Event Type := [STIX] -------------------------------------------------------')
            print(' ID Chain := [STIX:',xjson[i]['identifier'],']')
            print('STIX Type              :=', xjson[i]['type'])
            print('STIX Name              :=', xjson[i]['name'])
            print('STIX Identifier        :=', xjson[i]['identifier'])
            print('STIX Description       :=', xjson[i]['description'])
            print('STIX Creation Time     :=', xjson[i]['cdatetime'])
            print('STIX Modification Time :=', xjson[i]['mdatetime'])
            print('STIX Description       :=', xjson[i]['description'])
            print('STIX Pattern           :=', xjson[i]['pattern'])
            print('STIX Kill Chain Phase  :=', xjson[i]['killchainphase'])
            print('STIX Labels            :=', xjson[i]['lables'])
            print('STIX External Refs     :=', xjson[i]['externalrefs'])
            print('STIX Relationship Type :=', xjson[i]['relationship_type'])
            print('STIX Source Reference  :=', xjson[i]['source_ref'])
            print('STIX Target Reference  :=', xjson[i]['target_ref']) 
            print('--------------------------------------------------------------------------------') 
    elif (showlist[1] == 'event'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [EVENT] --------------------------------------------')
            print('ERROR: No Event Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT] --------------------------------------------')
            print('ID Chain := [EVENT:',xjson[i]['identifier'],']')
            print('Event Identifier      :=', xjson[i]['identifier'])
            print('Event Date and Time   :=', xjson[i]['datetime'])
            print('Event Sub Type        :=', xjson[i]['subtype'])
            print('Event Sub Type Ident  :=', xjson[i]['sub_id'], '\n')
            print('----------------------------------------------------------------------------------')
        #
    elif (showlist[1] == 'syslog'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [SYSLOG] -------------------------------------------')
            print('ERROR: No Syslog Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT]->[SYSLOG] ----------------------------------')
            print(' ID Chain := [EVENT:',xjson[i]['suptype_id'],']->[SYSLOG:',xjson[i]['identifier'],']')
            print(' Identifier             :=', xjson[i]['identifier'])
            print(' Date and Time          :=', xjson[i]['datetime'])
            print(' Super Type[Identifier] :=', xjson[i]['suptype'], '[', xjson[i]['suptype_id'], ']')
            print(' Sub Type[Identifier]   :=', xjson[i]['subtype'], '[', xjson[i]['subtype_id'], ']')
            print(' System                 :=', xjson[i]['system'])
            print(' Process[Identifier]    :=', xjson[i]['process_name'],'[', xjson[i]['process_id'], ']')
            print(' Message                :=', xjson[i]['data'], '\n')
            print('----------------------------------------------------------------------------------')
        #
    elif (showlist[1] == 'snort'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [SNORT] --------------------------------------------')
            print('ERROR: No Snort Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson: 
            print('\n---- Event/Partcile Type := [EVENT]->[SYSLOG]->[SNORT] --------------------------')
            print(' ID Chain := [SYSLOG:',xjson[i]['suptype_id'],']->[SNORT:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' System              :=', xjson[i]['system'])
            print(' Version             :=', xjson[i]['version'])
            print(' Classification      :=', xjson[i]['classification'])
            print(' Priority            :=', xjson[i]['priority'])
            print(' |----> Protocol             :=', xjson[i]['protocol'])
            print(' |----> Snort Alert Message  :=', xjson[i]['message'])
            print(' |----> SRC IP Address       :=', xjson[i]['src'])
            print(' |----> SRC Port Address     :=', xjson[i]['srcport'])
            print(' |----> DST IP Address       :=', xjson[i]['dst'])
            print(' |----> DST Port Address     :=', xjson[i]['dstport'])
        #
    elif (showlist[1] == 'sshd'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [SSHD] ---------------------------------------------')
            print('ERROR: No SSHD Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson: 
            print('\n---- Event/Partcile Type := [EVENT]->[SYSLOG]->[SSHD] --------------------------')
            print(' ID Chain := [SYSLOG:',xjson[i]['suptype_id'],']->[SSHD:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' System              :=', xjson[i]['system'])
            print(' Process             :=', xjson[i]['process'])
            print(' Source IP Address   :=', xjson[i]['sourceaddr'])
            print(' Source Port         :=', xjson[i]['sourceport'])
            print(' Username            :=', xjson[i]['username'])
            print(' Raw Data            :=', xjson[i]['data'])
            #
            print('--------------------------------------------------------------------------------')
        #
    elif (showlist[1] == 'vsftpd'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [VSFTPD] -------------------------------------------')
            print('ERROR: No VSFTPD Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson: 
            print('\n---- Event/Partcile Type := [EVENT]->[SYSLOG]->[VSFTPD] --------------------------')
            print(' ID Chain := [SYSLOG:',xjson[i]['suptype_id'],']->[VSFTPD:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' Username            :=', xjson[i]['username'])
            print(' Command Type        :=', xjson[i]['commandtype'])
            print(' Source Address      :=', xjson[i]['sourceaddr'])
            print(' Raw Data            :=', xjson[i]['data'])
            #
            print('--------------------------------------------------------------------------------')
        #
    elif (showlist[1] == 'tcpd'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [TCPD] ---------------------------------------------')
            print('ERROR: No TCPD Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT]->[SYSLOG]->[TCPD] --------------------------')
            print(' ID Chain := [SYSLOG:',xjson[i]['suptype_id'],']->[TCPD:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' System              :=', xjson[i]['system'])
            print(' Process             :=', xjson[i]['process'])
            print(' Connection          :=', xjson[i]['connection'])
            #
            print('--------------------------------------------------------------------------------')
        #
    elif (showlist[1] == 'cef'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [CEF] ----------------------------------------------')
            print('ERROR: No CEF Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT]->[SYSLOG]->[CEF] --------------------------')
            print(' ID Chain := [SYSLOG:',xjson[i]['suptype_id'],']->[CEF:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' Version             :=', xjson[i]['version'])
            print(' Device Info         :=', xjson[i]['deviceinfo'])
            print(' Source IP Address   :=', xjson[i]['sourceip'])
            print(' CEF Signature       :=', xjson[i]['signature'])
            print(' Severity            :=', xjson[i]['severity'])
            print(' CEF Exenstions      :=', xjson[i]['exenstions'])
            #
            print('--------------------------------------------------------------------------------')
        #
    elif (showlist[1] == 'nsca'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [NSCA] ---------------------------------------------')
            print('ERROR: No NCSA Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT]->[NSCA] ------------------------------------')
            print(' ID Chain := [EVENT:',xjson[i]['suptype_id'],']->[NSCA:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' Client              :=', xjson[i]['client'])
            print(' User ID             :=', xjson[i]['userid'])
            print(' User                :=', xjson[i]['user'])
            print(' NSCA Request        :=', xjson[i]['request'])
            print(' Status Code         :=', xjson[i]['statuscode'])
            print(' The Size            :=', xjson[i]['size'])
            #
            print('--------------------------------------------------------------------------------')
    elif (showlist[1] == 'dns'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [DNS] ----------------------------------------------')
            print('ERROR: No DNS Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT]->[DNS] -----------------------------------')
            print(' ID Chain := [EVENT:',xjson[i]['suptype_id'],']->[DNS:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' Requester           :=', xjson[i]['requester'])
            print(' DNS Request         :=', xjson[i]['request'])
            print(' DNS Request Type    :=', xjson[i]['requesttype'])
            #
            print('--------------------------------------------------------------------------------')
    elif (showlist[1] == 'netflow'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [NETFLOW] ------------------------------------------')
            print('ERROR: No NetFlow Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT]->[NETFLOW] ----------------------------------')
            print(' ID Chain := [EVENT:',xjson[i]['suptype_id'],']->[NETFLOW:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' Duration of Flow    :=', xjson[i]['duration'])
            print(' Protocol            :=', xjson[i]['protocol'])
            print(' Source IP Addrress  :=', xjson[i]['sourceip'])
            print(' Source Port         :=', xjson[i]['sourceport'])
            print(' Dest IP Address     :=', xjson[i]['destinationip'])
            print(' Destination Port    :=', xjson[i]['destport'])
            print(' No of Packets       :=', xjson[i]['packets'])
            print(' No of Bytes in Flow :=', xjson[i]['pbytes'])
            #
            print('--------------------------------------------------------------------------------')
    elif (showlist[1] == 'ftpd'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [FTPD] ---------------------------------------------')
            print('ERROR: No FTPD Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT]->[FTPDDDDD] ----------------------------------')
            print(' ID Chain := [EVENT:',xjson[i]['suptype_id'],']->[FTPD:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' Transfer Time       :=', xjson[i]['transfertime'])
            print(' Remote Host         :=', xjson[i]['remotehost'])
            print(' Filesize            :=', xjson[i]['filesize'])
            print(' FTP Filename        :=', xjson[i]['filename'])
            print(' Transfer Type       :=', xjson[i]['transfertype'])
            print(' Action Flag         :=', xjson[i]['actionflag'])
            print(' FTP Direction       :=', xjson[i]['direction'])
            print(' Access Mode         :=', xjson[i]['accessmode'])
            print(' Username            :=', xjson[i]['username'])
            print(' Service Name        :=', xjson[i]['servicename'])
            print(' Auth Method         :=', xjson[i]['authmethod'])
            print(' Authuser ID         :=', xjson[i]['authuserid'])
            print(' FTP Status Code     :=', xjson[i]['status'])
            #
            print('--------------------------------------------------------------------------------')
    elif (showlist[1] == 'evt'):
        #
        xjson = rcp(showlist[1], showlist[2], jsonrpcid)['data']
        if (xjson == 'NULL'):
            print('\n---- Event/Partcile Type := [EVT] ----------------------------------------------')
            print('ERROR: No Micorosft Windows Event(EVT) Identifier found in Database or Cache.')
            print('----------------------------------------------------------------------------------')
            return True
        #
        for i in xjson:
            print('\n---- Event/Partcile Type := [EVENT]->[EVT] ----------------------------------')
            print(' ID Chain := [EVENT:',xjson[i]['suptype_id'],']->[EVT:',xjson[i]['identifier'],']')
            print(' Identifier          :=', xjson[i]['identifier'])
            print(' Date and Time       :=', xjson[i]['datetime'])
            print(' Event ID            :=', xjson[i]['eventid'])
            print(' EVT Date & Time     :=', xjson[i]['evtdatetime'])
            print(' User                :=', xjson[i]['user'])
            print(' Computer            :=', xjson[i]['computer'])
            print(' Process ID          :=', xjson[i]['processid'])
            print(' Thread ID           :=', xjson[i]['threadid'])
            print(' EVT Keywords        :=', xjson[i]['keywords'])
            #
            print('--------------------------------------------------------------------------------')
    elif (showlist[1] == 'ip'):
        #
        _ = rcp(showlist[1], showlist[2], jsonrpcid)
        #
    elif (showlist[1] == 'tcp'):
        #
        _ = rcp(showlist[1], showlist[2], jsonrpcid)
        #
    elif (showlist[1] == 'udp'):
        #
        _ = rcp(showlist[1], showlist[2], jsonrpcid)
        #
    elif (showlist[1] == 'icmp'):
        #
        _ = rcp(showlist[1], showlist[2], jsonrpcid)
        #
    elif (showlist[1] == 'tcphttp'):
        #
        _ = rcp(showlist[1], showlist[2], jsonrpcid)
        #
    return True
#
#
#
