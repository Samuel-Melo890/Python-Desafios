print('='*8,'Conversao de Unidades de Distancia','='*8)
d = float(input('De-me uma distancia em metros:'))
print('''O valor da conversao de metros para outras unidades sera de:
km: {}km
hm: {}hm
dam: {}dam
dm: {}dm
cm: {}cm
mm: {}mm'''.format(d/1000,d/100,d/10,d*10,d*100,d*1000))
