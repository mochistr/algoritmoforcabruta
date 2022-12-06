n = 7099894159

def fatores_primos(n): 
  i = 2 
  fatores = [] 
  while i * i <= n: 
    if n % i != 0:
      i += 1
    else:  
      n = n // i
      fatores.append(i) 
  if n > 1:
    fatores.append(n) 
  return fatores

print(fatores_primos(n))
