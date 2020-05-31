all:
	cls ; python ale.py ./utfunctions 

ale:
	cls ; python ale.py ./utfunctions

clean:
	cls ; rm -rf core *.pyc *.bak

demo:
	make clean
	cls
	(cd ../datajsonrpc ; make)
	(cd ../threatintelligenceengine ; make tie)
	cls ; python ale.py ./utfunctions

