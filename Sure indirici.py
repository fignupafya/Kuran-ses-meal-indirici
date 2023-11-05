import threading
import requests
import os
from time import sleep
from pydub import AudioSegment

sureler = [
    ["Fâtiha", "05-fatiha"],
    ["Bakara", "87-bakara"],
    ["Âl-i İmrân", "89-aliimran"],
    ["Nisâ", "92-nisa"],
    ["Mâide", "s112-maide"],
    ["En'âm", "55-enam"],
    ["A'râf", "39-araf"],
    ["Enfâl", "88-enfal"],
    ["Tevbe", "s113-tevbe"],
    ["Yûnus", "51-yunus"],
    ["Hûd", "52-hud"],
    ["Yûsuf", "53-yusuf"],
    ["Ra'd", "96-rad"],
    ["İbrâhîm", "72-ibrahim"],
    ["Hicr", "54-hicr"],
    ["Nahl", "70-nahl"],
    ["İsrâ", "50-isra"],
    ["Kehf", "69-kehf"],
    ["Meryem", "44-meryem"],
    ["Tâhâ", "45-taha"],
    ["Enbiyâ", "73-enbiya"],
    ["Hac", "s103-hac"],
    ["Mü'minûn", "74-muminun"],
    ["Nûr", "s102-nur"],
    ["Furkân", "42-furkan"],
    ["Şuarâ", "47-suara"],
    ["Neml", "48-neml"],
    ["Kasas", "49-kasas"],
    ["Ankebût", "85-ankebut"],
    ["Rûm", "84-rum"],
    ["Lokmân", "57-lokman"],
    ["Secde", "75-secde"],
    ["Ahzâb", "90-ahzab"],
    ["Sebe'", "58-sebe"],
    ["Fâtır", "43-fatir"],
    ["Yâsîn", "41-yasin"],
    ["Sâffât", "56-saffat"],
    ["Sâd", "38-sad"],
    ["Zümer", "59-zumer"],
    ["Mü'min", "60-mumin"],
    ["Fussilet", "61-fussilet"],
    ["Şûrâ", "62-sura"],
    ["Zuhruf", "63-zuhruf"],
    ["Duhân", "64-duhan"],
    ["Câsiye", "65-casiye"],
    ["Ahkâf", "66-ahkaf"],
    ["Muhammed", "95-muhammed"],
    ["Fetih", "s111-fetih"],
    ["Hucurât", "s106-hucurat"],
    ["Kâf", "18-kafirun"],
    ["Zâriyât", "67-zariyat"],
    ["Tûr", "76-tur"],
    ["Necm", "23-necm"],
    ["Kamer", "37-kamer"],
    ["Rahmân", "97-rahman"],
    ["Vâkıa", "46-vakia"],
    ["Hadîd", "94-hadid"],
    ["Mücâdele", "s105-mucadele"],
    ["Haşr", "s101-hasr"],
    ["Mümtehine", "91-mumtehine"],
    ["Saff", "56-saffat"],
    ["Cuma", "s110-cuma"],
    ["Münâfikûn", "s104-munafikun"],
    ["Tegâbün", "s108-tegabun"],
    ["Talâk", "s99-talak"],
    ["Tahrîm", "s107-tahrim"],
    ["Mülk", "77-mulk"],
    ["Kalem", "02-kalem"],
    ["Hâkka", "78-hakka"],
    ["Meâric", "79-mearic"],
    ["Nûh", "71-nuh"],
    ["Cin", "40-cin"],
    ["Müzzemmil", "03-muzzemmil"],
    ["Müddessir", "04-muddessir"],
    ["Kıyâmet", "31-kiyamet"],
    ["İnsân", "98-insan"],
    ["Mürselât", "33-murselat"],
    ["Nebe", "80-nebe"],
    ["Naziât", "81-naziat"],
    ["Abese", "24-abese"],
    ["Tekvîr", "07-tekvir"],
    ["İnfitâr", "82-infitar"],
    ["Mutaffifîn", "86-mutaffifin"],
    ["İnşikâk", "83-insikak"],
    ["Burûc", "27-buruc"],
    ["Târık", "36-tarik"],
    ["A'lâ", "01-alak"],
    ["Gâşiye", "68-gasiye"],
    ["Fecr", "10-fecr"],
    ["Beled", "35-beled"],
    ["Şems", "26-sems"],
    ["Leyl", "09-leyl"],
    ["Duhâ", "11-duha"],
    ["İnşirâh", "12-insirah"],
    ["Tîn", "28-tin"],
    ["Alak", "01-alak"],
    ["Kadir", "25-kadir"],
    ["Beyyine", "s100-beyyine"],
    ["Zilzâl", "93-zilzal"],
    ["Âdiyât", "14-adiyat"],
    ["Kâria", "30-karia"],
    ["Tekâsür", "16-tekasur"],
    ["Asr", "13-asr"],
    ["Hümeze", "32-humeze"],
    ["Fîl", "19-fil"],
    ["Kureyş", "29-kureys"],
    ["Maûn", "17-maun"],
    ["Kevser", "15-kevser"],
    ["Kâfirûn", "18-kafirun"],
    ["Nasr", "s114-nasr"],
    ["Tebbet", "06-tebbet"],
    ["İhlâs", "22-ihlas"],
    ["Felak", "20-felak"],
    ["Nâs", "21-nas"]
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
while True:
    secim2 = input("Kuran için k\nMeali için m\nKuran ve meal için km yazınız: ").lower().strip()
    if secim2 != "k" and secim2 != "m" and secim2 != "km" and secim2 != "mk":
        print(f"Yanlış yazdınız: {secim2}")
    else:
        if "k" in secim2:
            parcaseslerisil = False if input(
                "Ayetleri ayrı ayrı indirmek isterseniz E yazınız: ").lower().strip() == "e" else True
        break


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


def meal_indir(surenumarasi):
    url = f"{meal_base_url}{sureler[surenumarasi][1]}.mp3"
    file_name = f"{sureler[surenumarasi][0]} Suresi Meali.mp3"
    file_path = os.path.join(output_directory, file_name)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
            print(f"-> {os.path.basename(file_path)} indirildi")
            return True


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
                    meal_indir(surenumarasi)
                end = True
            else:
                print(f"Yanlış numara girdiniz: {i}")
        else:
            if i.strip() != "":
                print(f"\nYanlış girdi girdiniz: {i}")

    if end:
        input("\n->Çıkmak için enter'a basınız")
