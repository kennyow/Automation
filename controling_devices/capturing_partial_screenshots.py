#pip install mss
from mss import mss, tools


path = 'Automation/controling_devices/'
with mss() as screen:
    part = {'top':257, 'left':900, 'width':500, 'height':400}
    image = screen.grab(part)
    tools.to_png(image.rgb, image.size, output=path+'output.png')
         #screen.shot(output=path+'screenshot.png')