def shoplist(zoz:list):
  cena = 0
  for i in range(0,len(zoz),2):
    cena1 = zoz[i]*zoz[i+1]
    cena += cena1
  print (cena)
  return cena

shoplist([3,2.5,0.5,10,1.2,1.2])
