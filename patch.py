import os
import requests
import zipfile
import io
import shutil

# copy fonts due to upstream changes in the repo
shutil.copytree("Extras", "Ligaturizer/fonts/fira/distr/otf", dirs_exist_ok=True)

# URL of the latest release
url = "https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip"

# Send HTTP request to the URL
response = requests.get(url)

# Make sure the request was successful
assert response.status_code == 200

# Open the zip file in memory
zip_file = zipfile.ZipFile(io.BytesIO(response.content))

# Extract the zip file
zip_file.extractall("FontPatcher")

# list all files in the current directory
files = os.listdir('Original')
# change root dir to Ligaturizer
os.chdir('Ligaturizer')

os.makedirs("../Ligaturized", exist_ok=True)

for file in files:
    if file == ".gitkeep":
        continue

    os.system(
        f'fontforge -lang py -script ligaturize.py "../Original/{file}" --output-dir="../Ligaturized/" --output-name="{file.replace("b.ttf","").replace("i.ttf","").replace("z.ttf","").replace(".ttf","")}"'
    )

os.chdir("../FontPatcher")
files = os.listdir('../Ligaturized')
os.makedirs("../Output", exist_ok=True)
for file in files:
    os.system(
        f'fontforge -script font-patcher "../Ligaturized/{file}" --out "../Output/" --complete'
    )
