#pip install mss
from mss import mss


path = 'Automation/controling_devices/'
with mss() as screen:
         screen.shot(output=path+'screenshot.png')