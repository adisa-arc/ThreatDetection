/*
 *
 * 
 * 
 * 
 */
#include "/usr/local/include/pcap/IPv4Layer.h"
#include "/usr/local/include/pcap/Packet.h"
#include "/usr/local/include/pcap/PcapFileDevice.h"
#include "/usr/local/include/pcap/EthLayer.h"
#include "/usr/local/include/pcap/IPv4Layer.h"
#include "/usr/local/include/pcap/TcpLayer.h"
#include "/usr/local/include/pcap/UdpLayer.h"
#include "/usr/local/include/pcap/IcmpLayer.h"
#include "/usr/local/include/pcap/HttpLayer.h"
#include "/usr/local/include/pcap/PcapLiveDeviceList.h"
#include "/usr/local/include/pcap/PlatformSpecificUtils.h"
/**
 *
 */
#include <stdlib.h>
#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;
/**
 *
 * 
 * 
 */
std::string getProtocolTypeAsString(pcpp::ProtocolType protocolType)
{
	switch (protocolType)
	{
	case pcpp::Ethernet:
		return "Ethernet";
	case pcpp::IPv4:
		return "IPv4";
	case pcpp::TCP:
		return "TCP";
    case pcpp::UDP:
        return "UDP";
    case pcpp::ICMP:
        return "ICMP";
	default:
		return "Unknown";
	}
}
/**
 * 
 * 
 * 
 */
std::string printHttpMethod(pcpp::HttpRequestLayer::HttpMethod httpMethod)
{
	switch (httpMethod)
	{
	case pcpp::HttpRequestLayer::HttpGET:
		return "GET";
	case pcpp::HttpRequestLayer::HttpPOST:
		return "POST";
	default:
		return "Other";
	}
}
/**
 * 
 * 
 * 
 */
struct PacketStats
{
	/**
	* Collect stats from a packet
	*/
	void consumePacket(pcpp::Packet& packet)
	{        
        // pcpp::Layer* packetLayer = packet.getFirstLayer();
        
        for (pcpp::Layer* curLayer = packet.getFirstLayer(); curLayer != NULL; curLayer = curLayer->getNextLayer())
        {
            if(strcmp(getProtocolTypeAsString(curLayer->getProtocol()).c_str(), "HTTP") == 0)
            {
                // 
                time_t now = time(0);
                tm *ltm = localtime(&now);
                cout << "{ \"event\" : { \"_datetime\" : \"";
                // 
                if ((1 + ltm->tm_mon) == 1) { cout <<  "Jan"; }
                if ((1 + ltm->tm_mon) == 2) { cout <<  "Feb"; }
                if ((1 + ltm->tm_mon) == 3) { cout <<  "Mar"; }
                if ((1 + ltm->tm_mon) == 4) { cout <<  "Apr"; }
                if ((1 + ltm->tm_mon) == 5) { cout <<  "May"; }
                if ((1 + ltm->tm_mon) == 6) { cout <<  "Jun"; }
                if ((1 + ltm->tm_mon) == 7) { cout <<  "Jul"; }
                if ((1 + ltm->tm_mon) == 8) { cout <<  "Aug"; }
                if ((1 + ltm->tm_mon) == 9) { cout <<  "Sep"; }
                if ((1 + ltm->tm_mon) == 10) { cout <<  "Oct"; }
                if ((1 + ltm->tm_mon) == 11) { cout <<  "Nov"; }
                if ((1 + ltm->tm_mon) == 12) { cout <<  "Dec"; }
                //
                cout << " " << ltm->tm_mday << " " << ltm->tm_hour << ":" << ltm->tm_min << ":" << ltm->tm_sec << "\", ";
                cout << "\"_ident\" : \"" << rand() << now << "\", ";
                cout << "\"_type\" : \"ipv4\", \"ipv4\": { \"_datetime\" : \" ";
                //
                cout << " " << ltm->tm_mday << " " << ltm->tm_hour << ":" << ltm->tm_min << ":" << ltm->tm_sec << "\", ";
                cout << "\"_ident\" : \"" << rand() << now << "\", ";
                cout << "\"_type\" : \"tcp\", ";
                //
                pcpp::IPv4Layer* ipLayer = packet.getLayerOfType<pcpp::IPv4Layer>();
                int ipv = ipLayer->getIPv4Header()->ipVersion;
                int ihl = ipLayer->getIPv4Header()->internetHeaderLength;
                int tos = ipLayer->getIPv4Header()->typeOfService;
                int tln = ipLayer->getIPv4Header()->totalLength;
                int pid = ipLayer->getIPv4Header()->ipId;
                int fos = ipLayer->getIPv4Header()->fragmentOffset;
                int ttl = ipLayer->getIPv4Header()->timeToLive;
                int pcl = ipLayer->getIPv4Header()->protocol;
                int hcs = ipLayer->getIPv4Header()->headerChecksum;
                cout << "\"version\" : \"" << ipv << "\", ";
                cout << "\"ihl\" : \"" << ihl << "\", ";
                cout << "\"tos\" : \"" << tos << "\", ";
                cout << "\"tlen\" : \"" << tln << "\", ";
                cout << "\"ident\" : \"" << pid << "\", ";
                cout << "\"fragoff\" : \"" << fos << "\", ";
                cout << "\"ttl\" : \"" << ttl << "\", ";
                cout << "\"protocol\" : \"" << pcl << "\", ";
                cout << "\"hcs\" : \"" << hcs << "\", ";
                cout << "\"sourceip\" : \"" << ipLayer->getSrcIpAddress().toString().c_str() << "\", ";
                cout << "\"destinationip\" : \"" << ipLayer->getDstIpAddress().toString().c_str() << "\", ";
                //
                // pcpp::IcmpLayer* icmpLayer = packet.getLayerOfType<pcpp::IcmpLayer>();
                pcpp::TcpLayer* tcpLayer = packet.getLayerOfType<pcpp::TcpLayer>();
                cout << "\"tcp\": { \"_datetime\" : \" ";
                // 
                if ((1 + ltm->tm_mon) == 1) { cout <<  "Jan"; }
                if ((1 + ltm->tm_mon) == 2) { cout <<  "Feb"; }
                if ((1 + ltm->tm_mon) == 3) { cout <<  "Mar"; }
                if ((1 + ltm->tm_mon) == 4) { cout <<  "Apr"; }
                if ((1 + ltm->tm_mon) == 5) { cout <<  "May"; }
                if ((1 + ltm->tm_mon) == 6) { cout <<  "Jun"; }
                if ((1 + ltm->tm_mon) == 7) { cout <<  "Jul"; }
                if ((1 + ltm->tm_mon) == 8) { cout <<  "Aug"; }
                if ((1 + ltm->tm_mon) == 9) { cout <<  "Sep"; }
                if ((1 + ltm->tm_mon) == 10) { cout <<  "Oct"; }
                if ((1 + ltm->tm_mon) == 11) { cout <<  "Nov"; }
                if ((1 + ltm->tm_mon) == 12) { cout <<  "Dec"; }
                //
                cout << " " << ltm->tm_mday << " " << ltm->tm_hour << ":" << ltm->tm_min << ":" << ltm->tm_sec << "\", ";
                cout << "\"_ident\" : \"" << rand() << now << "\", ";
                cout << "\"_type\" : \"http\", ";
                int spt = tcpLayer->getTcpHeader()->portSrc;
                int dpt = tcpLayer->getTcpHeader()->portDst;
                signed long int snm = tcpLayer->getTcpHeader()->sequenceNumber;
                signed long int anm = tcpLayer->getTcpHeader()->ackNumber;
                int win = tcpLayer->getTcpHeader()->windowSize;
                int csm = tcpLayer->getTcpHeader()->headerChecksum;
                int dff = tcpLayer->getTcpHeader()->dataOffset;
                int urp = tcpLayer->getTcpHeader()->urgentPointer; 
                int afg = tcpLayer->getTcpHeader()->ackFlag;        // The ACK Flag  - The Acknowledgement Flag.
                int cwg = tcpLayer->getTcpHeader()->cwrFlag;        // The CWR Flag  - Congestion Window Reduced (CWR) flag.
                int ecg = tcpLayer->getTcpHeader()->eceFlag;        // The ECN Flag  - ECN-Echo has a dual role.
                int fng = tcpLayer->getTcpHeader()->finFlag;        // The FIN Flag  - The Terminal a connection Flag
                int psg = tcpLayer->getTcpHeader()->pshFlag;        // The PUSH Flag - This is the PUSH data Flag
                int rtg = tcpLayer->getTcpHeader()->rstFlag;        // The RST Flag  - This is the Rest Glag.
                int syg = tcpLayer->getTcpHeader()->synFlag;        // The SYN Flag  - The Synchronisation Flag.
                int urg = tcpLayer->getTcpHeader()->urgFlag;        // The URG Flag  - This is the URGENT Flag.
                //
                cout << "\"sourport\" : \"" << spt << "\", ";
                cout << "\"destport\" : \"" << dpt << "\", ";
                cout << "\"sequnum\" : \"" << snm  << "\", ";
                cout << "\"acknum\" : \"" << anm << "\", ";
                cout << "\"winsize\" : \"" << win << "\", ";
                cout << "\"checksum\" : \"" << csm << "\", ";
                cout << "\"urgptr\" : \"" << urp << "\", ";
                cout << "\"dataoffset\" : \"" << dff << "\", ";
                cout << "\"ackflag\" : \"" << afg << "\", ";
                cout << "\"cwrflag\" : \"" << cwg << "\", ";
                cout << "\"synflag\" : \"" << syg << "\", ";
                cout << "\"pushflag\" : \"" << psg << "\", ";
                cout << "\"ecnflag\" : \"" << ecg << "\", ";
                cout << "\"finflag\" : \"" << fng << "\", ";
                cout << "\"rstflag\" : \"" << rtg << "\", ";
                cout << "\"urgflag\" : \"" << urg << "\", ";
                cout << "\"http\": { \"_datetime\" : \" ";
                // 
                if ((1 + ltm->tm_mon) == 1) { cout <<  "Jan"; }
                if ((1 + ltm->tm_mon) == 2) { cout <<  "Feb"; }
                if ((1 + ltm->tm_mon) == 3) { cout <<  "Mar"; }
                if ((1 + ltm->tm_mon) == 4) { cout <<  "Apr"; }
                if ((1 + ltm->tm_mon) == 5) { cout <<  "May"; }
                if ((1 + ltm->tm_mon) == 6) { cout <<  "Jun"; }
                if ((1 + ltm->tm_mon) == 7) { cout <<  "Jul"; }
                if ((1 + ltm->tm_mon) == 8) { cout <<  "Aug"; }
                if ((1 + ltm->tm_mon) == 9) { cout <<  "Sep"; }
                if ((1 + ltm->tm_mon) == 10) { cout <<  "Oct"; }
                if ((1 + ltm->tm_mon) == 11) { cout <<  "Nov"; }
                if ((1 + ltm->tm_mon) == 12) { cout <<  "Dec"; }
                //
                cout << " " << ltm->tm_mday << " " << ltm->tm_hour << ":" << ltm->tm_min << ":" << ltm->tm_sec << "\", ";
                cout << "\"_ident\" : \"" << rand() << now << "\", ";
                pcpp::HttpRequestLayer* httpRequestLayer = packet.getLayerOfType<pcpp::HttpRequestLayer>();
	            if (httpRequestLayer == NULL)
	            {
                    cout << "\"_type\" : \"http\" ";
		            cout << "} } } } }" << endl << endl;
		            exit(1);
	            } else
                {
                    cout << "\"_type\" : \"http\", ";
                    cout << "\"method\" : \"" << printHttpMethod(httpRequestLayer->getFirstLine()->getMethod()).c_str() << "\", ";
                    cout << "\"usergaent\" : \"" << httpRequestLayer->getFieldByName(PCPP_HTTP_USER_AGENT_FIELD)->getFieldValue().c_str() << "\", ";
                    cout << "\"cookie\" : \"" << httpRequestLayer->getFieldByName(PCPP_HTTP_COOKIE_FIELD)->getFieldValue().c_str() << "\", ";
                    cout << "\"fullurl\" : \"" << httpRequestLayer->getUrl().c_str() << "\" ";
                    cout << "} } } } }" << endl << endl;
                }
            }
        }
	}
};
/**
 * 
 * A callback function for the async capture which is called each time a packet is captured
 *
 */
static void onPacketArrives(pcpp::RawPacket* packet, pcpp::PcapLiveDevice* dev, void* cookie)
{
	// extract the stats object form the cookie
	PacketStats* stats = (PacketStats*)cookie;
	// parsed the raw packet
	pcpp::Packet parsedPacket(packet);
	// collect stats from packet
	stats->consumePacket(parsedPacket);
}
/**
 *
 */
int main(int argc, char* argv[])
{
    // IPv4 address of the interface we want to sniff
    std::string interfaceIPAddr = "192.168.1.100";

    // find the interface by IP address
    pcpp::PcapLiveDevice* dev = pcpp::PcapLiveDeviceList::getInstance().getPcapLiveDeviceByIp(interfaceIPAddr.c_str());
    if (dev == NULL)
    {
	    printf("Cannot find interface with IPv4 address of '%s'\n", interfaceIPAddr.c_str());
	    exit(1);
    }
    if (!dev->open())
    {
	    printf("Cannot open device\n");
	    exit(1);
    }
    // create the stats object
    PacketStats stats;
    // create an empty packet vector object
    pcpp::RawPacketVector packetVec;
    // start capturing packets. All packets will be added to the packet vector
    dev->startCapture(onPacketArrives, &stats);
    // sleep for 10 seconds in main thread, in the meantime packets are captured in the async thread
    while (true) {};
    // stop capturing packets
    dev->stopCapture();
    return 0;
}
/*
 *
 */