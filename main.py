import requests
import os
import shutil

def завантажити_файл(url, назва_файлу):
    response = requests.get(url)
    if response.status_code == 200:
        with open(назва_файлу, 'wb') as file:
            file.write(response.content)
        print(f"Файл {назва_файлу} завантажено успішно.")
        return назва_файлу
    else:
        print(f"Не вдалося завантажити файл {назва_файлу}.")
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
    поточний_шлях = f"{диск}\\SteamLibrary\\steamapps\\common\\Geometry Dash\\Resources"
    if os.path.exists(поточний_шлях):
        шлях_до_папки_SteamLibrary = поточний_шлях
        break

if шлях_до_папки_SteamLibrary:
    for назва_файлу in завантажені_файли:
        шлях_до_файлу = os.path.join(os.getcwd(), назва_файлу)
        if os.path.exists(шлях_до_файлу):
            shutil.copy(шлях_до_файлу, шлях_до_папки_SteamLibrary)
            print(f"Файл {назва_файлу} скопійовано до папки SteamLibrary.")
            os.remove(шлях_до_файлу)
            print(f"Файл {назва_файлу} видалено.")
        else:
            print(f"Не вдалося знайти файл {назва_файлу} для копіювання.")
else:
    print("Не вдалося знайти папку SteamLibrary на жодному з дисків.")
