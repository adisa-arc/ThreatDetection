#
#
#
#
#
#
#
#
#
def debugger(jdata, database): 
    #
    result = "{ \"retrunValue\" : \"True\" }"
    #
    command = jdata['command'].split(" ")
    #
    if (command[0] == 'get'):
        #
        try: 
            data = database._cacheDB[command[1]][command[2]]
        except:
            print('ERROR: Illegal Search command[1] :=', command[1])
            print('ERROR: Illegal Searchcommand[2] :=', command[2])
            result = "{ \"retrunValue\" : \"True\", \"data\" : \"NULL\" }"
            return(result)
        #
        # 
        #
        if (command[1] == 'prediction'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"name\" : \"" + data._name + "\", "
            particle = particle + "\"type\" : \"" + data._type + "\", "
            particle = particle + "\"datetime\" : \"" + data._datetime + "\", "
            particle = particle + "\"references\" : \"" + str(data._references) + "\"} "
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle + " } }"
            return(result)
        elif (command[1] == 'stix'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"name\" : \"" + data._name + "\", "
            particle = particle + "\"type\" : \"" + data._type + "\", "
            particle = particle + "\"cdatetime\" : \"" + data._cdatetime + "\", "
            particle = particle + "\"mdatetime\" : \"" + data._cdatetime + "\", "
            particle = particle + "\"description\" : \"" + data._description + "\", "
            particle = particle + "\"pattern\" : \"" + data._pattern + "\", "
            particle = particle + "\"killchainphase\" : \"" + str(data._killchainphase) + "\", "
            particle = particle + "\"lables\" : \"" + str(data._lables) + "\", "
            particle = particle + "\"externalrefs\" : \"" + str(data._externalrefs) + "\", "
            particle = particle + "\"relationship_type\" : \"" + data._relationship_type + "\", "
            particle = particle + "\"source_ref\" : \"" + str(data._source_ref) + "\", "
            particle = particle + "\"target_ref\" : \"" + str(data._target_ref) + "\"} "
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle + " } }"
            return(result)
        elif (command[1] == 'event'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"sub_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"super_id\" : \"" + data._super_id  + "\"} "
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle + " } }"
            return(result)
        elif (command[1] == 'syslog'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"system\" : \"" + data._system + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"process_name\" : \"" + data._process_name + "\", "
            particle = particle + "\"process_id\" : \"" + data._process_id + "\", "
            particle = particle + "\"super_id\" : \"" + data._super_id  + "\", "
            particle = particle + "\"sub_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"data\" : \"" + data._data['message']['__text'] + "\"} "
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } }"
            return(result)
        elif (command[1] == 'snort'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"system\" : \"" + data._system + "\", "
            particle = particle + "\"version\" : \"" + data._version + "\", "
            particle = particle + "\"classification\" : \"" + data._classification + "\", "
            particle = particle + "\"priority\" : \"" + data._priority + "\", "
            particle = particle + "\"protocol\" : \"" + data._protocol + "\", "
            particle = particle + "\"message\" : \"" + data._message + "\", "
            particle = particle + "\"dst\" : \"" + data._dst + "\", "
            particle = particle + "\"dstport\" : \"" + data._dstport + "\", "
            particle = particle + "\"src\" : \"" + data._src + "\", "
            particle = particle + "\"srcport\" : \"" + data._srcport + "\""
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'sshd'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"system\" : \"" + data._system + "\", "
            particle = particle + "\"process\" : \"" + data._process + "\", "
            particle = particle + "\"sourceaddr\" : \"" + data._sourceaddr + "\", "
            particle = particle + "\"sourceport\" : \"" + data._sourceport + "\", "
            particle = particle + "\"username\" : \"" + data._username + "\", "
            particle = particle + "\"data\" : \"" + data._data + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            print(result)
            return(result)
        elif (command[1] == 'vsftpd'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"username\" : \"" + data._username + "\", "
            particle = particle + "\"commandtype\" : \"" + data._commandtype + "\", "
            particle = particle + "\"sourceaddr\" : \"" + data._sourceaddr + "\", "
            particle = particle + "\"data\" : \"" + data._data + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'tcpd'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"system\" : \"" + data._system + "\", "
            particle = particle + "\"process\" : \"" + data._process + "\", "
            particle = particle + "\"connection\" : \"" + data._connection + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'cef'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"version\" : \"" + data._version + "\", "
            particle = particle + "\"deviceinfo\" : \"" + data._deviceinfo + "\", "
            particle = particle + "\"sourceip\" : \"" + data._sourceip + "\", "
            particle = particle + "\"signature\" : \"" + data._signature + "\", "
            particle = particle + "\"severity\" : \"" + data._severity + "\", "
            particle = particle + "\"exenstions\" : \"" + data._exenstions + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'nsca'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"client\" : \"" + data._client + "\", "
            particle = particle + "\"userid\" : \"" + data._userid + "\", "
            particle = particle + "\"user\" : \"" + data._user.replace("\\","\\\\") + "\", "
            particle = particle + "\"request\" : \"" + data._request + "\", "
            particle = particle + "\"statuscode\" : \"" + data._statuscode + "\", "
            particle = particle + "\"size\" : \"" + data._size + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'dns'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"requester\" : \"" + data._requester + "\", "
            particle = particle + "\"request\" : \"" + data._request + "\", "
            particle = particle + "\"requesttype\" : \"" + data._requesttype + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'netflow'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"duration\" : \"" + data._duration + "\", "
            particle = particle + "\"protocol\" : \"" + data._protocol + "\", "
            particle = particle + "\"sourceip\" : \"" + data._sourceip + "\", "
            particle = particle + "\"sourceport\" : \"" + data._sourceport + "\", "
            particle = particle + "\"destinationip\" : \"" + data._destinationip + "\", "
            particle = particle + "\"destport\" : \"" + data._destport + "\", "
            particle = particle + "\"packets\" : \"" + data._packets + "\", "
            particle = particle + "\"pbytes\" : \"" + data._pbytes + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'ftpd'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"transfertime\" : \"" + data._transfertime + "\", "
            particle = particle + "\"remotehost\" : \"" + data._remotehost + "\", "
            particle = particle + "\"filesize\" : \"" + data._filesize + "\", "
            particle = particle + "\"filename\" : \"" + data._filename.replace("\\","\\\\") + "\", "
            particle = particle + "\"transfertype\" : \"" + data._transfertype + "\", "
            particle = particle + "\"actionflag\" : \"" + data._actionflag + "\", "
            particle = particle + "\"direction\" : \"" + data._direction + "\", "
            particle = particle + "\"accessmode\" : \"" + data._accessmode + "\", "
            particle = particle + "\"username\" : \"" + data._username.replace("\\","\\\\") + "\", "
            particle = particle + "\"servicename\" : \"" + data._servicename + "\", "
            particle = particle + "\"authmethod\" : \"" + data._authmethod + "\", "
            particle = particle + "\"authuserid\" : \"" + data._authuserid + "\", "
            particle = particle + "\"status\" : \"" + data._status + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'evt'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            particle = particle + "\"source\" : \"" + data._source + "\", "
            particle = particle + "\"eventid\" : \"" + data._eventid + "\", "
            particle = particle + "\"evtdatetime\" : \"" + data._evtdatetime + "\", "
            particle = particle + "\"user\" : \"" + data._user.replace("\\","\\\\") + "\", "
            particle = particle + "\"computer\" : \"" + data._computer + "\", "
            particle = particle + "\"processid\" : \"" + data._processid + "\", "
            particle = particle + "\"threadid\" : \"" + data._threadid + "\", "
            particle = particle + "\"keywords\" : \"" + data._keywords + "\" "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'ip'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'tcp'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'udp'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'icmp'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        elif (command[1] == 'tcphttp'):
            particle = "{ \" " + str(data._ident) + "\" : "
            particle = particle + "{ \"identifier\" : \"" +  str(data._ident) + "\", "
            particle = particle + "\"datetime\" : \"" + data._datatime + "\", "
            particle = particle + "\"suptype\" : \"" + data._super_type + "\", "
            particle = particle + "\"suptype_id\" : \"" + data._super_id + "\", "
            particle = particle + "\"subtype\" : \"" + data._sub_type + "\", "
            particle = particle + "\"subtype_id\" : \"" + data._sub_id + "\", "
            #
            result = "{ \"retrunValue\" : \"True\", \"data\" : " + particle +" } } }"
            return(result)
        #except:
        #    result = "{ \"retrunValue\" : \"True\", \"data\" : \"\" } }"
    #
    #
    #
    elif (command[0] == 'list'):
        #
        # 
        #
        particles = "{" 
        #
        # 
        #
        if (command[1] == 'prediction'):
            if (len( database._cacheDB['prediction']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['prediction']:
                    particle = "\"" + str(database._cacheDB['prediction'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['prediction'][i]._ident) + "\", "
                    particle = particle + "\"name\" : \"" + database._cacheDB['prediction'][i]._name + "\", "
                    particle = particle + "\"type\" : \"" + database._cacheDB['prediction'][i]._type + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['prediction'][i]._datetime + "\", "
                    particle = particle + "\"references\" : \"" + str(database._cacheDB['prediction'][i]._references) + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'stix'):
            if (len( database._cacheDB['stix']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['stix']:
                    particle = "\"" + str(database._cacheDB['stix'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['stix'][i]._ident) + "\", "
                    particle = particle + "\"name\" : \"" + database._cacheDB['stix'][i]._name + "\" , "
                    particle = particle + "\"type\" : \"" + database._cacheDB['stix'][i]._type + "\", "
                    particle = particle + "\"cdatetime\" : \"" + database._cacheDB['stix'][i]._cdatetime + "\", "
                    particle = particle + "\"mdatetime\" : \"" + database._cacheDB['stix'][i]._cdatetime + "\", "
                    particle = particle + "\"description\" : \"" + database._cacheDB['stix'][i]._description + "\", "
                    particle = particle + "\"pattern\" : \"" + database._cacheDB['stix'][i]._pattern + "\", "
                    particle = particle + "\"killchainphase\" : \"" + str(database._cacheDB['stix'][i]._killchainphase) + "\", "
                    particle = particle + "\"lables\" : \"" + str(database._cacheDB['stix'][i]._lables) + "\", "
                    particle = particle + "\"externalrefs\" : \"" + str(database._cacheDB['stix'][i]._externalrefs) + "\", "
                    particle = particle + "\"relationship_type\" : \"" + database._cacheDB['stix'][i]._relationship_type + "\", "
                    particle = particle + "\"source_ref\" : \"" + str(database._cacheDB['stix'][i]._source_ref) + "\", "
                    particle = particle + "\"target_ref\" : \"" + str(database._cacheDB['stix'][i]._target_ref) + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'events'):
            if (len( database._cacheDB['event']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['event']:
                    particle = "\"" + str(database._cacheDB['event'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['event'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['event'][i]._datatime + "\", "
                    particle = particle + "\"subtype\" : \"" + database._cacheDB['event'][i]._sub_type + "\", "
                    particle = particle + "\"sub_id\" : \"" + database._cacheDB['event'][i].__sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['event'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        #
        #
        if (command[1] == 'syslog'):
            if (len( database._cacheDB['syslog']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['syslog']:
                    particle = "\"" + str(database._cacheDB['syslog'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['syslog'][i]._ident) + "\", "
                    particle = particle + "\"subtype\" : \"" + database._cacheDB['syslog'][i]._sub_type + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['syslog'][i]._datatime + "\", "
                    particle = particle + "\"system\" : \"" + database._cacheDB['syslog'][i]._system + "\", "
                    particle = particle + "\"suptype\" : \"" + database._cacheDB['syslog'][i]._super_type + "\", "
                    particle = particle + "\"suptype_id\" : \"" + database._cacheDB['syslog'][i]._super_id + "\", "
                    particle = particle + "\"subtype\" : \"" + database._cacheDB['syslog'][i]._sub_type + "\", "
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['syslog'][i]._sub_id + "\", "
                    particle = particle + "\"process_name\" : \"" + database._cacheDB['syslog'][i]._process_name + "\", "
                    particle = particle + "\"process_id\" : \"" + database._cacheDB['syslog'][i]._process_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['syslog'][i]._super_id  + "\", "
                    particle = particle + "\"sub_id\" : \"" + database._cacheDB['syslog'][i]._sub_id + "\", "
                    particle = particle + "\"data\" : \"" + database._cacheDB['syslog'][i]._data['message']['__text'] + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        #
        #
        if (command[1] == 'snort'):
            if (len( database._cacheDB['snort']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['snort']:
                    particle = "\"" + str(database._cacheDB['snort'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['snort'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['snort'][i]._datatime + "\", "
                    particle = particle + "\"system\" : \"" + database._cacheDB['snort'][i]._system + "\", "
                    particle = particle + "\"version\" : \"" + database._cacheDB['snort'][i]._version + "\", "
                    particle = particle + "\"classification\" : \"" + database._cacheDB['snort'][i]._classification + "\", "
                    particle = particle + "\"priority\" : \"" + database._cacheDB['snort'][i]._priority + "\", "
                    particle = particle + "\"protocol\" : \"" + database._cacheDB['snort'][i]._protocol + "\", "
                    particle = particle + "\"message\" : \"" + database._cacheDB['snort'][i]._message + "\", "
                    particle = particle + "\"dst\" : \"" + database._cacheDB['snort'][i]._dst + "\", "
                    particle = particle + "\"dstport\" : \"" + database._cacheDB['snort'][i]._dstport + "\", "
                    particle = particle + "\"src\" : \"" + database._cacheDB['snort'][i]._src + "\", "
                    particle = particle + "\"srcport\" : \"" + database._cacheDB['snort'][i]._srcport + "\", "
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['snort'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['snort'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        #
        #
        if (command[1] == 'sshd'):
            if (len( database._cacheDB['sshd']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['sshd']:
                    particle = "\"" + str(database._cacheDB['sshd'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['sshd'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['sshd'][i]._datatime + "\", "
                    particle = particle + "\"system\" : \"" + database._cacheDB['sshd'][i]._system + "\", "
                    particle = particle + "\"process\" : \"" + database._cacheDB['sshd'][i]._process + "\", "
                    particle = particle + "\"sourceaddr\" : \"" + database._cacheDB['sshd'][i]._sourceaddr + "\", "
                    particle = particle + "\"sourceport\" : \"" + database._cacheDB['sshd'][i]._sourceport + "\", "
                    particle = particle + "\"username\" : \"" + database._cacheDB['sshd'][i]._username + "\", "
                    particle = particle + "\"data\" : \"" + database._cacheDB['sshd'][i]._data + "\", "
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['sshd'][i]._sub_id + "\", "
                    #
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['sshd'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        #
        #
        if (command[1] == 'vsftpd'):
            if (len( database._cacheDB['vsftpd']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['vsftpd']:
                    particle = "\"" + str(database._cacheDB['vsftpd'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['vsftpd'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['vsftpd'][i]._datatime + "\", "
                    particle = particle + "\"username\" : \"" + database._cacheDB['vsftpd'][i]._username + "\", "
                    particle = particle + "\"commandtype\" : \"" + database._cacheDB['vsftpd'][i]._commandtype + "\", "
                    particle = particle + "\"sourceaddr\" : \"" + database._cacheDB['vsftpd'][i]._sourceaddr + "\", "
                    particle = particle + "\"data\" : \"" + database._cacheDB['vsftpd'][i]._data + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['vsftpd'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['vsftpd'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        #
        #
        if (command[1] == 'tcpd'):
            if (len( database._cacheDB['tcpd']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['tcpd']:
                    particle = "\"" + str(database._cacheDB['tcpd'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['tcpd'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['tcpd'][i]._datatime + "\", "
                    particle = particle + "\"system\" : \"" + database._cacheDB['tcpd'][i]._system + "\", "
                    particle = particle + "\"process\" : \"" + database._cacheDB['tcpd'][i]._process + "\", "
                    particle = particle + "\"connection\" : \"" + database._cacheDB['tcpd'][i]._connection + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['tcpd'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['tcpd'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        #
        #
        if (command[1] == 'cef'):
            if (len( database._cacheDB['cef']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['cef']:
                    particle = "\"" + str(database._cacheDB['cef'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['cef'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['cef'][i]._datatime + "\", "
                    particle = particle + "\"version\" : \"" + database._cacheDB['cef'][i]._version + "\", "
                    particle = particle + "\"deviceinfo\" : \"" + database._cacheDB['cef'][i]._deviceinfo + "\", "
                    particle = particle + "\"sourceip\" : \"" + database._cacheDB['cef'][i]._sourceip + "\", "
                    particle = particle + "\"signature\" : \"" + database._cacheDB['cef'][i]._signature + "\", "
                    particle = particle + "\"severity\" : \"" + database._cacheDB['cef'][i]._severity + "\", "
                    particle = particle + "\"exenstions\" : \"" + database._cacheDB['cef'][i]._exenstions + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['cef'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['cef'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        #
        #
        if (command[1] == 'nsca'):
            if (len( database._cacheDB['nsca']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['nsca']:
                    particle = "\"" + str(database._cacheDB['nsca'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['nsca'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['nsca'][i]._datatime + "\", "
                    particle = particle + "\"client\" : \"" + database._cacheDB['nsca'][i]._client + "\", "
                    particle = particle + "\"userid\" : \"" + database._cacheDB['nsca'][i]._userid + "\", "
                    particle = particle + "\"user\" : \"" + database._cacheDB['nsca'][i]._user.replace("\\","\\\\") + "\", "
                    particle = particle + "\"request\" : \"" + database._cacheDB['nsca'][i]._request + "\", "
                    particle = particle + "\"statuscode\" : \"" + database._cacheDB['nsca'][i]._statuscode + "\", "
                    particle = particle + "\"size\" : \"" + database._cacheDB['nsca'][i]._size + "\", "
                    # 
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['nsca'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['nsca'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # request
        #
        if (command[1] == 'dns'):
            if (len( database._cacheDB['dns']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['dns']:
                    particle = "\"" + str(database._cacheDB['dns'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['dns'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['dns'][i]._datatime + "\", "
                    particle = particle + "\"requester\" : \"" + database._cacheDB['dns'][i]._requester + "\", "
                    particle = particle + "\"request\" : \"" + database._cacheDB['dns'][i]._request + "\", "
                    particle = particle + "\"requesttype\" : \"" + database._cacheDB['dns'][i]._requesttype + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['dns'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['dns'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'ftpd'):
            if (len( database._cacheDB['ftpd']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['ftpd']:
                    particle = "\"" + str(database._cacheDB['ftpd'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['ftpd'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['ftpd'][i]._datatime + "\", "
                    particle = particle + "\"transfertime\" : \"" + database._cacheDB['ftpd'][i]._transfertime + "\", "
                    particle = particle + "\"remotehost\" : \"" + database._cacheDB['ftpd'][i]._remotehost + "\", "
                    particle = particle + "\"filesize\" : \"" + database._cacheDB['ftpd'][i]._filesize + "\", "
                    particle = particle + "\"filename\" : \"" + database._cacheDB['ftpd'][i]._filename.replace("\\","\\\\") + "\", "
                    particle = particle + "\"transfertype\" : \"" + database._cacheDB['ftpd'][i]._transfertype + "\", "
                    particle = particle + "\"actionflag\" : \"" + database._cacheDB['ftpd'][i]._actionflag + "\", "
                    particle = particle + "\"direction\" : \"" + database._cacheDB['ftpd'][i]._direction + "\", "
                    particle = particle + "\"accessmode\" : \"" + database._cacheDB['ftpd'][i]._accessmode + "\", "
                    particle = particle + "\"username\" : \"" + database._cacheDB['ftpd'][i]._username.replace("\\","\\\\") + "\", "
                    particle = particle + "\"servicename\" : \"" + database._cacheDB['ftpd'][i]._servicename + "\", "
                    particle = particle + "\"authmethod\" : \"" + database._cacheDB['ftpd'][i]._authmethod + "\", "
                    particle = particle + "\"authuserid\" : \"" + database._cacheDB['ftpd'][i]._authuserid + "\", "
                    particle = particle + "\"status\" : \"" + database._cacheDB['ftpd'][i]._status + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['ftpd'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['ftpd'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'netflow'):
            if (len( database._cacheDB['netflow']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['netflow']:
                    particle = "\"" + str(database._cacheDB['netflow'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['netflow'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['netflow'][i]._datatime + "\", "
                    particle = particle + "\"duration\" : \"" + database._cacheDB['netflow'][i]._duration + "\", "
                    particle = particle + "\"protocol\" : \"" + database._cacheDB['netflow'][i]._protocol + "\", "
                    particle = particle + "\"sourceip\" : \"" + database._cacheDB['netflow'][i]._sourceip + "\", "
                    particle = particle + "\"sourceport\" : \"" + database._cacheDB['netflow'][i]._sourceport + "\", "
                    particle = particle + "\"destinationip\" : \"" + database._cacheDB['netflow'][i]._destinationip + "\", "
                    particle = particle + "\"destport\" : \"" + database._cacheDB['netflow'][i]._destport + "\", "
                    particle = particle + "\"packets\" : \"" + database._cacheDB['netflow'][i]._packets + "\", "
                    particle = particle + "\"pbytes\" : \"" + database._cacheDB['netflow'][i]._pbytes + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['netflow'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['netflow'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'evt'):
            if (len( database._cacheDB['evt']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['evt']:
                    particle = "\"" + str(database._cacheDB['evt'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['evt'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['evt'][i]._datatime + "\", "
                    particle = particle + "\"source\" : \"" + database._cacheDB['evt'][i]._source + "\", "
                    particle = particle + "\"eventid\" : \"" + database._cacheDB['evt'][i]._eventid + "\", "
                    particle = particle + "\"evtdatetime\" : \"" + database._cacheDB['evt'][i]._evtdatetime + "\", "
                    particle = particle + "\"user\" : \"" + database._cacheDB['evt'][i]._user.replace("\\","\\\\") + "\", "
                    particle = particle + "\"computer\" : \"" + database._cacheDB['evt'][i]._computer + "\", "
                    particle = particle + "\"processid\" : \"" + database._cacheDB['evt'][i]._processid + "\", "
                    particle = particle + "\"threadid\" : \"" + database._cacheDB['evt'][i]._threadid + "\", "
                    particle = particle + "\"keywords\" : \"" + database._cacheDB['evt'][i]._keywords + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['evt'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['evt'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'ipv4'):
            if (len( database._cacheDB['ipv4']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['ipv4']:
                    particle = "\"" + str(database._cacheDB['ipv4'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['ipv4'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['ipv4'][i]._datatime + "\", "
                    particle = particle + "\"version\" : \"" + database._cacheDB['ipv4'][i]._version + "\", "
                    particle = particle + "\"ihl\" : \"" + database._cacheDB['ipv4'][i]._ihl + "\", "
                    particle = particle + "\"tos\" : \"" + database._cacheDB['ipv4'][i]._tos + "\", "
                    particle = particle + "\"tlen\" : \"" + database._cacheDB['ipv4'][i]._tlen + "\", "
                    particle = particle + "\"packident\" : \"" + database._cacheDB['ipv4'][i]._packident + "\", "
                    particle = particle + "\"fragoff\" : \"" + database._cacheDB['ipv4'][i]._fragoff + "\", "
                    particle = particle + "\"ttl\" : \"" + database._cacheDB['ipv4'][i]._ttl + "\", "
                    particle = particle + "\"protocol\" : \"" + database._cacheDB['ipv4'][i]._protocol + "\", "
                    particle = particle + "\"hcs\" : \"" + database._cacheDB['ipv4'][i]._hcs + "\", "
                    particle = particle + "\"sourceip\" : \"" + database._cacheDB['ipv4'][i]._sourceip + "\", "
                    particle = particle + "\"destinationip\" : \"" + database._cacheDB['ipv4'][i]._destinationip + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['ipv4'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['ipv4'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'tcp'):
            if (len( database._cacheDB['tcp']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['tcp']:
                    particle = "\"" + str(database._cacheDB['tcp'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['tcp'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['tcp'][i]._datatime + "\", "
                    particle = particle + "\"sourport\" : \"" + database._cacheDB['tcp'][i]._sourport + "\", "
                    particle = particle + "\"destport\" : \"" + database._cacheDB['tcp'][i]._destport + "\", "
                    particle = particle + "\"sequnum\" : \"" + database._cacheDB['tcp'][i]._sequnum + "\", "
                    particle = particle + "\"acknum\" : \"" + database._cacheDB['tcp'][i]._acknum + "\", "
                    particle = particle + "\"winsize\" : \"" + database._cacheDB['tcp'][i]._winsize + "\", "
                    particle = particle + "\"checksum\" : \"" + database._cacheDB['tcp'][i]._checksum + "\", "
                    particle = particle + "\"urgptr\" : \"" + database._cacheDB['tcp'][i]._urgptr + "\", "
                    particle = particle + "\"dataoffset\" : \"" + database._cacheDB['tcp'][i]._dataoffset + "\", "
                    particle = particle + "\"ackflag\" : \"" + database._cacheDB['tcp'][i]._ackflag + "\", "
                    particle = particle + "\"cwrflag\" : \"" + database._cacheDB['tcp'][i]._cwrflag + "\", "
                    particle = particle + "\"synflag\" : \"" + database._cacheDB['tcp'][i]._synflag + "\", "
                    particle = particle + "\"pushflag\" : \"" + database._cacheDB['tcp'][i]._pushflag + "\", "
                    particle = particle + "\"ecnflag\" : \"" + database._cacheDB['tcp'][i]._ecnflag + "\", "
                    particle = particle + "\"finflag\" : \"" + database._cacheDB['tcp'][i]._finflag + "\", "
                    particle = particle + "\"rstflag\" : \"" + database._cacheDB['tcp'][i]._rstflag + "\", "
                    particle = particle + "\"urgflag\" : \"" + database._cacheDB['tcp'][i]._urgflag + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['tcp'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['tcp'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'udp'):
            if (len( database._cacheDB['udp']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['udp']:
                    particle = "\"" + str(database._cacheDB['udp'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['udp'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['udp'][i]._datatime + "\", "
                    particle = particle + "\"checksum\" : \"" + database._cacheDB['udp'][i]._checksum + "\", "
                    particle = particle + "\"length\" : \"" + database._cacheDB['udp'][i]._length + "\", "
                    particle = particle + "\"sourport\" : \"" + database._cacheDB['udp'][i]._sourport + "\", "
                    particle = particle + "\"destport\" : \"" + database._cacheDB['udp'][i]._destport + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['udp'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['udp'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'icmp'):
            if (len( database._cacheDB['icmp']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['icmp']:
                    particle = "\"" + str(database._cacheDB['icmp'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['icmp'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['icmp'][i]._datatime + "\", "
                    particle = particle + "\"type\" : \"" + database._cacheDB['icmp'][i]._type + "\", "
                    particle = particle + "\"code\" : \"" + database._cacheDB['icmp'][i]._code + "\", "
                    particle = particle + "\"checksum\" : \"" + database._cacheDB['icmp'][i]._checksum + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['icmp'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['icmp'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
        #
        # 
        #
        if (command[1] == 'tcphttp'):
            if (len( database._cacheDB['tcphttp']) == 0):
                result = "{ \"retrunValue\" : \"True\", \"data\" : \"NONE\" }"
            else:
                for i in database._cacheDB['tcphttp']:
                    particle = "\"" + str(database._cacheDB['tcphttp'][i]._ident) + "\" : "
                    particle = particle + "{ \"identifier\" : \"" +  str(database._cacheDB['tcphttp'][i]._ident) + "\", "
                    particle = particle + "\"datetime\" : \"" + database._cacheDB['tcphttp'][i]._datatime + "\", "
                    particle = particle + "\"method\" : \"" + database._cacheDB['tcphttp'][i]._method  + "\", "
                    particle = particle + "\"useragent\" : \"" + database._cacheDB['tcphttp'][i]._useragent  + "\", "
                    particle = particle + "\"cookie\" : \"" + database._cacheDB['tcphttp'][i]._cookie  + "\", "
                    particle = particle + "\"fullurl\" : \"" + database._cacheDB['tcphttp'][i]._fullurl  + "\", "
                    #
                    particle = particle + "\"subtype_id\" : \"" + database._cacheDB['tcphttp'][i]._sub_id + "\", "
                    particle = particle + "\"super_id\" : \"" + database._cacheDB['tcphttp'][i]._super_id  + "\"}, "
                    particles = particles + particle
                particles = particles[0:(len(particles)-2)]
                result = "{ \"retrunValue\" : \"True\", \"data\" : " + particles +" } }"
    #
    #
    #
    return result
#
#  
# 
#
