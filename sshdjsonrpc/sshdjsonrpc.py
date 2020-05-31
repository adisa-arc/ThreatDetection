#
# -------------------------------------------------------------------------------------------------
# This is the SSHD to JSON RPC tool.
# Decsription:     It reads SSHD event encoded in SYSLOG messages and converts then to JSON.
#                  It then makes an json RPC request to a server to register/assert the event.
# Date:            19th April 2019
# Author:          andrew.blyth@adisa.global
# -------------------------------------------------------------------------------------------------
#
#
import sys
import os
import datetime
import hashlib
import time
import requests
import json
#
#
#
#
DEBUG = False
#
#
#
def arraytostr(sdata):
    rstr = ""
    for i in sdata:
        rstr = rstr + str(i) + " "
    return rstr[0:len(rstr)-1]
#
#
#
def JSONSSHD(data, dtime, eventid, syslogid):
    sshid = eventid + syslogid + 1
    jsonevent = "{"
    jsonevent = jsonevent + "\"event\": { "
    jsonevent = jsonevent + "\"syslog\": { "
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str(syslogid) + "\", "
    jsonevent = jsonevent + "\"_type\": \"sshd\","
    jsonevent = jsonevent + "\"system\": { "
    jsonevent = jsonevent + "\"_type\": \"name\","
    jsonevent = jsonevent + "\"__text\": \"" + str(data[3]) + "\""
    jsonevent = jsonevent + " },"
    jsonevent = jsonevent + "\"process\": { "
    if ("[" in str(data[4])):
        jsonevent = jsonevent + "\"_type\": \"papid\","
        jsonevent = jsonevent + "\"__text\": \"" + str(data[4]) + "\""
    else:
        jsonevent = jsonevent + "\"_type\": \"proc\","
        jsonevent = jsonevent + "\"__text\": \"" + str(data[4]) + "\""
    jsonevent = jsonevent + " },"
    jsonevent = jsonevent + "\"message\": { "
    jsonevent = jsonevent + "\"_type\": \"ascii\","
    jsonevent = jsonevent + "\"__text\": \"" + arraytostr(data[5:len(data)]) + "\""
    jsonevent = jsonevent + " }, "
    jsonevent = jsonevent + "\"sshd\" : {"
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\","
    jsonevent = jsonevent + "\"_ident\": \""+ str(sshid) + "\","
    jsonevent = jsonevent + "\"_type\": \"sshd\", "
    jsonevent = jsonevent + "\"system\": { "
    jsonevent = jsonevent + "\"_type\": \"name\","
    jsonevent = jsonevent + "\"__text\": \"" + str(data[3]) + "\""
    jsonevent = jsonevent + " },"
    jsonevent = jsonevent + "\"process\": { "
    if ("[" in str(data[4])):
        jsonevent = jsonevent + "\"_type\": \"papid\","
        jsonevent = jsonevent + "\"__text\": \"" + str(data[4]) + "\""
    else:
        jsonevent = jsonevent + "\"_type\": \"proc\","
        jsonevent = jsonevent + "\"__text\": \"" + str(data[4]) + "\""
    jsonevent = jsonevent + " },"
    #
    username = "NULL"
    sourceip = "NULL"
    sourcept = "NULL"
    smessage = arraytostr(data[5:len(data)])
    if (str(data[5]) == "Failed" or str(data[5]) == "Accepted"):
        username = str(data[8])
        sourceip = str(data[10])
        sourcept = str(data[12])
    elif (str(data[5]) == "Connection"):
        sourceip = str(data[8])
        sourcept = str(data[10])
    elif (str(data[5]) == "Received"):
        sourceip = str(data[8])
        sourcept = str(str(data[10]).split(':')[0])
    elif (str(data[5]) == "Disconnected"):
        sourceip = str(data[7])
        sourcept = str(data[9])
    jsonevent = jsonevent + "\"sourceaddr\": { "
    jsonevent = jsonevent + "\"_type\": \"ipv4\","
    jsonevent = jsonevent + "\"__text\": \"" + sourceip + "\""
    jsonevent = jsonevent + " },"
    jsonevent = jsonevent + "\"sourceport\": \"" + sourcept + "\","
    jsonevent = jsonevent + "\"username\": \"" + username + "\","
    jsonevent = jsonevent + "\"message\": { "
    jsonevent = jsonevent + "\"_type\": \"ascii\","
    jsonevent = jsonevent + "\"__text\": \"" + smessage + "\""
    jsonevent = jsonevent + " }"
    #
    jsonevent = jsonevent + " } "
    jsonevent = jsonevent + " }, "
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\","
    jsonevent = jsonevent + "\"_ident\": \""+ str(eventid) + "\","
    jsonevent = jsonevent + "\"_type\": \"syslog\""
    jsonevent = jsonevent + " } "
    jsonevent = jsonevent + " } "
    return jsonevent
#
#
#
def sshdParsetoJSON(inputline):
    #
    rdata = inputline.replace('\'','')
    data = rdata.split()
    digest = int(hashlib.md5(inputline.encode()).hexdigest()[:8], 16)
    etime = time.mktime(time.gmtime())
    eventid = int(hashlib.md5((str(etime) + str(digest)).encode()).hexdigest()[:8], 16)
    stime = time.mktime(time.gmtime()) + 1
    syslogid = int(hashlib.md5((str(stime) + str(digest)).encode()).hexdigest()[:8], 16)
    dtime = str(data[0]) + " " + str(data[1]) + " " + str(data[2])
    #
    # -> Process as a SYSLOG Message
    jsonevent = JSONSSHD(data, dtime, eventid, syslogid)
    if DEBUG:
        print("->The RAW Data<-------------------------------------------------------------------------------")
        print(data)
        print("->The JSON Data-------------------------------------------------------------------------------")
        print(jsonevent)
        print("##############################################################################################")
    #
    return jsonevent
#
#
#
def processSyslogFile(filename, count):
    counter = int(count)
    # -> Create the JSON RPC Counter for the RPC Identifier
    jsonrpcid = 1
    # -> Parse the Contents of the Syslog file
    while(counter != 0):
        contents = filename.readline()
        if len(contents) != 0:
            #
            #
            # -> Parse for a SYSLOG Type Message
            jsonparams = sshdParsetoJSON(contents)
            url = "http://localhost:4000/jsonrpc"
            headers = {'content-type': 'application/json'}
            #
            #
            # -> Marshall the JSON RPC Components
            payload = {
                "method": "addParticle",
                "params": [jsonparams],
                "jsonrpc": "2.0",
                "id": jsonrpcid, }
            #
            #
            # -> Make/execute the JSON RPC
            response = requests.post(url, data=json.dumps(payload), headers=headers).json()
            #
            #
            # -> Manage/Update the JSON RPC Counter
            jsonrpcid = jsonrpcid + 1
            if jsonrpcid > 65535:
                jsonrpcid = 1
            #
            if DEBUG:
                print("--Payload-------------------------------------------------------------------------------------")
                print(payload)
                print("---Response-----------------------------------------------------------------------------------")
                print(response)
                print("##############################################################################################")
                print("")
                #
        if (int(counter) > -1): counter = counter - 1
    #
    return 1
#
#
#
#
#
def help():
    print('SSHD to JSON Converter [sshdjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: sshdjsonrpc [-n number] /path/filename\n') 
    print('WHERE:')
    print('      -n number                       - Specifies the number of entries to process.\n')
    print('Examples of Usage:\n')
    print('       sshdjsonrpc sshddata.dat       - This will read and process all enties for ever.\n')
    print('       sshdjsonrpc -n 8 sshddata.dat  - This will read and process the first 8 entries.\n')
#
#
#
def main(): 
    #
    count = -1
    if (len(sys.argv) == 4):
        if (sys.argv[1] == "-n"):
            exists = os.path.isfile(sys.argv[3])
            file = sys.argv[3]
            count = sys.argv[2]
        else:
            print('SSHD to JSON Converter [sshdjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
            print(":- ERROR: Insufficent command line arguments.\n\n")
            help()
            sys.exit()
    elif (len(sys.argv) == 2):
        exists = os.path.isfile(sys.argv[1])
        file = sys.argv[1]
    else:
        print('SSHD to JSON Converter [sshdjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #   
    if not exists:
        print('SYSLOG to JSON Converter [sshdjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: File '" + file + "' not found or unaccessable.\n")
        help()
        sys.exit()
    #
    try:
        openfile = open(file,'r')
        processSyslogFile(openfile, count)
    #
    except Exception as e:
        print("Exception Error in processing:- " + e)
    #
    return 1
#
#
#
if __name__ == "__main__":
    main()
#
#