# bulk-quotes-instagram-generator
Python script to bulk generate posts with quotes on Instagram

## Usage
```
usage: generator.py [-h] [-csv CSV] [-img IMG] [-out OUT] [-font FONT]
                    [-bbox BBOX] [-col COL] [-iline ILINE]

Arguments for generator

optional arguments:
  -h, --help    show this help message and exit
  -csv CSV      CSV files with the list of quotes and authors in format
                QUOTE|AUTHOR (default: None)
  -img IMG      Background image file (default: None)
  -out OUT      Output dir (default: None)
  -font FONT    Font used to write quotes (default: None)
  -bbox BBOX    Bounding box coordinates in format
                top_left_x,top_left_y,bottom_right_x, bottom_right_y (default:
                None)
  -col COL      Text color in RGB format (#RRGGBB) (default: None)
  -iline ILINE  Interline (default: None)
```

