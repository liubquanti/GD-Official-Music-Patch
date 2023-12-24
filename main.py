import requests
import os
import shutil
import time

def завантажити_файл(url, назва_файлу):
    response = requests.get(url)
    if response.status_code == 200:
        with open(назва_файлу, 'wb') as file:
            file.write(response.content)
        os.system('cls')
        print(f">>> GD Official Music Patch")
        print(f">>> White Heart Dev / Oleh Liubchenko")
        print(f"")
        print(f">>> {назва_файлу} / Завантажено успішно.")
        return назва_файлу
    else:
        print(f">>> {назва_файлу} / Не завантажено.")
        return None

urls = [
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/Meltdown/AirborneRobots.mp3', 'AirborneRobots.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/Meltdown/The7Seas.mp3', 'The7Seas.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/Meltdown/VikingArena.mp3', 'VikingArena.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/SubZero/PowerTrip.mp3', 'PowerTrip.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/SubZero/PressStart.mp3', 'PressStart.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/SubZero/knockemout.mp3', 'knockemout.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/BeastMode.mp3', 'BeastMode.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/ElectroFrontlines.mp3', 'ElectroFrontlines.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/Embers.mp3', 'Embers.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/Machina.mp3', 'Machina.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/MonsterDanceOff.mp3', 'MonsterDanceOff.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/Payload.mp3', 'Payload.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/Round1.mp3', 'Round1.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/SpacePirates.mp3', 'SpacePirates.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/Striker.mp3', 'Striker.mp3'),
    ('https://github.com/liubquanti-dev/GD-Official-Music-Patch/raw/main/Music/World/Years.mp3', 'Years.mp3'),
]

завантажені_файли = []
for url, назва_файлу in urls:
    завантажений_файл = завантажити_файл(url, назва_файлу)
    if завантажений_файл:
        завантажені_файли.append(завантажений_файл)

шлях_до_папки_SteamLibrary = None

диски = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']

for диск in диски:
    можливий_шлях_до_ресурсів = os.path.join(диск, 'SteamLibrary', 'steamapps', 'common', 'Geometry Dash', 'Resources')
    if os.path.exists(можливий_шлях_до_ресурсів):
        шлях_до_папки_SteamLibrary = можливий_шлях_до_ресурсів
        os.system('cls')
        print(f">>> GD Official Music Patch")
        print(f">>> White Heart Dev / Oleh Liubchenko")
        print(f"")
        print(f">>> {можливий_шлях_до_ресурсів} / Визначено.")
        time.sleep(2.0)
        break

if not шлях_до_папки_SteamLibrary:
    можливий_шлях_до_ресурсів = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Geometry Dash\\Resources'
    if os.path.exists(можливий_шлях_до_ресурсів):
        шлях_до_папки_SteamLibrary = можливий_шлях_до_ресурсів
        os.system('cls')
        print(f">>> GD Official Music Patch")
        print(f">>> White Heart Dev / Oleh Liubchenko")
        print(f"")
        print(f">>> {можливий_шлях_до_ресурсів} / Визначено.")
        time.sleep(2.0)

if шлях_до_папки_SteamLibrary:
    for назва_файлу in завантажені_файли:
        шлях_до_файлу = os.path.join(os.getcwd(), назва_файлу)
        if os.path.exists(шлях_до_файлу):
            shutil.copy(шлях_до_файлу, шлях_до_папки_SteamLibrary)
            os.system('cls')
            print(f">>> GD Official Music Patch")
            print(f">>> White Heart Dev / Oleh Liubchenko")
            print(f"")
            print(f">>> {назва_файлу} / Скопійовано.")
            time.sleep(0.5)
            os.remove(шлях_до_файлу)
            print(f">>> {назва_файлу} / Видалено.")
            time.sleep(0.5)
        else:
            os.system('cls')
            print(f">>> GD Official Music Patch")
            print(f">>> White Heart Dev / Oleh Liubchenko")
            print(f"")
            print(f">>> {назва_файлу} / Не знайдено.")
            time.sleep(0.5)
        os.system('cls')
    print(f">>> GD Official Music Patch")
    print(f">>> White Heart Dev / Oleh Liubchenko")
    print(f"")
    print(f">>> Патч виконано.")
    time.sleep(2.0)
    os.system('cls')
    print(f">>> GD Official Music Patch")
    print(f">>> White Heart Dev / Oleh Liubchenko")
    print(f"")
    print(f">>> Завершення програми.")
    time.sleep(2.0)
else:
    os.system('cls')
    print(f">>> GD Official Music Patch")
    print(f">>> White Heart Dev / Oleh Liubchenko")
    print(f"")
    print(">>> Не вдалося знайти папку SteamLibrary на жодному з дисків.")
    time.sleep(0.5)
    for назва_файлу in завантажені_файли:
        шлях_до_файлу = os.path.join(os.getcwd(), назва_файлу)
        if os.path.exists(шлях_до_файлу):
            os.remove(шлях_до_файлу)
            os.system('cls')
            print(f">>> GD Official Music Patch")
            print(f">>> White Heart Dev / Oleh Liubchenko")
            print(f"")
            print(f">>> {назва_файлу} / Видалено.")
    os.system('cls')
    print(f">>> GD Official Music Patch")
    print(f">>> White Heart Dev / Oleh Liubchenko")
    print(f"")
    print(f">>> Патч не виконано.")
    time.sleep(2.0)
    os.system('cls')
    print(f">>> GD Official Music Patch")
    print(f">>> White Heart Dev / Oleh Liubchenko")
    print(f"")
    print(f">>> Завершення програми.")
    time.sleep(2.0)
