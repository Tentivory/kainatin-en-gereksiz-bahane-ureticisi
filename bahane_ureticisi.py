#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kainatın En Gereksiz Bahane Üreticisi
=====================================
Bu yazılım, evrenin en derin sırlarını çözmek için değil,
sadece senin bugün hiçbir şey yapmama kararını meşrulaştırmak için tasarlanmıştır.

Bilimsel olarak kanıtlanmıştır ki: Bahane üretmek, üretkenlikten daha zevklidir.
"""

import random
import time
import sys

# Gizli not: 6f7a6765726c696b206865726b6573696e2068616b6b69646972 (hex olarak saklanmıştır, dikkat çekmesin)

bahaneler = [
    "Bugün kuantum fiziği beni engelliyor. Elektronlarım karar veremedi.",
    "Ay'ın konumu ruh halimi etkiliyor ve bugün Ay tam da 'hiçbir şey yapma' pozisyonunda.",
    "Komşunun kedisi bana telepatik olarak 'bugün dinlen' mesajı gönderdi. Reddedemem.",
    "Evrenin genişleme hızı bugün biraz fazla, o yüzden ben de yavaşladım.",
    "Kahvaltıda yediğim yumurta bana felsefi bir soru sordu, cevabını düşünüyorum hâlâ.",
    "Zamanın göreceliliği yüzünden şu an aslında dünüm, o yüzden bugünkü işleri yarına bırakıyorum.",
    "Beynimdeki nöronlar greve çıktı. Sendika temsilcisiyle görüşme devam ediyor.",
    "Bulutlar bugün çok dramatik şekiller almış, onları izlemek bilimsel bir zorunluluk.",
    "WiFi sinyalim duygusal olarak yorgun, ben de ona empati duyuyorum.",
    "Dünya kendi ekseni etrafında dönerken ben de kendi tembellik eksenimde dönüyorum.",
    "Sabah kalktığımda yerçekimi biraz fazla kuvvetliydi, o yüzden yataktan çıkamadım.",
    "Bir paralel evrende zaten her şeyi bitirdim, bu evrende dinlenmeye karar verdim.",
    "Kahve makinem bana 'sen yeterince kahve içmedin' diye bakıyor, önce onu mutlu etmeliyim.",
    "Güneş ışınları bugün özellikle tembellik frekansında titreşiyor.",
    "Rüyamda bir ejderha bana 'bugün hiçbir şey yapma' diye fısıldadı. Ejderhalara karşı gelinmez."
]

def dramatik_yukleme():
    print("\n" + "="*60)
    print("   KAINATIN EN GEREKSİZ BAHANE ÜRETİCİSİ v1.0")
    print("   Bilimsel Kesinlikle Çalışır (Belki)")
    print("="*60)
    print("\nBahane motoru ısınıyor...")
    for i in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n\nHazır! Evrenin en abartılı bahanesi seçiliyor...\n")
    time.sleep(0.8)

def uret():
    bahane = random.choice(bahaneler)
    print("🎯 BUGÜNKÜ RESMİ BAHANEN:")
    print("-" * 50)
    print(f"\"{bahane}\"")
    print("-" * 50)
    print("\nBu bahane, uluslararası tembellik standartlarına uygundur.")
    print("Kullanım hakkı: Sonsuza kadar, her yerde, herkese karşı.\n")

if __name__ == "__main__":
    dramatik_yukleme()
    uret()
    print("\n" + "="*60)
    print("Program başarıyla hiçbir şey yapmana yardımcı oldu.")
    print("Tekrar çalıştırmak için: python bahane_ureticisi.py")
    print("="*60)
