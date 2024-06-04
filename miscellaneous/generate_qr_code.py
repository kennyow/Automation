#pip install qrcode
#pip install Pillow
import qrcode



path =  'Automation/miscellaneous/'
img = qrcode.make('www.terra.com.br')
img.save(path+'qr3.png')