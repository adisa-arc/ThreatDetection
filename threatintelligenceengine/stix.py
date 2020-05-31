#
# This is the Python Script that create a STIX.JSON description of a cyber attack.
# To achieve this it makes use of the stix2 python module. This allows is to define
# a set of objects and a set of relationships.
#
#   Author:     Dr Andrew Blyth, PhD <andrew.blyth@adisa.global>
#   Date:       1st June 2019
#   Version:    1.0
#
#
#
import stix2
#
#
# This is the CAPEC-448: Embed Virus into DLL
er00 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-448"
)
# This is the CVE for an Exploit
er01 = stix2.ExternalReference(
    source_name="CVE",
    external_id="CVE-2019-9182"
)
# This is the CAPEC for TCP Connect Scan / PortScanning
er02 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-301"
)
# This is the CAPEC for Service Footprinting
er03 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-574"
)
# This is the CAPEC for Active OS Fingerprinting
er04 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-312"
)
# This is the CAPEC for EXploit API Validation
er05 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-121"
)
# This is the CAPEC for Code Injection  
er06 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-242"
)
# ACPEC-187: Malicious Automated Software Update
er07 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-187"
)
# APEC-168: DNS Query
er08 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-168"
)
# APEC-169: DNS Query
er09 = stix2.ExternalReference(
    source_name="CAPEC",
    external_id="CAPEC-169"
)
#
foothold1 = stix2.KillChainPhase(
    kill_chain_name="cyber-attack-lifecycle-model",
    phase_name="Reconnaissance"
)
#
foothold2 = stix2.KillChainPhase(
    kill_chain_name="cyber-attack-lifecycle-model",
    phase_name="Weaponization"
)
#
foothold3 = stix2.KillChainPhase(
    kill_chain_name="cyber-attack-lifecycle-model",
    phase_name="Delivery"
)
#
foothold4 = stix2.KillChainPhase(
    kill_chain_name="cyber-attack-lifecycle-model",
    phase_name="Exploitation"
)
#
foothold5 = stix2.KillChainPhase(
    kill_chain_name="cyber-attack-lifecycle-model",
    phase_name="Installation"
)
#
foothold6 = stix2.KillChainPhase(
    kill_chain_name="cyber-attack-lifecycle-model",
    phase_name="Command and Control"
)
#
vulnerabilit01 = stix2.Vulnerability(
    name ="Poision Ivy Vulnerability ",
    description = "This is the Poision Ivy RAT infection vulnerability used by CTT1.",
    external_references=[er00,er01],
)
#
intrusionset01 = stix2.IntrusionSet(
    name ="Cowbridge Team Threat Actor Group - CTT1",
    description = "This organized threat actor group operates to perform data harvesting.",
)
#
threat_actor1 = stix2.ThreatActor(
    name="Cowbridge Team Threat Actor Group - CTT1",
    description="This organized threat actor group operates to perform data harvesting.",
    labels=["crime-syndicate"],
    aliases=["Cowbridge Red Team"],
    roles=["agent"],
    goals=["Steal Intellectual Property"],
    sophistication="expert",
    resource_level="organization",
    primary_motivation="personal-gain"
)
#
indicator1 = stix2.Indicator(
    name="Update Software Server for RAT",
    description="This is the RAT making an software update request",
    labels=["malicious-activity"],
    pattern="[url:value = '']",
    external_references=[er07],
    kill_chain_phases=[foothold5]
)
#
indicator2 = stix2.Indicator(
    name="Port Scanning & Banner Grabbing",
    description="This is use of the NMAP tool to perform TCP port scanning and banner grabbing.",
    labels=["reconnaissance"],
    pattern="[url:value = '']",
    external_references=[er02],
    kill_chain_phases=[foothold1]
)
#
indicator3 = stix2.Indicator(
    name="Banner Grabbing & OS Fingerpriniting",
    description="This is indicator for the identification of Service and and Operating System.",
    labels=["reconnaissance"],
    pattern="[url:value = '']",
    external_references=[er03,er04],
    kill_chain_phases=[foothold2]
)
#
indicator4 = stix2.Indicator(
    name="Vul ID and Exploit",
    description="This is indicator for the identification of a vulnerability.",
    labels=["Exploitation"],
    pattern="[url:value = '']",
    external_references=[er05, er06],
    kill_chain_phases=[foothold3, foothold4]
)
#
indicator5 = stix2.Indicator(
    name="DNS Activity - av.ddns.us",
    description="This Indicator is connected to av.ddns.us with the password of admin.",
    labels=["Exploitation"],
    pattern="[domain-name:value = 'av.ddns.us' OR ipv4-addr:value = '60.2.148.167']",
    external_references=[er09],
    kill_chain_phases=[foothold6]
)
#
indicator6 = stix2.Indicator(
    name="SSHD Activity from send.have8000.com",
    description="This indicator is connected to send.have8000.com with the password of suzuki. The domain have8000.com was with the email zhengyanbin8@ gmail.com",
    labels=["Exploitation"],
    pattern="[domain-name:value = 'send.have8000.com']",
    external_references=[er08],
    kill_chain_phases=[foothold6]
)
#
malware1 = stix2.Malware(
    name="Pison Ivy Version 15..12.01",
    labels=["backdoor", "remote-access-trojan"],
    description="This malware is s Remote Access Trojan",
    kill_chain_phases=[foothold2],
)
#
attackpattern01 = stix2.AttackPattern(
    name="Cowbridge Team Threat Actor Group - CTT1",
    description="This organized threat actor group operates to perform data harvesting.",
    kill_chain_phases=[foothold3, foothold4, foothold5]
)
#
tools01 = stix2.Tool(
    name="NMAP Port Scanning & Banner Enumeration",
    description="This is the use of the NMAP too to perform port scanning and banner enumeration",
    tool_version="1.0", 
    labels=["port-scanning"],
    kill_chain_phases=[foothold1]
)
#
tools02 = stix2.Tool(
    name="Identf of Vulnerability",
    description="This is the identfiication of a vulnerability.",
    tool_version="1.0", 
    labels=["vulnerability identification"],
    kill_chain_phases=[foothold2]
)
#
tools03 = stix2.Tool(
    name="Vul Validation",
    description="This is the validation of a vulnerability.",
    tool_version="1.0", 
    labels=["vulnerability validation"],
    kill_chain_phases=[foothold3]
)

#
#
#
if __name__ == '__main__':
    #
    relationship01 = stix2.Relationship(threat_actor1, 'uses', malware1)
    relationship02 = stix2.Relationship(indicator1, 'indicates', malware1)
    relationship03 = stix2.Relationship(malware1, 'targets', vulnerabilit01)
    relationship04 = stix2.Relationship(threat_actor1, 'uses', attackpattern01)
    relationship05 = stix2.Relationship(intrusionset01, 'attributedto', threat_actor1)
    relationship06 = stix2.Relationship(intrusionset01, 'attributedto', attackpattern01)
    relationship07 = stix2.Relationship(indicator2, 'indicates', tools01)
    relationship08 = stix2.Relationship(indicator3, 'indicates', tools02)
    relationship09 = stix2.Relationship(attackpattern01, 'uses', tools01)
    relationship10 = stix2.Relationship(attackpattern01, 'uses', tools02)
    relationship11 = stix2.Relationship(attackpattern01, 'uses', tools03)
    relationship12 = stix2.Relationship(indicator4, 'indicates', tools03)
    relationship13 = stix2.Relationship(indicator5, 'indicates', malware1)
    relationship14 = stix2.Relationship(indicator6, 'indicates', malware1)
    relationship15 = stix2.Relationship(attackpattern01, 'uses', malware1)
    #
    bundle = stix2.Bundle(objects=[indicator1, malware1, threat_actor1, vulnerabilit01,
        attackpattern01, intrusionset01, tools01, tools02, tools03, indicator2,  indicator3, indicator4,
        indicator5, indicator6, relationship11, relationship12, relationship13, relationship14,
        relationship01, relationship02, relationship03, relationship04, relationship05, relationship15,
        relationship06, relationship07, relationship08, relationship09, relationship10])
    #
    print(bundle)
#
#
# 