def generate_prime_nums(n):
  #initialize empty list
  prime_list = []
  for candidateprime in range(2,n):
    '''
    declare that candidateprime number is prime before entering loop
    '''
    is_prime = True
    #check if candidateprime is divible by numbers other than itself.
    for x in range (2,candidateprime):
      if candidateprime % x == 0:#1 is not a prime number,therefore omitted in original list
        is_prime = False
    if is_prime:
      prime_list.append(candidateprime)
  return prime_list
#print(generate_prime_nums(100))


