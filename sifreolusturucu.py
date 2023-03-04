import random

#Parola Uzunluğu Seçebilirsiniz!
parola_uzunluk = int(input('\nParolanızın Uzunluğunu Giriniz: '))

kucuk_harf = "abcdefghijklmnoprstuvyzx"
buyuk_harf = "ABCDEFGIJKLMNOPRSTUVYZX"
numaralar = "0123456789"
karakterler = "£#$%+^!*/"

kullan = kucuk_harf + buyuk_harf + numaralar + karakterler

parola = "".join(random.sample(kullan, parola_uzunluk))

print(parola)
