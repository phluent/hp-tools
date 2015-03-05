## This is a Comware IRF stack configuration builder
# written by Ray Glauner and modifed by Mike Skelly
# Defaults can be used through out.
# two to eight port IRF
# two to eight switch configuration
# Change the information in the IRF class to change the default port names/numbers.
outFile = open("IRF-8-output.txt","w")
class default:
    IrfPreamble = 'irf mac-address persistent timer', 'irf auto-update enable' ,'undo irf link-delay'
    IrfMemPri = '30','26','22','16','12','10','8','6'
    PortTypeName = 'Ten-GigabitEthernet'
PortTypeName=''
numIRFMembers = []
irfMembers = []
print 'This program will create the IRF configuration for two to eight switchs'
outFile.write('This program will create the IRF configuration for two to eight switchs\n')
print 'All the inputs have defaults in square brakets but will be overwitten by users input'
outFile.write('All the inputs have defaults in square brakets but will be overwitten by users input\n')
print 'The output is broken into sections, each section goes to individual switches'
outFile.write('The output is broken into sections, each section goes to individual switches\n')
print ''
outFile.write('\n')
try:
    numIRFMembers = input("Enter the number of IRF Members <2-8> [2]: ")
except SyntaxError:
    numIRFMembers = 2

try:
    numIRFPorts = input("Enter the number of IRF Ports per Switch <2-8> [2]: ")
except SyntaxError:
    numIRFPorts = 2

# numIRFPorts = 2 # Not sure that it makes sense to have more than two IRF ports, all somple configurations stop there
PortTypeName = raw_input('Enter the Interface name <Ten-GigabitEthernet> [Ten-GigabitEthernet]: ')
if PortTypeName =='':
    PortTypeName = default.PortTypeName

for i in range(numIRFMembers):
    memberPorts = []
    for n in range(numIRFPorts):
        tmpPort = raw_input('interface port for IRF member {member} port {port} <1/0/1> [{member}/0/{port}]: '.format(member=i+1,port=n+1));
        if tmpPort == '':
            tmpPort = str(i+1) + '/0/' + str(n+1)
        memberPorts.append(PortTypeName+tmpPort)
    irfMembers.append(memberPorts)

def note(message):
    print '# '+ message
    outFile.write('# '+ message)

def separator():
    print '############################\n'
    outFile.write('############################\n')

separator()
note('Unplug all cables used for IRF on these systems\n')
separator()

# begin IRF config by renumbering member devices (last to first)
for i,e in reversed(list(enumerate(irfMembers))):
    current_member_id = i+1
    separator()
    if current_member_id == 1: break
    note('On switch %s run the following\n' % current_member_id)
    separator()
    print 'system'
    outFile.write('system\n')
    print "irf member 1 renumber %s\n" % current_member_id
    outFile.write("irf member 1 renumber %s\n" % current_member_id)
    note('---> you must answer YES before proceding\n')
    print 'save'
    outFile.write('save\n')
    print 'quit'
    outFile.write('quit\n')
    print 'reboot'
    outFile.write('reboot\n')
    separator()
    note('end of switch %s config for now\n' % current_member_id)


# continue IRF configuration by setting ports (first to last)
for i,ports in list(enumerate(irfMembers)):
    current_member_id = i+1
    separator()
    note('On Switch %s do the following\n' % current_member_id)
    separator()
    print 'system'
    outFile.write('system\n')
    for p in ports:
        print 'interface ' + p
        outFile.write('interface ' + p+ '\n')
        print 'shutdown'
        outFile.write('shutdown\n')
    print 'quit'
    outFile.write('quit\n')

    for line in default.IrfPreamble:
        print line
        outFile.write(line + '\n')

    print 'irf member %s priority %s' % (current_member_id, default.IrfMemPri[i])
    outFile.write('irf member %s priority %s\n' % (current_member_id, default.IrfMemPri[i]))

    for n,interface in list(enumerate(ports)):
        mymod = ((n + 2) % 2) + 1   #to make irf-port come out 1/1,and 1/2 etc.
        print 'irf-port %s/%s' % (current_member_id,mymod)
        outFile.write('irf-port %s/%s\n' % (current_member_id,mymod))
        print 'port group interface %s mode enhanced' % (interface)
        outFile.write('port group interface %s mode enhanced\n' % (interface))

    for p in ports:
        print 'interface ' + p
        outFile.write('interface ' + p + '\n')
        print 'undo shutdown'
        outFile.write('undo shutdown\n')
    print 'quit'
    outFile.write('quit\n')
    print 'irf-port-configuration active'
    outFile.write('irf-port-configuration active\n')
    print 'save'
    outFile.write('save\n')
    separator()
    note('Member %s is done\n' % current_member_id)

note('plug in all IRF cables all members\n')
note('members should reboot when plugging in the cables\n')
note('ouput file is in current directory, named IRF-8-output.txt\n')
separator()
raw_input('Press OK to end, see file IRF-8-output.txt:')
outFile.close()
