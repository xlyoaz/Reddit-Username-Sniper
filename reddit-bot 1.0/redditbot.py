import praw
import itertools

# Reddit API kimlik bilgileri
client_id = ''
client_secret = ''
user_agent = ''
username = ''
password = ''

# Reddit istemcisini oluştur
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

# Kontrol edilecek kullanıcı adı karakterleri
karakterler = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
uzunluk = 3

# Mevcut olmayan kullanıcı adlarını saklamak için bir liste oluştur
mevcut_olmayanlar = []

with open('mevcut_olmayanlar.txt', 'w') as dosya:
    for kombinasyon in itertools.product(karakterler, repeat=uzunluk):
        kullanici_adi = ''.join(kombinasyon)
        try:
            # Reddit API'nin search işlevini kullanarak kullanıcı adını kontrol et
            sonuclar = list(reddit.subreddit("all").search(f"author:{kullanici_adi}", limit=1))
            if not sonuclar:
                print(f"Kullanıcı adı mevcut değil: {kullanici_adi}")
                mevcut_olmayanlar.append(kullanici_adi)
                dosya.write(kullanici_adi + '\n')
        except praw.exceptions.APIException as e:
            print(f"API Hatası: {str(e)}")
        except praw.exceptions.PRAWException as e:
            print(f"PRAW Hatası: {str(e)}")
        except Exception as e:
            print(f"Diğer Hata: {str(e)}")

print("İşlem tamamlandı. Mevcut olmayan kullanıcı adları 'mevcut_olmayanlar.txt' dosyasına kaydedildi.")
