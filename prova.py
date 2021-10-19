
texto = open('d:/dadosdeviolencia.txt','r', encoding="utf8")

qV = 0
ttl = 0

for linha in texto:
 
    linhaatual = linha
    
    qV = linhaatual.count("Violência")
    
    ttl = ttl+qV
      
print('forão', ttl,'vezes')

texto.close()   