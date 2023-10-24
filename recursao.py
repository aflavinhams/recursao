# ---------------------   EXERCÍCIO 1 ------------------------

# Letra a
def S(n):

    if n == 1:
        return 10
    elif n >= 2:
        return S(n-1) + 10

# Letra b
def A(n):

    if n == 1:
        return 2
    elif n >= 2:
        return A(n-1)**-1

# Letra c
def B(n):

    if n == 1:
        return 1
    elif n >= 2:
        return B(n-1) + n**2

# Letra d
def P(n):

    if n == 1:
        return 1
    elif n >= 2:
        return n**2 * P(n-1) + n - 1

# Letra e
def D(n):

    if n == 1:
        return 3
    elif n == 2:
        return 5
    elif n > 2:
        return (n-1) * D(n-1) + (n-2) * D(n-2)

# Letra f
def W(n):

    if n == 1:
        return 2
    elif n == 2:
        return 5
    elif n > 2:
        return W(n-1) * W(n-2)

# Letra g
def T(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n > 3:
        return T(n-1) + 2 * T(n-2) + 3 * T(n-3)

# ---------------------  EXERCÍCIO 3 ------------------------

def T2(n):

    if n == 2:
        return True
    elif n > 2:
        return T2(n - 3) or T2(n / 2)
    else:
        return False
    
# Resposta: apenas o 7 e o 19 pertencem a T

# ---------------------  EXERCÍCIO 4 ------------------------

def M(n):
  
  if n == 2 or n == 3:
      return True
  if n < 2:
      return False

  for x in range(2, n):
      if n % x == 0 and M(x) and M(n // x):
          return True

  return False

# Resposta: apenas os numeros 6, 9, 16, 54, 72

# ---------------------  EXERCÍCIO 5 ------------------------

def S(n):

    a = 'a'
    b = 'b'
    if n == a or n == b:
        return True
    elif n == S(n) + b:
        return True
    else:
        return False
    
print(S('aa'))

# ---------------------  EXERCÍCIO 9 ------------------------

def triangulos(n):

    return n == (n**2 + n - 2) / 2 + 1
