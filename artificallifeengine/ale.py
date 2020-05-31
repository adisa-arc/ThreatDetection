#
# This the Artifical Life Engine  Definition
#           Date:   1st June 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
#
#
import sys
import os
from artificallifeengine import ArtificalLifeEngine
#
#
#
#
#
def help():
    print('Artifical Life Engine [ale] - Version 1.0 - andrew.blyth@adisa.global\n')
    print('USAGE: ale /path/directory\n') 
    print('Examples of Usage:\n')
    print('        ale ../ale/XML        - This will read and process all utility functions ')
    print('                                in the directory ../ale/XML\n')
#
#
#
def main(): 
    #
    if (len(sys.argv) == 2):
        exists = os.path.exists(sys.argv[1])
        directoryName = sys.argv[1]
    else:
        print('Artifical Life Engine [ale] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Insufficent command line arguments.\n\n")
        help()
        sys.exit()
    #   
    if not exists:
        print('Artifical Life Engine [ale] - Version 1.0 - andrew.blyth@adisa.global\n')
        print(":- ERROR: Directory '" + directoryName + "' not found or unaccessable.\n")
        help()
        sys.exit()
    #
    try:
        ALE = ArtificalLifeEngine(directoryName)
        ALE.run()
    #
    except Exception as e:
        print("Exception Error in processing Artifical Life Engine:- " + e)
    #
    return True
#
#
#
if __name__ == "__main__":
    main()
#
#
#    