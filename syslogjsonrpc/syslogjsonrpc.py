#
# -------------------------------------------------------------------------------------------------
# This is the SYSLOG to JSON RPC tool.
# Decsription:     It reads SNORT event encoded in SYSLOG messages and converts then to JSON.
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
#
def JSONSyslog(data, dtime, eventid, syslogid):
    jsonevent = "{"
    jsonevent = jsonevent + "\"event\": { "
    jsonevent = jsonevent + "\"syslog\": { "
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str(syslogid) + "\", "
    jsonevent = jsonevent + "\"_type\": \"syslog\","
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
def syslogParsetoJSON(inputline):
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
    jsonevent = JSONSyslog(data, dtime, eventid, syslogid)
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
            jsonparams = syslogParsetoJSON(contents)
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
def help():
    print('SYSLOG to JSON Converter [syslogjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: syslogjsonrpc [-n number] /path/filename\n') 
    print('WHERE:')
    print('      -n number                       - Specifies the number of entries to process.\n')
    print('Examples of Usage:\n')
    print('       syslogjsonrpc syslogdata.dat       - This will read and process all enties for ever.\n')
    print('       syslogjsonrpc -n 8 syslogdata.dat  - This will read and process the first 8 entries.\n')
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
            print('SYSLOG to JSON Converter [syslogjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
            print(":- ERROR: Insufficent command line arguments.\n\n")
            help()
            sys.exit()
    elif (len(sys.argv) == 2):
        exists = os.path.isfile(sys.argv[1])
        file = sys.argv[1]
    else:
        print('SYSLOG to JSON Converter [syslogjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #   
    if not exists:
        print('SYSLOG to JSON Converter [syslogjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
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