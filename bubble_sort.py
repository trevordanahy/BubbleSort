def bubble(alist):
  max_run = len(alist)-1

#The sort runs 1 time less than the lenght of the list.
  for n in range(0,max_run):
    for i in range(0,max_run):
      if alist[i] > alist[i+1]:
        #swap item places 
        alist[i], alist[i+1] = alist[i+1], alist[i]
  return alist