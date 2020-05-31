#
# -------------------------------------------------------------------------------------------------
# This is the NSCA to JSON RPC tool.
# Decsription:     It reads NSCA event encoded in SYSLOG messages and converts then to JSON.
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
def JSONCEF(data, dtime, eventid, syslogid):
    cefid = syslogid + eventid + 1
    cefRawData = ""
    for i in data[4:-1]: cefRawData = cefRawData + str(i) + " "
    cefData = cefRawData.split("|")
    #
    jsonevent = "{"
    #
    jsonevent = jsonevent + "\"event\": { "
    #
    jsonevent = jsonevent + "\"syslog\": { "
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str(syslogid) + "\", "
    jsonevent = jsonevent + "\"_type\": \"cef\", "
    jsonevent = jsonevent + "\"system\": { "
    jsonevent = jsonevent + "\"type\": \"name\", "
    jsonevent = jsonevent + "\"__text\": \""+ str(data[3]) + "\" "
    jsonevent = jsonevent + "}, "
    jsonevent = jsonevent + "\"process\": { "
    jsonevent = jsonevent + "\"type\": \"proc\", "
    jsonevent = jsonevent + "\"__text\": \""+ str(cefData[0]) + "\" "
    jsonevent = jsonevent + "}, "
    jsonevent = jsonevent + "\"message\": { "
    jsonevent = jsonevent + "\"type\": \"proc\", "
    jsonevent = jsonevent + "\"__text\": \""+ cefRawData + "\" "
    jsonevent = jsonevent + "}, "
    #
    jsonevent = jsonevent + "\"cef\": { "
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str(cefid) + "\", "
    jsonevent = jsonevent + "\"_type\": \"cef\", "
    jsonevent = jsonevent + "\"version\": \"" + str(cefData[0]) + "\", "
    jsonevent = jsonevent + "\"deviceinfo\": \"" + str(cefData[1]) + " " + str(cefData[2]) + " " + str(cefData[3]) + "\", "
    jsonevent = jsonevent + "\"signature\": \"" + str(cefData[4]) + "\", "
    jsonevent = jsonevent + "\"name\": { "
    jsonevent = jsonevent + "\"type\": \"ascii\", "
    jsonevent = jsonevent + "\"__text\": \""+ str(cefData[5]) + "\" "
    jsonevent = jsonevent + "}, "
    jsonevent = jsonevent + "\"severity\": \"" + str(cefData[6]) + "\", "
    jsonevent = jsonevent + "\"exenstions\": { "
    jsonevent = jsonevent + "\"type\": \"ascii\", "
    jsonevent = jsonevent + "\"__text\": \""+ cefData[7] + "\" "
    jsonevent = jsonevent + "} "
    jsonevent = jsonevent + "} "
    #
    jsonevent = jsonevent + "}, "
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str(eventid) + "\", "
    jsonevent = jsonevent + "\"_type\": \"syslog\" "
    #
    jsonevent = jsonevent + "} "
    #
    jsonevent = jsonevent + "} "
    #
    return jsonevent
#
#
#
def CEFParsetoJSON(inputline):
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
    jsonevent = JSONCEF(data, dtime, eventid, syslogid)
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
            jsonparams = CEFParsetoJSON(contents)
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
    print('CEF to JSON Converter [cefjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: cefjsonrpc [-n number] /path/filename\n') 
    print('WHERE:')
    print('      -n number                       - Specifies the number of entries to process.\n')
    print('Examples of Usage:\n')
    print('       cefjsonrpc ftpdata.dat       - This will read and process all enties for ever.\n')
    print('       cefjsonrpc -n 8 ftpdata.dat  - This will read and process the first 8 entries.\n')
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
            print('CEF to JSON Converter [cefjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
            print(":- ERROR: Insufficent command line arguments.\n\n")
            help()
            sys.exit()
    elif (len(sys.argv) == 2):
        exists = os.path.isfile(sys.argv[1])
        file = sys.argv[1]
    else:
        print('CEF to JSON Converter [cefjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #   
    if not exists:
        print('CEF to JSON Converter [cefjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
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