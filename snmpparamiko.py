#snmp_python_interfacestats.py
import paramiko
from pysnmp.entity.rfc3413.oneliner import cmdgen
cmdGen = cmdgen.CommandGenerator()

for n in range(1, 3):
    server_ip = "10.65.205.31"
    print("\nFetching stats for...", server_ip)
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd( cmdgen.CommunityData('public'), cmdgen.UdpTransportTarget((server_ip, 161)),0,25,'1.3.6.1.2.1.2.2.1.2')

for varBindTableRow in varBindTable:
    for name, val in varBindTableRow:
        print('%s = Interface Name: %s' % (name.prettyPrint(), val.prettyPrint()))