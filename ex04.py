segundo=int(input('Por favor, entre com o número de segundos que deseja converter:',))
minuto=segundo//60
seg_resto=segundo%60
hora=minuto//60
min_resto=minuto%60
dia=hora//24
hora_resto=hora%24
print(dia,'dias,',hora_resto,'horas,',min_resto,'minutos e',seg_resto,'segundos.');
