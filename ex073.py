# Times
times = ('Botafogo','Flamengo','Palmeiras','Grêmio','Fluminense','Bragantino','Athletico-PR',
         'São Paulo','Cuiabá','Cruzeiro','Fortaleza','Internacional','Atlético-MG','Corinthians',
         'Santos','Goiás','Bahia','Coritiba','América-MG','Vasco')
print('-'*30)
print(f"Os primeiros 5 times são: {times[:5]}")
print('-'*30)
print(f"Ultimos 4 times: {times[-4:]}")
print('-'*30)
print(f"Ordem ALfabetica: {sorted(times)}")
print('-'*30)
print(f"Onde está o São Paulo: {times.index('São Paulo')+1}ª Posição")
print('-'*30)
