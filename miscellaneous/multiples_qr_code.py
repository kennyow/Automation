import qrcode
 


path =  'Automation/miscellaneous/'
with open(path+'urls.txt') as file:
  lines = file.readlines()
  count = 1
  for line in lines:
    img = qrcode.make(line)
    img.save(f"{path}{count}.png")
    count += 1