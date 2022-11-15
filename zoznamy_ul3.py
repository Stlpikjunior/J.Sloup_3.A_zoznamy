def sucin(zoz:list):
  suc = 1
  for i in range(0,len(zoz)):
    suc *= zoz[i]
  print(suc)

sucin([2,3,5,7,11])