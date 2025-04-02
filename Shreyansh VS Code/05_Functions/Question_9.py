def even_numbers_generator(limit):
 
  number = 0  
  while number <= limit:
    yield number  
    number += 2   
for even_num in even_numbers_generator(10):
  print(even_num)