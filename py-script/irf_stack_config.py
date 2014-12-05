## This is a Comware IRF stack configuration builder
# written by Ray Glauner and modifed by Mike Skelly

# This is Ten gig interfaces using four ports on each module.
# Change the information in the IRF class to change the port names/numbers.
class default:
    IrfPreamble = 'irf mac-address persistent timer', 'irf auto-update enable' ,'undo irf link-delay'
    IrfPort = 'irf-port 1/1','irf-port 2/2'
    IrfMemPri = 'irf member 1 priority 30','irf member 2 priority 25'
    PortTypeName = 'Ten-GigabitEthernet'
    PortInt = ['Ten-GigabitEthernet1/0/1','Ten-GigabitEthernet1/0/2','Ten-GigabitEthernet1/0/13','Ten-GigabitEthernet1/0/14'],['Ten-GigabitEthernet2/0/1','Ten-GigabitEthernet2/0/2','Ten-GigabitEthernet2/0/13','Ten-GigabitEthernet2/0/14']
PortTypeName=''
PortList1 = [] # Create a list of port numbers e.g. 1/0/22
PortList2 = [] # Create a list of port numbers e.g. 2/0/13
PortInt =[]
tmp1 = []
tmp2 =[]
try:
    numIRFPorts = input("Enter the number of Interfaces to configure on fisrt switch <1-8> [2]: ")
except SyntaxError:
    numIRFPorts = 2

PortTypeName = raw_input('Enter the Interface name <Ten-GigabitEthernet> [Ten-GigabitEthernet]: ')
if PortTypeName =='':
    PortTypeName = default.PortTypeName
for i in range(numIRFPorts):
    PortList1.append(raw_input('interface port for IRF member 1 <1/0/4>: '))
for i in range(numIRFPorts):
    PortList2.append(raw_input('interface port for IRF member 2 <1/0/4>: '))
for x in range(0,len(PortList1)):
    tmp1.append(PortTypeName+PortList1[x])
PortInt.append(tmp1)
for x in range(0,len(PortList2)):
    tmp2.append(PortTypeName+PortList2[x])
PortInt.append(tmp2)

print '****************************'
print 'Unplug all cables used for IRF on these systems'
print '****************************'
print 'On Switch 2 do the following'
print '****************************'
print 'system'
print 'irf member 1 renumber 2'
print '---> you must answer YES before proceding'
print 'save'
print 'quit'
print 'reboot'
print '****************************'
print 'end of switch 2 config for now'
print '****************************'
print 'On Switch 1 do the following'
print '****************************'
print 'system'
for x in range(0,len(PortInt[0])):
    print 'interface ' + PortInt[0][x]
    print 'shutdown'
print 'quit'
for x in range(0,len(default.IrfPreamble)):
    print default.IrfPreamble[x]
print default.IrfMemPri[0]
print 'irf-port 1/1'
for x in range(0, len(PortInt[0])):
    print 'port group interface ' + PortInt[0][x] + ' mode enhanced'

for x in range(0,len(PortInt[0])):
    print 'interface ' + PortInt[0][x]
    print 'undo shutdown'
print 'quit'
print 'save'
print '****************************'
print 'Member 1 is done'
print '****************************'
print 'Finish member 2 configuration'
print '****************************'
for x in range(0,len(PortInt[0])):
    print 'interface ' + PortInt[1][x]
    print 'shutdown'
print 'quit'
for x in range(0,len(default.IrfPreamble)):
    print default.IrfPreamble[x]
print default.IrfMemPri[1]
print default.IrfPort[1]
for x in range(0, len(PortInt[0])):
    print 'port group interface ' + PortInt[1][x] + ' mode enhanced'
for x in range(0,len(PortInt[0])):
    print 'interface ' + PortInt[1][x]
    print 'undo shutdown'
    print 'quit'
    print 'save'
print '****************************'
print 'plug in all IRF cables both members'
print 'member two should reboot when plugging in the cables'
print '****************************'
print ' 5900 do this on both switches -irf-port-configuration active.'
raw_input('hit any key when done:')
