#
# -------------------------------------------------------------------------------------------------
# This is the Generic Insert for events into the JSON RPC tool.
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
DEBUG = True
#
#
#
#
#
def parsejsoninput(contents):
    try:
        json.loads(contents)
    except:
        return False
    return True
#
#
#
def genericjsoninsert():
    #
    jsonrpcid = 1
    #
    while(True):
        try:
            jsonparams = input()
            print(jsonparams)
        except:
            sys.exit()
        if len(jsonparams) != 0:
            #
            #
            # -> Parse for a SYSLOG Type Message
            if (parsejsoninput(jsonparams)):
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
    return True
#
#
#
def help():
    print('Generic Inserter to JSON Converter [insertjsonsrc] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: insertjsonsrc \n') 
    print('Examples of Usage:\n')
    print('       cat ../event.dat | insertjsonsrc       - This will insert the data read from standard input.\n')
#
#
#
def main(): 
    #
    if (len(sys.argv) != 1):
        print('VSTFPD to JSON Converter [vsftpjsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #
    try:
        genericjsoninsert()
    #
    except:
        return False
    #
    return True
#
#
#
if __name__ == "__main__":
    main()
#
#
