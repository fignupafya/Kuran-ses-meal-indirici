import threading
import requests
import os
from pydub import AudioSegment
import json

sureler = [
    ["Fâtiha", "05-fatiha", 0],
    ["Bakara", "87-bakara", 1],
    ["Âl-i İmrân", "89-aliimran", 49],
    ["Nisâ", "92-nisa", 76],
    ["Mâide", "s112-maide", 105],
    ["En'âm", "55-enam", 127],
    ["A'râf", "39-araf", 150],
    ["Enfâl", "88-enfal", 176],
    ["Tevbe", "s113-tevbe", 186],
    ["Yûnus", "51-yunus", 207],
    ["Hûd", "52-hud", 220],
    ["Yûsuf", "53-yusuf", 234],
    ["Ra'd", "96-rad", 248],
    ["İbrâhîm", "72-ibrahim", 254],
    ["Hicr", "54-hicr", 261],
    ["Nahl", "70-nahl", 266],
    ["İsrâ", "50-isra", 281],
    ["Kehf", "69-kehf", 292],
    ["Meryem", "44-meryem", 304],
    ["Tâhâ", "45-taha", 311],
    ["Enbiyâ", "73-enbiya", 321],
    ["Hac", "s103-hac", 331],
    ["Mü'minûn", "74-muminun", 341],
    ["Nûr", "s102-nur", 349],
    ["Furkân", "42-furkan", 358],
    ["Şuarâ", "47-suara", 366],
    ["Neml", "48-neml", 376],
    ["Kasas", "49-kasas", 384],
    ["Ankebût", "85-ankebut", 395],
    ["Rûm", "84-rum", 403],
    ["Lokmân", "57-lokman", 410],
    ["Secde", "75-secde", 414],
    ["Ahzâb", "90-ahzab", 417],
    ["Sebe'", "58-sebe", 427],
    ["Fâtır", "43-fatir", 433],
    ["Yâsîn", "41-yasin", 439],
    ["Sâffât", "56-saffat", 445],
    ["Sâd", "38-sad", 452],
    ["Zü39-2mer", "59-zumer", 457],
    ["Mü'min", "60-mumin", 466],
    ["Fussilet", "61-fussilet", 476],
    ["Şûrâ", "62-sura", 482],
    ["Zuhruf", "63-zuhruf", 488],
    ["Duhân", "64-duhan", 495],
    ["Câsiye", "65-casiye", 498],
    ["Ahkâf", "66-ahkaf", 501],
    ["Muhammed", "95-muhammed", 506],
    ["Fetih", "s111-fetih", 510],
    ["Hucurât", "s106-hucurat", 514],
    ["Kâf", "18-kafirun", 517],
    ["Zâriyât", "67-zariyat", 519],
    ["Tûr", "76-tur", 522],
    ["Necm", "23-necm", 525],
    ["Kamer", "37-kamer", 527],
    ["Rahmân", "97-rahman", 530],
    ["Vâkıa", "46-vakia", 533],
    ["Hadîd", "94-hadid", 536],
    ["Mücâdele", "s105-mucadele", 541],
    ["Haşr", "s101-hasr", 544],
    ["Mümtehine", "91-mumtehine", 548],
    ["Saff", "56-saffat", 550],
    ["Cuma", "s110-cuma", 552],
    ["Münâfikûn", "s104-munafikun", 553],
    ["Tegâbün", "s108-tegabun", 555],
    ["Talâk", "s99-talak", 557],
    ["Tahrîm", "s107-tahrim", 559],
    ["Mülk", "77-mulk", 561],
    ["Kalem", "02-kalem", 563],
    ["Hâkka", "78-hakka", 565],
    ["Meâric", "79-mearic", 567],
    ["Nûh", "71-nuh", 569],
    ["Cin", "40-cin", 571],
    ["Müzzemmil", "03-muzzemmil", 573],
    ["Müddessir", "04-muddessir", 574],
    ["Kıyâmet", "31-kiyamet", 576],
    ["İnsân", "98-insan", 577],
    ["Mürselât", "33-murselat", 579],
    ["Nebe", "80-nebe", 581],
    ["Naziât", "81-naziat", 582],
    ["Abese", "24-abese", 584],
    ["Tekvîr", "07-tekvir", 585],
    ["İnfitâr", "82-infitar", 586],
    ["Mutaffifîn", "86-mutaffifin", 587],
    ["İnşikâk", "83-insikak", 588],
    ["Burûc", "27-buruc", 589],
    ["Târık", "36-tarik", 590],
    ["A'lâ", "01-alak", 591],
    ["Gâshiye", "68-gasiye", 591],
    ["Fecr", "10-fecr", 592],
    ["Beled", "35-beled", 593],
    ["Şems", "26-sems", 594],
    ["Leyl", "09-leyl", 595],
    ["Duhâ", "11-duha", 595],
    ["İnşirâh", "12-insirah", 596],
    ["Tîn", "28-tin", 596],
    ["Alak", "01-alak", 597],
    ["Kadir", "25-kadir", 598],
    ["Beyyine", "s100-beyyine", 598],
    ["Zilzâl", "93-zilzal", 599],
    ["Âdiyât", "14-adiyat", 599],
    ["Kâria", "30-karia", 600],
    ["Tekâsür", "16-tekasur", 600],
    ["Asr", "13-asr", 601],
    ["Hümeze", "32-humeze", 601],
    ["Fîl", "19-fil", 601],
    ["Kureyş", "29-kureys", 602],
    ["Maûn", "17-maun", 602],
    ["Kevser", "15-kevser", 602],
    ["Kâfirûn", "18-kafirun", 603],
    ["Nasr", "s114-nasr", 603],
    ["Tebbet", "06-tebbet", 603],
    ["İhlâs", "22-ihlas", 604],
    ["Felak", "20-felak", 604],
    ["Nâs", "21-nas", 604]
]

kuran_base_url = "https://webdosya.diyanet.gov.tr/kuran/kuranikerim/Sound/ar_osmanSahin/"
meal_base_url = "https://ia601904.us.archive.org/22/items/INDIRILIS_SIRASINA_GORE_SESLI_KURAN_MEALI/"
Desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
output_directory = Desktop_path
parcaseslerisil = True
index = 0
topnum = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
}
notcompletedyet = []



# MENU
secim2 = input("Kuran için k\nMeali için m\nKuran ve meal için km yazınız: ").lower().strip()
while secim2 != "k" and secim2 != "m" and secim2 != "km" and secim2 != "mk":
    print(f"Yanlış yazdınız: {secim2}")

if "k" in secim2:
    parcaseslerisil = False if input(
        "Ayetleri ayrı ayrı indirmek isterseniz E yazınız: ").lower().strip() == "e" else True

if "m" in secim2:
    secim3 = input("\nMeali yazı olarak indirmek için y\nses olarak indirmek için s\nikisini de indirmek için  ys yazınız: ").lower().strip()
    while secim3 != "y" and secim3 != "s" and secim3 != "sy" and secim3 != "ys":
        print(f"Yanlış yazdınız: {secim3}")


def ayet_indir(sureismi, url="", file_path=""):
    global index
    global topnum
    index += 1
    iscompletion = False
    if index < 0:
        return False
    if url == "":
        url = f"{kuran_base_url}{surenumarasi + 1}_{index}.mp3"
        file_name = f"{sureismi}_{index}.mp3"
        file_path = os.path.join(TEMP_output_directory, file_name)
    else:
        iscompletion = True
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
                print(os.path.basename(file_path))
                if iscompletion:
                    notcompletedyet.remove([url, file_path])
                topnum+=1
                return True

        else:
            index = -10
            return False
    except:
        if [url, file_path] not in notcompletedyet:
            notcompletedyet.append([url, file_path])


def sesli_meal_indir(surenumarasi):
    url = f"{meal_base_url}{sureler[surenumarasi][1]}.mp3"
    file_name = f"{sureler[surenumarasi][0]} Suresi Meali.mp3"
    file_path = os.path.join(output_directory, file_name)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
            print(f"-> {os.path.basename(file_path)} indirildi")
            return True

def download_meal_text(surenum):
    pagenum=sureler[surenum][2]
    output_meal_arr=[]
    while (True):
        req = requests.get(f"https://kuran.diyanet.gov.tr/mushaf/qurandm/pagedata?id={pagenum}&ml=5&ql=7")
        if (req.status_code==200):
            data = json.loads(req.text)
            # python mantığı ne? nasıl çalışıyor?
            page_meals = [meal["AyetText"] for meal in data.get("MealAyats", []) if meal.get("SureId") == surenum+1]


            if page_meals == []:
                break
            else:
                pagenum+=1
                temparr=[]
                for i in page_meals:
                    if page_meals.count(i) == 1:
                        temparr.append(i)
                output_meal_arr.append(temparr)
        else:
            break

    sure_ismi = sureler[surenum][0]
    file_path = os.path.join(output_directory, f"{sure_ismi} Suresi Meali.txt")

    with open(file_path,"w",encoding="utf-8") as file:
        for index,meal_arr in enumerate(output_meal_arr):
            for meal_ayet in meal_arr:
                file.write(meal_ayet+"\n")
            file.write(f"-----{index+1}-----\n\n")
    print(f"Yazılı {sure_ismi} meali - indirildi")










def start_downloading(sureismi):
    print()

    global topnum
    topnum=0

    threads = []

    if not os.path.exists(TEMP_output_directory):
        os.makedirs(TEMP_output_directory)

    global index
    index = -1
    while index != -10:
        for i in range(0, 2):  # Adjust the number of threads as per your requirement
            thread = threading.Thread(target=ayet_indir, args=(sureismi,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    while len(notcompletedyet) != 0:
        for i in range(0, 2):  # Adjust the number of threads as per your requirement
            for data in notcompletedyet:
                thread = threading.Thread(target=ayet_indir, args=(sureismi, data[0], data[1]))
                threads.append(thread)
                thread.start()
        for thread in threads:
            thread.join()

    merged_audio = AudioSegment.empty()

    for a in range(0, topnum):
        file_name = f"{sureismi}_{a}.mp3"
        mp3path = os.path.join(TEMP_output_directory, file_name)
        audio_segment = AudioSegment.from_mp3(mp3path)
        merged_audio += audio_segment
        if parcaseslerisil:
            os.remove(mp3path)

    if parcaseslerisil:
        os.rmdir(TEMP_output_directory)
    else:
        os.rename(TEMP_output_directory, os.path.join(output_directory, f"{sureismi}"))
    outfilename = f"{sureismi}.mp3"
    output_file = os.path.join(output_directory, outfilename)
    merged_audio.export(output_file, format='mp3')

    print(f'-> {outfilename} indirildi')


end = False
while not end:

    secim = input("\nIndirilecek sure numarası/numaralarını girin veya \nmenu yazarak sure numaralarını görüntüleyin: ")
    for i in secim.split(" "):
        if i.lower().strip() == "menu" or i.lower().strip() == "menü":
            for k in range(0, len(sureler)):
                print(f"{k + 1}-{sureler[k][0]}")
            print()

        elif i.isdigit():

            surenumarasi = int(i) - 1
            if 114 >= surenumarasi >= 0:
                sureismi = sureler[surenumarasi][0]
                TEMP_output_directory = os.path.join(output_directory, f"{sureismi}_TEMP")
                if "k" in secim2:
                    start_downloading(sureismi)

                if "m" in secim2:
                    if "s" in secim3:
                        sesli_meal_indir(surenumarasi)
                    if "y" in secim3:
                        download_meal_text(surenumarasi)
                end = True
            else:
                print(f"Yanlış numara girdiniz: {i}")
        else:
            if i.strip() != "":
                print(f"\nYanlış girdi girdiniz: {i}")

    if end:
        input("\n->Çıkmak için enter'a basınız")
