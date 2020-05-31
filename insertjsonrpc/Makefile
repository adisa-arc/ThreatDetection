all:
	cls
	@echo ''
	@echo '|==> The Options are as follows so please use one:'
	@echo '     $ make ip           - This makes and inserts the IP data'
	@echo '     $ make tcp          - This makes and inserts the TCP data'
	@echo '     $ make udp          - This makes and inserts the UDP data'
	@echo '     $ make icmp         - This makes and inserts the ICMP data'
	@echo '     $ make http         - This makes and inserts the TCP/IP HTTP data'
	@echo ''

ip: 
	cls ; cat ../data/ip.dat |  python insertjsonsrc.py 

tcp:
	cls ; cat ../data/tcp.dat | python insertjsonsrc.py

udp:
	cls ; cat ../data/udp.dat | python insertjsonsrc.py

icmp:
	cls ; cat ../data/icmp.dat | python insertjsonsrc.py

http:
	cls ; cat ../data/tcphttp.dat | python insertjsonsrc.py
