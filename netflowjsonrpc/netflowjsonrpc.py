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
import xmltodict
#
#
#
DEBUG = False 
#
#
#
#
#
#
def NETFLOWParsetoJSON(data):
    #
    # -> Process as a Netflow XML Data into JSON Data
    __dtime = data['event']['netflow']['@datetime']
    __ident = data['event']['netflow']['@ident']
    nettime = data['event']['netflow']['datetime']
    duratin = data['event']['netflow']['duration']
    protocl = data['event']['netflow']['protocol']
    sourcip = data['event']['netflow']['sourceip']
    sourcpt = data['event']['netflow']['sourceport']
    destnip = data['event']['netflow']['destinationip']
    destprt = data['event']['netflow']['destinationport']
    packets = data['event']['netflow']['packets']
    ptbytes = data['event']['netflow']['bytes']
    #
    jsonevent = "{"
    jsonevent = jsonevent + "\"event\": { "
    jsonevent = jsonevent + "\"netflow\": { "
    jsonevent = jsonevent + "\"_datetime\": \"" + nettime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ __ident + "\", "
    jsonevent = jsonevent + "\"_type\": \"netflow\","
    jsonevent = jsonevent + "\"duration\": \""+ duratin + "\", "
    jsonevent = jsonevent + "\"protocol\": \""+ protocl + "\", "
    jsonevent = jsonevent + "\"sourceip\": \""+ sourcip + "\", "
    jsonevent = jsonevent + "\"sourceport\": \""+ sourcpt + "\", "
    jsonevent = jsonevent + "\"destinationip\": \""+ destnip + "\", "
    jsonevent = jsonevent + "\"destport\": \""+ destprt + "\", "
    jsonevent = jsonevent + "\"packets\": \""+ packets + "\", "
    jsonevent = jsonevent + "\"bytes\": \""+ ptbytes + "\" "
    jsonevent = jsonevent + "},  " 
    jsonevent = jsonevent + "\"_datetime\": \"" + __dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str((int(__ident) + 1))+ "\", "
    jsonevent = jsonevent + "\"_type\": \"netflow\""
    jsonevent = jsonevent + "} " 
    jsonevent = jsonevent + "} " 
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
def processSyslogFile(filenames):
    #
    jsonrpcid = 1
    for file in filenames:
        with open(file) as fd:
            doc = xmltodict.parse(fd.read())
        jsonparams = NETFLOWParsetoJSON(doc)
        #
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
    # 
    return True
#
#
#
def help():
    print('NETFLOW to JSON Converter [netflowjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: netflowjsonrpc [/path/filenameA] . . . /path/filenameZ\n') 
    print('Examples of Usage:\n')
    print('       netflowjsonrpc ../../netflow.xml    - This will read and process all enties for ever.\n')
    print('       netflowjsonrpc flow1.xml flow2.xml  - This will read and process the first 8 entries.\n')
#
#
#
def main(): 
    #
    if (len(sys.argv) < 2):
        print('NETFLOW to JSON Converter [netflowjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #
    files = (sys.argv[1:])
    try:
        processSyslogFile(files)
    #
    except Exception as e:
        print("Exception Error in processing:- " + e)
    #
    return True
#ß
#
#
if __name__ == "__main__":
    main()
#
#