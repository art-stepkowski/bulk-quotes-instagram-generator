import argparse
import csv
import textwrap
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Parse arguments
parser = argparse.ArgumentParser(description = "Arguments for generator",
                                 formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-csv", help = "CSV files with the list of quotes and authors in format QUOTE|AUTHOR")
parser.add_argument("-img", help = "Background image file")
parser.add_argument("-out", help = "Output dir")
parser.add_argument("-font", help = "Font used to write quotes")
parser.add_argument("-bbox", help = "Bounding box coordinates in format top_left_x,top_left_y,bottom_right_x, bottom_right_y")
parser.add_argument("-col", help = "Text color in RGB format (#RRGGBB)")
parser.add_argument("-iline", help = "Interline")
args = parser.parse_args()
config = vars(args)

# Parse bounding box
bbox = [int(e) for e in config.get("bbox").split(',')]
bbox_width = bbox[2] - bbox[0]
bbox_height = bbox[3] - bbox[1]

fill_color = config.get("col")
index = 1

# Create directory if not exists
output_dir = config.get("out")
isExist = os.path.exists(output_dir)

if not isExist:
    os.makedirs(output_dir)
    print("Output directory is created!")


def calculate_font_size(_row, _font):
    global font_size
    if font_size < 30:
        print("Text to large: " + row[0])
        return False, None, None, None, None, None, None, None, None
    _quote_font = ImageFont.truetype(_font, font_size)
    _author_font = ImageFont.truetype(_font, int(font_size * 0.6))
    _quote_w, quote_h = draw.textsize(_row[0], font = _quote_font)
    _author_w, _author_h = draw.textsize(_row[1], font = _author_font)
    ppc = _quote_w / len(_row[0])
    _para = textwrap.wrap(_row[0], width = int(bbox_width / ppc))
    _pad = int(quote_h * float(config.get("iline")))
    _text_height = (len(_para) + 1) * _pad + 20 + _author_h
    if _text_height > bbox_height:
        font_size -= 1
        return calculate_font_size(_row, _font)
    return True, _quote_font, _author_font, _text_height, _para, _pad, _author_w, _author_h, _quote_w


with open(config.get("csv")) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '|')
    for row in csv_reader:
        img = Image.open(config.get("img"))
        draw = ImageDraw.Draw(img)
        font_size = 45
        is_ok, quote_font, author_font, text_height, para, pad, author_w, author_h, quote_w = calculate_font_size(row,
                                                                                                           config.get("font"))
        if is_ok:
            current_h = bbox[1] + (bbox_height - text_height) / 2
            for line in para:
                line_w, line_h = draw.textsize(line, font = quote_font)
                x = bbox[0] + (bbox_width - line_w) / 2
                draw.text((x, current_h), line, font = quote_font, fill = fill_color)
                current_h += pad
            lw = int(bbox_width * 0.5)
            current_h += 20
            draw.line((bbox[0] + (bbox_width - lw) / 2, current_h, bbox[0] + (bbox_width - lw) / 2 + lw, current_h),
                      fill = fill_color)
            x = bbox[0] + (bbox_width - author_w) / 2
            draw.text((x, current_h + author_h), row[1], font = author_font, fill = fill_color)
            img.save(output_dir + "/" + str(index) + ".png")
            index += 1
