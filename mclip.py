#! /usr/bin/python3
# mclip.py - a multi clip board program.

TEXT = {'agree':'Yes, i agree thanks whatever.','busy':'so sorry cant come too busy.',
        'upsell':'gis more money please'}

import sys,pyperclip
if len(sys.argv)<2:
    print("Usage: python mclip.py [keyphrase] - copy paste text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print('There is no text for '+keyphrase)
