#
# -------------------------------------------------------------------------------------------------
# This is the Data XML to JSON RPC tool.
# Decsription:     It reads Data Particles encoded in XML and converts then to JSON.
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
import binascii
import xmltodict
#
DEBUG = True
#
# -> This functions reads an XMLFile and converted to a set of json objects.
#
def DataXMLtoJSON(XMLFile):
    xDocList = []
    xDoc = xmltodict.parse(XMLFile.read())
    for x in xDoc['dataparticles']['dataparticle']:
        print(x)
        jData = '{ \"data\" : { '
        jData = jData + '\"_datetime\": \"' + x['datatime'] + '\", '
        jData = jData + '\"_ident\": \"' + x['@ident'] + '\", '
        jData = jData + '\"_type\": \"data\",'
        jData = jData + '\"_name\": \"' + x['@name'] + '\", '
        data = binascii.hexlify(str(x['external_id']).encode('utf-8')).decode('utf-8')
        jData = jData + '\"_external_id\": \"' + data + '\" '
        jData = jData + ' } }'
        xDocList.append(jData)
    #
    return xDocList
#
# -> This function call the DataXMLtoJSON and for the returned list it make JSON RPC calls.
#
def processDataFile(filename):
    # -> Create the JSON RPC Counter for the RPC Identifier
    jsonrpcid = 1
    # -> Parse the Contents of the XML file to the jsonparamsList function
    jsonparamsList = DataXMLtoJSON(filename)
    #
    for jsonparams in jsonparamsList:
        #
        #
        # -> Parse for a SYSLOG Type Message
        url = "http://localhost:4000/jsonrpc"
        headers = {'content-type': 'application/json'}
        #
        #
        # -> Marshall the JSON RPC Components
        payload = {
            "method": "addDataParticle",
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
        if jsonrpcid > 65535: jsonrpcid = 1
        # 
        # 
        # -> Print Degug Information.
        if DEBUG:
            print("--Parameter-----------------------------------------------------------------------------------")
            print(jsonparams)
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
# -> This is the help function for the the Data XML to JSON RPC tool.
#
def help():
    print('DATA to JSON Converter [datajsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: datajsonrpc [-n number] /path/filename\n') 
    print('Examples of Usage:\n')
    print('       dnsjsonrpc data.xmlt       - This will read and process all enties for ever.\n')
#
# -> This is the main function for the the Data XML to JSON RPC tool.
#
def main(): 
    #
    if (len(sys.argv) == 2):
        exists = os.path.isfile(sys.argv[1])
        file = sys.argv[1]
    else:
        print('DATA to JSON Converter [datajsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #   
    if not exists:
        print('DATA to JSON Converter [datajsonrpc] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: File '" + file + "' not found or unaccessable.\n")
        help()
        sys.exit()
    #
    try:
        openfile = open(file,'r')
        processDataFile(openfile)
    #
    except Exception as e:
        print("Exception Error in processing:- " + e)
    #
    return 1
#
# -> This is the command line invocation test for the the Data XML to JSON RPC tool.
#
if __name__ == "__main__":
    main()
#
#