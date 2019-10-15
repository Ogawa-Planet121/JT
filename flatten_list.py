# Created by James Tavs
------------------------
intergerList = [1,[9,2],4,6,(4,5),9]  # < Note: Nested List and a tuple embedded
#-----------------------------
def flattenLists(listPassed):
  flattenList = []
  for x in listPassed:
      if type(x) == tuple:
          for y in(list(x)):
              flattenList.append(y)
      elif type(x) == list:
           for y in x:
                flattenList.append(y)
      else:
          flattenList.append(x)
  return flattenList

listFlatten = flattenLists(intergerList)
print(listFlatten)
--------------------------------------------------
Output
------
[1, 9, 2, 4, 6, 4, 5, 9]