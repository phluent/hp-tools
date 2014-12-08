# HPN Link agg
# aggInterfaces = the number of interfaces used in this Link agg
# aggPortType = Use Ten-GigabitEthernet, FastEthernet etc.
# aggPortList = Interface numbering scheme i.e. 1/0/4, 2/0/13 etc.
# aggGroupNumber = agg group number 1-1024
# aggPermitVlan = permitted vlan's
import sys
class default:
    aggGroupNum = 110
    aggInterfaces = 4
    aggPortType = 'Ten-GigabitEthernet'
    aggToAseries = 'Yes'
print 'NOTE: Ranges are  in <>, defaults are [] '
aggPortList = [] # Create a list
aggPortType = default.aggPortType
aggToAseries = 'Yes'

try:
    aggGroupNum = input("Enter Group number <1-1024> [110]: ")
except SyntaxError:
    aggGroupNum = default.aggGroupNum
try:
    aggInterfaces = input("Enter The number of link agg interfaces <1-8> [4]: ")
except SyntaxError:
    aggInterfaces = default.aggInterfaces

aggPortType = raw_input('Enter the Interface name <Ten-GigabitEthernet> [Ten-GigabitEthernet]: ')
if not aggPortType:
    aggPortType = default.aggPortType
for i in range(aggInterfaces):
    aggPortList.append(raw_input('interface port <1/0/4>: '))
aggPermitVlan = raw_input('Enter each permitted Vlan seperate with a comma i.e. <3,27,110>:').split(",")
try:
    aggUndoPermitVlan = raw_input('Enter NOT permitted Vlans seperate with a comma i.e. <1,6>:').split(",")
except SyntaxError:
    del aggUndoPermitVlan[:]
print 'system view'
for x in range(0, len(aggPermitVlan)):
    print 'vlan ' + aggPermitVlan[x]
    print 'quit'
print 'interface Bridge-Aggregation ' + str(aggGroupNum)
print 'link-aggregation mode dynamic'

print 'quit'
for x in range(0,aggInterfaces):
    print 'interface ' + aggPortType + aggPortList[x]
    print 'port link-type trunk '
print 'quit'
print 'interface Bridge-Aggregation ' + str(aggGroupNum)
print 'port link-type trunk'
for x in range(0, len(aggUndoPermitVlan)):
    if aggUndoPermitVlan[0] != '':
        print 'undo port trunk permit vlan' + aggUndoPermitVlan[x]
for x in range(0, len(aggPermitVlan)):
    print 'port trunk permit vlan ' + aggPermitVlan[x]
print 'quit'
print 'save'
