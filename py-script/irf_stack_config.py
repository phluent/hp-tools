## This is a Comware IRF stack configuration builder
# written by Ray Glauner and modifed by Mike Skelly

# This is Ten gig interfaces using four ports on each module.
# Change the information in the IRF class to change the port names/numbers.
class default:
    IrfPreamble = 'irf mac-address persistent timer', 'irf auto-update enable' ,'undo irf link-delay'
    IrfMemPri = '50','40','30','25','20','15','10','5'
    PortTypeName = 'Ten-GigabitEthernet'
PortTypeName=''
numIRFMembers = []
irfMembers = []

try: 
    numIRFMembers = input("Enter the number of IRF Members <2-8> [2]: ")
except SyntaxError:
    numIRFMembers = 2

numIRFPorts = 2 # Not sure that it makes sense to have more than two IRF ports, all somple configurations stop there
#try:
#    numIRFPorts = input("Enter the number of Interfaces to configure for irf <1-2> [2]: ")
#except SyntaxError:
#    numIRFPorts = 2

PortTypeName = raw_input('Enter the Interface name <Ten-GigabitEthernet> [Ten-GigabitEthernet]: ')
if PortTypeName =='':
    PortTypeName = default.PortTypeName

for i in range(numIRFMembers):
    memberPorts = []
    for n in range(numIRFPorts):
        tmpPort = raw_input('interface port for IRF member {member} port {port} <{member}/0/{port}>: '.format(member=i+1,port=n+1))
        if tmpPort == '':
            tmpPort = str(i+1) + '/0/' + str(n+1)
        memberPorts.append(PortTypeName+tmpPort)
    irfMembers.append(memberPorts)

def note(message):
    print '# '+message

def separator():
    print '############################'

separator()
note('Unplug all cables used for IRF on these systems')
separator()

# begin IRF config by renumbering member devices (last to first)
for i,e in reversed(list(enumerate(irfMembers))):
    current_member_id = i+1
    separator()
    if current_member_id == 1: break
    note('On switch %s run the following' % current_member_id)
    separator()
    print 'system'
    print "irf member 1 renumber %s" % current_member_id
    note('---> you must answer YES before proceding')
    print 'save'
    print 'quit'
    print 'reboot'
    separator()
    note('end of switch %s config for now' % current_member_id)


# continue IRF configuration by setting ports (first to last)
for i,ports in list(enumerate(irfMembers)):
    current_member_id = i+1
    separator()
    note('On Switch %s do the following' % current_member_id)
    separator()
    print 'system'
    for p in ports:
        print 'interface ' + p
        print 'shutdown'
    print 'quit'
    
    for line in default.IrfPreamble:
        print line

    print 'irf member %s priority %s' % (current_member_id, default.IrfMemPri[i])

    for n,interface in list(enumerate(ports)):
        print 'irf-port %s/%s' % (current_member_id,n+1)
        print 'port group interface %s mode enhanced' % (interface)

    for p in ports:
        print 'interface ' + p
        print 'undo shutdown'
    print 'quit'
    print 'irf-port-configuration active'
    print 'save'
    separator()
    note('Member %s is done' % current_member_id)

note('plug in all IRF cables all members')
note('members should reboot when plugging in the cables')
separator()
raw_input('hit any key when done:')
