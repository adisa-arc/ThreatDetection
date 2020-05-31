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
#include "/usr/local/include/pcap/DnsLayer.h"
#include "/usr/local/include/pcap/IcmpLayer.h"
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
 * A struct for collecting packet statistics
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
            if(strcmp(getProtocolTypeAsString(curLayer->getProtocol()).c_str(), "UDP") == 0)
            {
                pcpp::DnsLayer* newDnsLayer = packet.getLayerOfType<pcpp::DnsLayer>();
	            if (newDnsLayer != NULL)
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
                    cout << "\"_type\" : \"udp\", ";
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
                    // Get the UDP Packet layer and decode it.
                    pcpp::UdpLayer* udpLayer = packet.getLayerOfType<pcpp::UdpLayer>();
                    cout << "\"udp\": { \"_datetime\" : \" ";
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
                    cout << "\"_type\" : \"udp\", ";
                    //
                    int hcm = udpLayer->getUdpHeader()->headerChecksum;
                    int len = udpLayer->getUdpHeader()->length;
                    int spt = udpLayer->getUdpHeader()->portSrc;
                    int dpt = udpLayer->getUdpHeader()->portDst;
                    cout << "\"checksum\" : \"" << hcm << "\", ";
                    cout << "\"length\" : \"" << len << "\", ";
                    cout << "\"sourport\" : \"" << spt << "\", ";
                    cout << "\"destport\" : \"" << dpt << "\", ";
                    cout << "\"dns\": { \"_datetime\" : \" ";
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
                    cout << "\"_type\" : \"dns\", ";
                    cout << "\"identification\" : \""<< newDnsLayer->getDnsHeader()->transactionID << "\", ";
                    cout << "\"queryname\" : \""<< newDnsLayer->getFirstQuery()->getName() << "\" ";
                    //
                    //
                    cout << "} } } } }" << endl;
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