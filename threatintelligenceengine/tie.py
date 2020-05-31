#
# -------------------------------------------------------------------------------------------------
# This is the STIX Database Inserter tool.
# Decsription:     It reads STIX objects encoded in JSON. It then makes an json RPC request to a 
#                  server to register/assert the STIX object as a particle.
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
DEBUG = True
#
#
# 
#
#
def processSTIXFile(JSONFile):
    jdata = JSONFile.read()
    jsonrpcid = 1
    if len(jdata) != 0:
            #
            #
            # -> Parse for a SYSLOG Type Message
            jsonparams = jdata
            url = "http://localhost:4000/jsonrpc"
            headers = {'content-type': 'application/json'}
            #
            #
            # -> Marshall the JSON RPC Components
            payload = {
                "method": "addStixObject",
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
    return True
#
#
#
def help():
    print('STIX Database Inserter [tie] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: tie /path/filename\n') 
    print('       tie stix.json       - This will read and process all STIX JSON entries.\n')
#
#
#
def main(): 
    #
    if (len(sys.argv) == 2):
        exists = os.path.isfile(sys.argv[1])
        file = sys.argv[1]
    else:
        print('STIX Database Inserter [tie] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #   
    if not exists:
        print('STIX Database Inserter [tie] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: File '" + file + "' not found or unaccessable.\n")
        help()
        sys.exit()
    #
    try:
        openfile = open(file,'r')
        processSTIXFile(openfile)
        jsonparams = "{}"
        # -> Distribute Prediction Particles around the Global Vetcor Space Matrix [Vs]
        url = "http://localhost:4000/jsonrpc"
        headers = {'content-type': 'application/json'}
        jsonrpcid = 1
        payload = {
                "method": "distributePredictionParticle",
                "params": [jsonparams],
                "jsonrpc": "2.0",
                "id": jsonrpcid, }
        response = requests.post(url, data=json.dumps(payload), headers=headers).json()
        if DEBUG:
                print("---distributePredictionParticleinGVSM---------------------------------------------------------")
                print("--Payload-------------------------------------------------------------------------------------")
                print(payload)
                print(response)
                print("##############################################################################################")
                print("")
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