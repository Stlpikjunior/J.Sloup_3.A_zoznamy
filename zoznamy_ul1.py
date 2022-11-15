def vyptyp(x:list):
  for i in x:
    if type(i) == int or type(i)==float:
      print(i,' - číslo')
    elif type(i) ==str:
      print(i,' - reťazec')
    else:
      print(i,' - iný typ')

vyptyp([1,2,"cislo",True])