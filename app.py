import re
from collections import Counter

# Abra o arquivo de log do Squid em modo de leitura
with open('squid.log', 'r') as f:
  # Crie uma lista vazia para armazenar os sites bloqueados
  blocked_sites = []

  # Use um loop for para percorrer cada linha do arquivo de log
  for line in f:
    # Use uma expressão regular para extrair o endereço do site bloqueado da linha atual
    site = re.search(r'BLOCKED_SITE=([^\s]+)', line)
    if site:
      # Adicione o endereço do site bloqueado à lista
      blocked_sites.append(site.group(1))

  # Use a função Counter para contar a frequência de cada site na lista
  site_counts = Counter(blocked_sites)

  # Classifique o dicionário pelos valores (frequências) em ordem decrescente
  sorted_sites = sorted(site_counts.items(), key=lambda x: x[1], reverse=True)

  # Imprima os sites e as frequências
  for site, count in sorted_sites:
    print(f'{site}: {count}')