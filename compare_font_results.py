import os


def get_files(path):
    for _file in os.listdir(path):
        if os.path.isfile(os.path.join(path, _file)) and _file.endswith('.ttf'):
            yield _file


lorem_ipsum = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...|{}"
index = 1
for file in get_files(r'.\\fonts'):
    myFile = open("compare_fonts_input.csv", "w")
    myFile.write(lorem_ipsum.format(file))
    myFile.close()
    os.system(
        "generator.py -csv compare_fonts_input.csv -img compare_fonts_background.png -out comparison_output -font "
        "\"./fonts/{}\" -bbox 200,200,880,880 -col #ffffff -iline 1.2 -prefix {}".format(file, index))
    index += 1
