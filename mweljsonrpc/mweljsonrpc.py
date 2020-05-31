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
def MWELParsetoJSON(data):
    #
    # -> Process as a Windows Event Log XML Data into JSON Data
    __dtime = data['event']['evt']['@datetime']
    __ident = data['event']['evt']['@ident']
    msource = data['event']['evt']['source']
    eventid = data['event']['evt']['eventid']
    datetim = data['event']['evt']['datetime']
    mweuser = data['event']['evt']['user']
    computr = data['event']['evt']['computer']
    procsid = data['event']['evt']['processid']
    thredid = data['event']['evt']['threadid']
    keywrds = data['event']['evt']['keywords']
    #
    jsonevent = "{"
    jsonevent = jsonevent + "\"event\": { "
    jsonevent = jsonevent + "\"evt\": { "
    jsonevent = jsonevent + "\"_datetime\": \"" + datetim + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ __ident + "\", "
    jsonevent = jsonevent + "\"_type\": \"evt\","
    jsonevent = jsonevent + "\"source\": \"" + msource + "\", "
    jsonevent = jsonevent + "\"eventid\": \"" + eventid + "\", "
    jsonevent = jsonevent + "\"datetime\": \"" + datetim + "\", "
    jsonevent = jsonevent + "\"user\": \"" + mweuser + "\", "
    jsonevent = jsonevent + "\"computer\": \"" + computr + "\", "
    jsonevent = jsonevent + "\"processid\": \"" + procsid + "\", "
    jsonevent = jsonevent + "\"threadid\": \"" + thredid + "\", "
    jsonevent = jsonevent + "\"keywords\": \"" + keywrds + "\" "
    jsonevent = jsonevent + "},  " 
    jsonevent = jsonevent + "\"_datetime\": \"" + __dtime + "\", "
    jsonevent = jsonevent + "\"_ident\": \""+ str((int(__ident) + 1))+ "\", "
    jsonevent = jsonevent + "\"_type\": \"evt\""
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
        jsonparams = MWELParsetoJSON(doc)
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
    print('Windows Event Log to JSON Converter [mweljsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: mweljsonrpc [/path/filenameA] . . . /path/filenameZ\n') 
    print('Examples of Usage:\n')
    print('       mweljsonrpc ../../netflow.xml    - This will read and process all enties for ever.\n')
    print('       mweljsonrpc flow1.xml flow2.xml  - This will read and process the first 8 entries.\n')
#
#
#
def main(): 
    #
    if (len(sys.argv) < 2):
        print('Windows Event Log to JSON Converter [mweljsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
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