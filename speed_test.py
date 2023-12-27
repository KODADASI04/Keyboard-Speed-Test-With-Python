import constants
import random
from Models.word import Word
from Models.competitor import Competitor
import time
from inputimeout import inputimeout, TimeoutOccurred
        
def createAppendWord(word,competitor,timeout):
    print(word)
    get_word = inputimeout(prompt = "Yukarıdaki Kelimeyi Girin : " , timeout = timeout)
    word_obj = Word(word)
    competitor.written_words.append(word_obj)
    word_obj.calculate_score(get_word)

def getWrittenWords(competitor):
    with open(f"{constants.PATH}/all_words.txt") as file:
        words = file.readlines()
        timeout = time.time() + 60
        countDown(competitor)
        while True:
            remain_time = timeout - time.time()
            random_word = words[random.randint(0,len(words))].strip("\n")
            if " " in random_word:
                random_words = random_word.split(" ")
                for seperate_word in random_words:
                    try:
                        createAppendWord(seperate_word,competitor,remain_time)
                    except TimeoutOccurred:
                        print("\nYour Time is Over\n")
                        break
            else:
                try:
                    createAppendWord(random_word,competitor,remain_time)
                except TimeoutOccurred:
                    print("\nYour Time is Over\n")
                    break

def calculateScores(competitor):
    competitor.total_score = sum([wrd.score for wrd in competitor.written_words])
    competitor.total_written_charc = sum([word.written_char_count for word in competitor.written_words])
    competitor.wrong_written_charc = sum([word.wrongchar_count for word in competitor.written_words])
    competitor.wrong_writtens = list(filter(lambda word : word.wrongwritten,competitor.written_words))
    
def printResults(competitor):
    print(f"\n{competitor.name}'in Sonuçları: ")
    print(f"Toplam Skorunuz: {competitor.total_score}")
    print(f"Toplam Yazdığınız Kelime Sayısı: {len(competitor.written_words)}")
    print(f"Toplam Yanlış Yazdığınız Kelime Sayısı: {len(competitor.wrong_writtens)}")
    print(f"Toplam Tıklama Sayınız: {competitor.total_written_charc}")
    print(f"Toplam Yanlış Tıklama Sayınız: {competitor.wrong_written_charc}")    

def showResult(competitor1,competitor2 = None):
    calculateScores(competitor1)
    printResults(competitor1)
    
    if competitor2 != None:
        calculateScores(competitor2)
        printResults(competitor2)
        compareCompetitors(competitor1,competitor2)
        
def compareCompetitors(competitor1,competitor2):
    print("\n VE KAZANAN...")
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)
        
    if competitor1.total_score > competitor2.total_score:
        print(f"\n\n{competitor1.name}")
    elif competitor1.total_score < competitor2.total_score:
        print(f"\n\n{competitor2.name}")
    else:
        print(f"Berabere Kaldınız")

def countDown(competitor):
    print(f"\nŞimdi {competitor.name}'in Sırası")
    input("Hazır Olduğunuzda Enter'a Basınız...")
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    print("Hadi Başlayalım \n")

def startSpeedTest():
    competition_type = input("Tek Kişi Oynamak İçin T'ye, İki Kişi Oynamak İçin I'ya basınız ")
    if competition_type.upper() == "T":
        competitor1 = Competitor()
        name1 = input("İsminizi Yazınız: ")
        competitor1.name = name1
        getWrittenWords(competitor1)
        showResult(competitor1)
        
    elif competition_type.upper() == "I":
        competitor1 = Competitor()
        competitor2 = Competitor()
        name1 = input("Birinci Oyuncunun İsmini Yazınız: ")
        name2 = input("İkinci Oyuncunun İsmini Yazınız: ")
        competitor1.name = name1
        competitor2.name = name2
        getWrittenWords(competitor1)
        getWrittenWords(competitor2)
        showResult(competitor1,competitor2)

startSpeedTest()


