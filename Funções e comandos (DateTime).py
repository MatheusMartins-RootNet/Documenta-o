# DateTime
import datetime
from time import strftime

datetime.datetime.now().strftime('%d|%m|%Y') # Jeito completo

strftime('%d|%m|%Y')  # Jeito mais simples

# %d = Dia  |  %m = Mês  |  %Y = Ano

# %H = Hora 24H
# %I = Hora 12H
# %p = AM / PM
# %M = Minuto
# %S = Segundo

# %w = Dia da semana (em número)
# %D = Dia abreviado
# %b = Mês abreviado
# %y = Ano abreviado
# %j = Dia no ano
