class PrimeNumber():
  def __init__(self):
    pass
  def generate_prime(self,n):
    self.n = n
    #initialize empty list
    prime_list = []
    for candidateprime in range(2,n):
      is_prime = True
      
      for x in range (2,candidateprime):
        
        if candidateprime % x == 0:
          is_prime = False
        
      if is_prime:
        prime_list.append(candidateprime)
    return prime_list

num = PrimeNumber()
print (num.generate_prime(20))
