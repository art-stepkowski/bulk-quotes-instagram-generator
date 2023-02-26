import argparse
import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

parser = argparse.ArgumentParser(description = "Arguments for generator",
                                 formatter_class = argparse.ArgumentDefaultsHelpFormatter)
# csv file
# image
# output dir

parser.add_argument("-csv", help = "CSV files with the list of quotes and authors in format QUOTE,AUTHOR")
parser.add_argument("-img", help = "Background image file")
parser.add_argument("-out", help = "Output dir")
parser.add_argument("-font", help = "Font used to write quotes")
parser.add_argument("-bbox", help = "Bounding box coordinates in format top_left_x,top_left_y,bottom_right_x, bottom_right_y")
parser.add_argument("-col", help = "Text color in RGB format (#RRGGBB)")
args = parser.parse_args()
config = vars(args)
bbox = [int(e) for e in config.get("bbox").split(',')]
myFont = ImageFont.truetype(config.get("font"), 50)
with open(config.get("csv")) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        img = Image.open(config.get("img"))
        draw = ImageDraw.Draw(img)
        draw.text((bbox[0], bbox[1]), row[0], font = myFont, fill = config.get("col"))
        img.show()
