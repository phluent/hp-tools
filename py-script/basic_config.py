import datetime
now = datetime.datetime.now()
mytimedate = now.strftime("%H:%M:%S %m/%d/%Y")

GPublicSNMP = raw_input('Enter Public SNMP String: ')
GPrivateSNMP = raw_input('Enter Private SNMP String: ')
GsshUserName = raw_input('Enter admin username: ')
GsshPassword = raw_input('Enter admin Password: ')

print 'A-Series config: '
print 'snmp-agent sys-info version all'
print 'info-center loghost 10.10.20.250'
print 'snmp-agent community read ' + GPublicSNMP # A-Series
print 'snmp-agent community write ' + GPrivateSNMP # A-Series
print 'snmp-agent trap if-mib link extended'
print 'snmp-agent target-host trap address udp-domain trapserver-IP-Address-here params securityname ' + GPrivateSNMP +  ' v2c'
print 'local-user ' + GsshUserName
print '  password simple ' + GsshPassword
print '  authorization-attribute level 3'
print '  service-type ssh'
print '  service-type web'
print '  quit'
print 'public-key local create rsa' #this requires keyboard input
print 'ssh server enable'
print 'user-interface vty 0 15'
print 'authentication-mode scheme'
print 'protocol inbound ssh telnet'
print 'user privilege level 3'
print 'quit'
print 'return' # make sure your in usermode for this command else it will not work.
print 'clock datetime ' + mytimedate
print 'system-view'
print 'clock timezone PST minus 8'
print 'clock summer-time PDT repeating 02:00:00 03/09/2014 02:00:00 11/02/2014 01:00:00'
print 'quit'
print ' ----------------------------------------'
print 'E-Series config: '
print 'snmp-server community ' + GPublicSNMP + ' operator' # E-Series
print 'snmp-server community ' + GPrivateSNMP + ' unrestricted' # E-Series
print 'password manager user-name ' + GsshUserName + ' plaintext ' + GsshPassword
print 'clock datetime ' + mytimedate
print 'clock timezone us pacific'
print 'clock summer-time'
print 'crypto key generate ssh rsa bits 1024'
print 'ip ssh'
