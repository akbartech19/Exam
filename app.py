def juft_sonlarni_sarala(royxat):
    juft_sonlar = []
    for son in royxat:
        if son % 2 == 0: 
            juft_sonlar.append(son) 
    return juft_sonlar

mening_sonlarim = [12, 23, 45, 67, 89]

natija = juft_sonlarni_sarala(mening_sonlarim)

print(natija)  