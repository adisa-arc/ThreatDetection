#
# -------------------------------------------------------------------------------------------------
# This is the FTPD to JSON RPC tool.
# Decsription:     It reads FTPD event encoded in SYSLOG messages and converts then to JSON.
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
def JSONFTPD(data, dtime, eventid, syslogid):
    jsonevent = "{"
    jsonevent = jsonevent + "\"event\": { "
    jsonevent = jsonevent + "\"ftpd\": { "
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str(syslogid) + "\", "
    jsonevent = jsonevent + "\"_type\": \"ftpd\", "
    jsonevent = jsonevent + "\"transfertime\": \"" + str(data[5]) + "\", "
    jsonevent = jsonevent + "\"remotehost\": { "
    jsonevent = jsonevent + "\"_type\": \"ipv4\","
    jsonevent = jsonevent + "\"__text\": \"" + str(data[6]) + "\""
    jsonevent = jsonevent + " }, "
    jsonevent = jsonevent + "\"filesize\": \"" + str(data[7]) + "\", "
    jsonevent = jsonevent + "\"filename\": \"" + str(data[8]) + "\", "
    jsonevent = jsonevent + "\"transfertype\": \"" + str(data[9]) + "\", "
    jsonevent = jsonevent + "\"actionflag\": \"" + str(data[10]) + "\", "
    jsonevent = jsonevent + "\"direction\": \"" + str(data[11]) + "\", "
    jsonevent = jsonevent + "\"accessmode\": \"" + str(data[12]) + "\", "
    jsonevent = jsonevent + "\"username\": \"" + str(data[13]) + "\", "
    jsonevent = jsonevent + "\"servicename\": \"" + str(data[14]) + "\", "
    jsonevent = jsonevent + "\"authmethod\": \"" + str(data[15]) + "\", "
    jsonevent = jsonevent + "\"authuserid\": \"" + str(data[16]) + "\", "
    jsonevent = jsonevent + "\"status\": \"" + str(data[17]) + "\""
    jsonevent = jsonevent + " }, "
    jsonevent = jsonevent + "\"_datetime\": \"" + dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str(eventid) + "\", "
    jsonevent = jsonevent + "\"_type\": \"ftpd\""
    jsonevent = jsonevent + " } "
    jsonevent = jsonevent + " } "
    return jsonevent
#
#
#
def ftpdParsetoJSON(inputline):
    #
    rdata = inputline.replace('\'','')
    data = rdata.split()
    digest = int(hashlib.md5(inputline.encode()).hexdigest()[:8], 16)
    etime = time.mktime(time.gmtime())
    eventid = int(hashlib.md5((str(etime) + str(digest)).encode()).hexdigest()[:8], 16)
    stime = time.mktime(time.gmtime()) + 1
    syslogid = int(hashlib.md5((str(stime) + str(digest)).encode()).hexdigest()[:8], 16)
    dtime = str(data[1]) + " " + str(data[2]) + " " + str(data[3])
    #
    # -> Process as a SYSLOG Message
    jsonevent = JSONFTPD(data, dtime, eventid, syslogid)
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
            jsonparams = ftpdParsetoJSON(contents)
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
    print('FTPD to JSON Converter [ftpdjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: ftpdjsonrpc [-n number] /path/filename\n') 
    print('WHERE:')
    print('      -n number                       - Specifies the number of entries to process.\n')
    print('Examples of Usage:\n')
    print('       ftpdjsonrpc ftpdata.dat       - This will read and process all enties for ever.\n')
    print('       ftpdjsonrpc -n 8 ftpdata.dat  - This will read and process the first 8 entries.\n')
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
            print('FTPD to JSON Converter [ftpdjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
            print(":- ERROR: Insufficent command line arguments.\n\n")
            help()
            sys.exit()
    elif (len(sys.argv) == 2):
        exists = os.path.isfile(sys.argv[1])
        file = sys.argv[1]
    else:
        print('FTPD to JSON Converter [ftpdjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #   
    if not exists:
        print('FTPD to JSON Converter [ftpdjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
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