import re

slideOrder = [74,69,70,68,48,72,75,77,76,64,51,67,73,55,56,65,50,62,54,32,60,46,71,47,44,53,59,24,52,61,6,5,23,49,29,78,57,66,7,40,3,25,33,63,30,17,16,43,8,42,31,41,45,34,35,4,18,28,58,39,2,21,20,22,37,27,26,19,12,13,1,38,36,14,9,11,10,15,79]

fileS = open("test.txt",'r').read()
slides = re.findall(r"^<!--nextpage-->\n?(\[tps.+?</a>.+?\n.+?\n)",fileS,re.M|re.S)

reorderedSlides = []
for slideNum in slideOrder:
  if slideNum > 2 :
    slideContent = slides[slideNum-2]
    reorderedSlides.append(slideContent)
    #print(slideContent)

startNum = 2
for content in reorderedSlides:
  slideNumber = startNum
  startNum+=1
  newUrl = 'who-is-donald-trumps-ideal-vice-president-pick/%d/' % slideNumber
  modifiedContent = re.sub(r'who-is-donald-trumps-ideal-vice-president-pick/[0-9]?[0-9]?/?',newUrl,content)
  print(modifiedContent + '\n<!--nextpage-->\n')
