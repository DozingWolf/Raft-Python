import sys
sys.path.append('../source code')
from raftmachine import RaftMachine

rm01_listener = RaftMachine(modelname = 'RMListener')
rm01_listener.getRaftMachineInfo()

rm01_sender = RaftMachine(modelname='RMSender')
rm01_sender.getRaftMachineInfo()
