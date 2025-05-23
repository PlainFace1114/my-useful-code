# loader our newly minted testbed file
from genie.testbed import load
testbed = load('network.yaml')

# access the devices
testbed.devices
# AttrDict({'ios-1': <Device ott-tb1-n7k4 at 0xf77190cc>,
#           'ios-2': <Device ott-tb1-n7k5 at 0xf744e16c>})
ios_1 = testbed.devices['2960x-sw']
ios_2 = testbed.devices['c9300-sw']

# establish basic connectivity
ios_1.connect()
#ios_2.connect()

#parse commands
output = testbed.devices['2960x-sw'].parse('show run')
#pyats parse "show run" --testbed-file network.yaml
# issue commands
print(ios_1.execute('show run | include username'))
