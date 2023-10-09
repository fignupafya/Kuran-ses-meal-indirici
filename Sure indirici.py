import requests
import os
from time import sleep
from pydub import AudioSegment


sureler = """
Fâtiha
Bakara
Âl-i İmrân
Nisâ
Mâide
En'âm
A'râf
Enfâl
Tevbe
Yûnus
Hûd
Yûsuf
Ra'd
İbrâhîm
Hicr
Nahl
İsrâ
Kehf
Meryem
Tâhâ
Enbiyâ
Hac
Mü'minûn
Nûr
Furkân
Şuarâ
Neml
Kasas
Ankebût
Rûm
Lokmân
Secde
Ahzâb
Sebe'
Fâtır
Yâsîn
Sâffât
Sâd
Zümer
Mü'min
Fussilet
Şûrâ
Zuhruf
Duhân
Câsiye
Ahkâf
Muhammed
Fetih
Hucurât
Kâf
Zâriyât
Tûr
Necm
Kamer
Rahmân
Vâkıa
Hadîd
Mücâdele
Haşr
Mümtehine
Saff
Cuma
Münâfikûn
Tegâbün
Talâk
Tahrîm
Mülk
Kalem
Hâkka
Meâric
Nûh
Cin
Müzzemmil
Müddessir
Kıyâmet
İnsân
Mürselât
Nebe
Naziât
Abese
Tekvîr
İnfitâr
Mutaffifîn
İnşikâk
Burûc
Târık
A'lâ
Gâşiye
Fecr
Beled
Şems
Leyl
Duhâ
İnşirâh
Tîn
Alak
Kadir
Beyyine
Zilzâl
Âdiyât
Kâria
Tekâsür
Asr
Hümeze
Fîl
Kureyş
Maûn
Kevser
Kâfirûn
Nasr
Tebbet
İhlâs
Felak
Nâs""".splitlines()

base_url = "https://webdosya.diyanet.gov.tr/kuran/kuranikerim/Sound/ar_osmanSahin/"
Desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

secim = input("Indirilecek sure numarası girin veya menu yazarak sure numaralarını görüntüleyin: ")
if secim.lower().strip() == "menu" or secim.lower().strip() == "menü":
    for i in range(1,len(sureler)):
        print(f"{i}-{sureler[i]}")
    print()
    surenumarasi = int(input("Sure numarası: "))
else:
    surenumarasi = int(secim)

sureismi = sureler[surenumarasi]

TEMP_output_directory = os.path.join(Desktop_path, f"{sureismi}_TEMP")
output_directory = Desktop_path



if not os.path.exists(TEMP_output_directory):
    os.makedirs(TEMP_output_directory)

keepdownloading = True
i = 0
while (keepdownloading):
    url = f"{base_url}{surenumarasi}_{i}.mp3"

    # Send an HTTP GET request to the URL
    response = requests.get(url)
    sleep(0.2)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Create the file name for the downloaded MP3 file
        file_name = f"{sureismi}_{i}.mp3"

        # Specify the full path to save the file
        file_path = os.path.join(TEMP_output_directory, file_name)

        # Save the content to the specified directory
        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"{file_name} indirildi")
        i+=1
    else:
        if response.status_code == 404:
            print("İndirme tamamlandı")
        else:
            print(f"Failed to download {url} - Status code: {response.status_code}")
        keepdownloading = False



print("\n\nKayıtlar birleştiriliyor\n")

merged_audio = AudioSegment.empty()

for a in range(0,i):
    file_name = f"{sureismi}_{a}.mp3"
    mp3_path = os.path.join(TEMP_output_directory, file_name)
    audio_segment = AudioSegment.from_mp3(mp3_path)
    merged_audio += audio_segment
    os.remove(mp3_path)

os.rmdir(TEMP_output_directory)
outfilename=f"{sureismi}.mp3"
output_file = os.path.join(output_directory, outfilename)
merged_audio.export(output_file, format='mp3')


print(f'Işlem tamamlandı -> {outfilename}')
