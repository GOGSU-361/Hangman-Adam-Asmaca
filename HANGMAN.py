from random import randint
fruits=["portakal","armut","karpuz","incir","elma","mandalina","çilek","böğürtlen","kiraz","mango"]
animals=["maymun","köpek","zürafa","yılan","ahtapot","kertenkele","martı","kartal","kaplan","iguana"] 
words=fruits+animals                             #rastgele kelimenin seçileceği liste, tüm kelimeleri içerir
secret_word=words[randint(0,len(words))-1]           
a=["      |","      |","      |","      |"]      #oyunda adamın asılacağı kısım, satır satır
body_parts=["o","|","/","\\","/","\\"]  #vücüt parçaları her yanlış cevapta ilgili satıra sırayla eklenecek
false_answers=0    #yanlış tahmin sayısı (harf tahmini)
true_answers=0     #kelimede açılan harf sayısı -> ilerde tüm kelimenin açılıp açılmadığının kontrolü için                                
bonus_points=0
score=0
guesses=[]    #SADECE tahminleri içerir/Tahmin edilen harflerin gösterilmesini ve bonus harflerden ayrı tutulmasını sağlar
letters=[]    #letters listesi hem TAHMİNLERİ hem de işlem ile açılan BONUS harfleri içerir. Kelimeyi ekrana yazdırırken kullanılır.
math_process=[]
letter_check="abcçdefgğhıijklmnoöprsştuüvyz"
print("=== Calc & Hang: İşlem Yap, Harfi Kurtar! ===")
while True:
    print("\n\n--Yeni Tur--\n\n  +---+\n  |   |") if len(secret_word)!=true_answers and false_answers!=6 else print("\n\n\n=========== OYUN BİTTİ ===========\n  +---+\n  |   |")  #adam asmacada değişiklik yapılmayacak kısım (platformun en üstü + ip)        
    if false_answers>5:                                        
        a[2]=a[2][:3]+body_parts[false_answers-1]+a[2][4:]
    elif false_answers>4:
        a[2]=a[2][:1]+body_parts[false_answers-1]+a[2][2:]  
    elif false_answers>3:
        a[1]=a[1][:3]+body_parts[false_answers-1]+a[1][4:]      #yapılan hatalı tahmin sayısına bağlı olarak ilgili satıra ilgili vücüt parçasını ekle
    elif false_answers>2:
        a[1]=a[1][:1]+body_parts[false_answers-1]+a[1][2:]     
    elif false_answers>1:
        a[1]=a[1][:2]+body_parts[false_answers-1]+a[1][3:]
    elif false_answers>0:
        a[0]=a[0][:2]+body_parts[false_answers-1]+a[0][3:]
    else:pass

    [print(i) for i in a]         #ilk tahminden önce platformu çiz, ardından yanlış/doğru cevaplara bağlı olarak yapılan değişikliklere göre çiz
    print("============")
    print("Kelime : ",end=""),[print("_ ",end="") if i not in letters else print(i+" ",end="") for i in secret_word[0:len(secret_word)]] #ilk turda sadece _ basar, ardından tahmin alındıktan hemen 
    print("\nTahmin edilen harfler : {}".format((",").join(guesses)))                                                                   #sonra tahmin edilen harf ile kelimedeki her harfi tek tek karşılaştır.
    print("Bonus puanlar: {}".format(bonus_points))

    if true_answers==len(secret_word) or false_answers==6:
        pass
    else:
        print("Seçenekler: [H]arf tahmini | [İ]şlem çöz | [I]pucu | [Ç]ıkış")       #Eğer oyun BİTMİŞSE input alınmayacak, break devreye girecek -> Bu satıra gerek YOK.

    if false_answers==6:               
        print("\n\033[31mKAYBETTIN!")
        break
    if true_answers==len(secret_word):                       #Sonraki turlarda döngü {Tahmin al>Tahmine uygun adamı çiz} şeklinde ilerleyeceği için çizme kısmının HEMEN altına 
        print("\n\033[32mKAZANDIN!")                                 # ve bir sonraki tahminden HEMEN önce win/lose kontrolü
        score+=50
        break

    process=input("Seçiminiz:")
    if process.upper()=="H":                                         #process>H>Harf tahmini al
        guess=input("Harf:").lower()
        if len(guess)!=1 or guess not in letter_check:               #Harf tahmini geçerli mi?  Evet->Devam / Hayır->Döngüyü kır bir sonraki tur
            print("\n\033[33mGeçersiz harf tahmini:\033[0m  {}".format(guess))
            continue
        else:
            if guess not in guesses and guess not in letters: #Mevcut tahmin önceden DENENMEMİŞSE ve ya BONUS HARF ile açılmadıysa tahmini kabul et/kullan
                guesses.append(guess)
                if guess not in secret_word:                                                                
                    false_answers+=1
                    print("\U0000274C Yanlış harf:{} | Kalan hata hakkı={}".format(guess,6-false_answers))
                    score-=5
                else:
                    print("\U00002705 Doğru harf:{} | Kalan hata hakkı={}".format(guess,6-false_answers))
                    letters.append(guess)
                    true_answers+=secret_word.count(guess)      #Tahmin edilen harf kelimede ne kadar tekrar ediyorsa açılan harf sayısını tutan değişkene sayarak ekle->Kazandın/Kaybettin kontrolü için
                    score+=10
            else:                                                                                  #Mevcut tahmin önceden DENENMİŞSE hiçbir şey yapmadan atla
                continue

    elif process=="İ":                                    #process>İ>işlem seç/yap
            islem=str(input("İşlem türünü seçin (toplama/çıkarma/çarpma/bölme) veya 'iptal' yazarak çıkış yapın:\n=>Her işlem türü bir kere kullanılabilir! "))
            if islem.lower()=="iptal":
                continue
            elif islem.lower()=="toplama" and 1 not in math_process:
                n1=input("1. sayı (iptal için 'iptal')")
                if n1=="iptal":continue
                else:pass
                n2=input("2. sayı (iptal için 'iptal')")
                if n2=="iptal":continue
                else:pass
                print("Soru: {} + {}".format(n1,n2))
                sonuc=float(input("Cevabınız:"))
                math_process.append(int(1))
                if sonuc==float(n1)+float(n2):
                    score+=15
                    bonus_points+=1
                    while True:
                        bonusharf=secret_word[randint(0,len(secret_word)-1)]
                        if bonusharf not in letters:
                            letters.append(bonusharf)                                                   #bonus harf açılmamış bir harf olana kadar döngü yeni bir bonus harf seçer.
                            true_answers+=secret_word.count(bonusharf)
                            print("\033[34mDoğru cevap!\033[0m\nBonus ödül \U0001F389: '{}' harfi açıldı ".format(bonusharf))
                            break
                else:
                    print("\033[33mYanlış Cevap!\033[0m")
                    score-=10
                    false_answers+=1
            elif islem=="çıkarma" and 2 not in math_process:
                n1=input("1. sayı (iptal için 'iptal')")
                if n1=="iptal":continue
                else:pass
                n2=input("2. sayı (iptal için 'iptal')")
                if n2=="iptal":continue
                else:pass
                print("Soru: {} - {}".format(n1,n2))
                sonuc=float(input("Cevabınız:"))
                math_process.append(int(2))
                if sonuc==float(n1)-float(n2):
                    score+=15
                    bonus_points+=1
                    while True:
                        bonusharf=secret_word[randint(0,len(secret_word)-1)]
                        if bonusharf not in letters:
                            letters.append(bonusharf)                        #bonus harf kaydedilerek kelimeyi yazdırırken kullanılır.
                            true_answers+=secret_word.count(bonusharf)
                            print("\033[34mDoğru cevap!\033[0m\nBonus ödül \U0001F389: '{}' harfi açıldı ".format(bonusharf))
                            break
                else:
                    print("\033[33mYanlış Cevap!\033[0m")
                    score-=10
                    false_answers+=1
            elif islem.lower()=="çarpma" and 3 not in math_process:
                n1=input("1. sayı (iptal için 'iptal')")
                if n1=="iptal":continue
                else:pass
                n2=input("2. sayı (iptal için 'iptal')")
                if n2=="iptal":continue
                else:pass
                print("Soru: {} * {}".format(n1,n2))
                sonuc=float(input("Cevabınız:"))
                math_process.append(int(3))
                if sonuc==float(n1)*float(n2):
                    score+=15
                    bonus_points+=1
                    while True:
                        bonusharf=secret_word[randint(0,len(secret_word)-1)]
                        if bonusharf not in letters:
                            letters.append(bonusharf)
                            true_answers+=secret_word.count(bonusharf)
                            print("\033[34mDoğru cevap!\033[0m\nBonus ödül \U0001F389: '{}' harfi açıldı ".format(bonusharf))
                            break
                else:
                    print("\033[33mYanlış Cevap!\033[0m")
                    score-=10
                    false_answers+=1
            elif islem.lower()=="bölme" and 4 not in math_process:
                n1=input("1. sayı (iptal için 'iptal')")
                if n1=="iptal":continue
                else:pass
                n2=input("2. sayı (iptal için 'iptal')")
                if n2=="iptal":continue
                else:pass
                print("Soru: {} / {}".format(n1,n2))
                sonuc=float(input("Cevabınız:"))
                math_process.append(int(4))
                if sonuc==float(n1)/float(n2):
                    score+=15
                    bonus_points+=1
                    while True:
                        bonusharf=secret_word[randint(0,len(secret_word)-1)]
                        if bonusharf not in letters:
                            letters.append(bonusharf)
                            true_answers+=secret_word.count(bonusharf)
                            print("\033[34mDoğru cevap!\033[0m\nBonus ödül \U0001F389: '{}' harfi açıldı ".format(bonusharf))
                            break
                else:
                    print("\033[33mYanlış Cevap!\033[0m")
                    score-=10
                    false_answers+=1

    elif process=="I":                          
        if bonus_points>=1:                             #Bonus puan yeterli/yetersiz kontrolü
            print("\n\033[34mIPUCU[Tür]: {}\033[0m".format("Hayvan" if secret_word in animals else "Meyve")) #Bonus puan yeterli > Kelime animals listesinde ise HAYVAN ipucu ver değil ise Meyve ver 
            bonus_points-=1                                                                                  #Çünkü 2 liste var hayvan değilse %100 meyve. -> Kullanılan bonus puanı EKSİLT.
        else:
            print("Yetersiz bonus puan")   
    elif process.upper()=="Ç":
        print("\n\u2757ÇIKIŞ YAPILDI\nBu oyunun skoru hesaplanmayacaktır.")
        exit()             
print("======================\nKelime : {}\nOYUN SONU SKORUN : {}\n======================\033[0m\n\n".format(secret_word.upper(),score))      #Döngü kırılıp oyun bittikten sonra kelimeyi ve skoru yazdır.