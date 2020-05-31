all:
	cls ; python tie.py

tie:	
	cls ; python tie.py stix.json

stix:
	cls ; python stix.py

json:
	rm -rf *.json
	cls
	python stix.py > stix.json

clean:
	cls ; rm -rf core *.pyc *.bak *.json __pycache__
