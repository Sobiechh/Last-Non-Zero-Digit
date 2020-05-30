import glob  # sciezki do plikow
import pandas as pd  # wyswietlenie na stronie
import datetime as dt #pandas
import os #odpalanie
import last_zero

files_path = "in/*.txt"  # sciezka do plikow in
files_path2 = "out/*.txt"  # sciezka plikow out

files_in = glob.glob(files_path)
files_out = glob.glob(files_path2)

in_stuff =[] #in pliki
out_stuff = [] #out pliki

for name in files_in: #lecimy po in
    with open(name) as f:
        word = f.readlines()
        word = [x.strip() for x in word] #potrzebny strip, poniewaz bralo \n
        in_stuff.append(word) #wypisanie danych do in_stuff
        f.close()

for name in files_out:
    with open(name) as f:
        word = f.readlines() #wypisanie danych do out_stuff
        word = [x.strip() for x in word] #potrzebny strip, poniewaz bralo \n
        out_stuff.append(word)
        f.close()

s="," #separator

flat_in_list = [] #mam [[plik1], [plik2] itd], chce ['plik1', 'plik2'] itd
for list in in_stuff:
    flat_in_list.append(s.join(list))

flat_out_list = [] #mam [[plik1], [plik2] itd], chce ['plik1', 'plik2'] itd
for list in out_stuff:
    flat_out_list.append(s.join(list))

data_frame = pd.DataFrame({ #uzycie biblioteki pandas do wyseietlenia na stronie
    'input' : flat_in_list,
    'output' : flat_out_list,
    'input created': last_zero.time_in,
    'output created': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
})

pd.set_option('colheader_justify', 'center') #wycentrowanie

#poczatek HTML, wpisuje tytul html, dodaje styl css
html_string ='''
<html>
  <head><title> LastNonZeroDigit {data} </title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  <body>
    <h1> BACKUP {data} </h1>
    {table}
  </body>
</html>.
'''

#wykorzystanie datatime
file_name= dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+".html"

# OUTPUT HTML
with open('backup\\'+file_name, "w") as f: #utworzenie backupu pliku html
    f.write(html_string.format(data= dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), table=data_frame.to_html(classes='mystyle')))

os.startfile('backup\\'+file_name) #otwierania pliku