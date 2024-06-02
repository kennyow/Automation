from mss import mss
import time
from datetime import datetime


path = 'Automation/controling_devices/'
# Set interval (600 sec = 10 min)
interval = 6
 
while True:
    with mss() as screen:
        # Filepath will have the current datetime (e.g., 2022-02-02 13:17:21.png)
        filepath = f"{path}{datetime.now().strftime('%Y-%m-%m %H-%M-%S')}.png"
        screen.shot(output=filepath)
 
    print(filepath)
    time.sleep(interval) # Wait 600 sec/ 10 min