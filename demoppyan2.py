from flask import Flask, request, url_for
from date_intrare_proiect import *
import functiilib

# Logging - utilizare pachet logging

app = Flask(__name__)

# Pagina Principala
@app.route('/')
def index():
    ret = "<h1>Exemplu Proiect Python Pentru Studentii din anul II</h1>"
    
    ret += "<a href=" + url_for("salut") + ">Salut</a>"
    
    return ret

# Exemple de apel cu parte variabila de URL si parametrii in URL
#  - methoda HTTP GET
# URL-uri care folosesc aceasta ruta:
# http://127.0.0.1:5000/salut
# http://127.0.0.1:5000/salut/
# http://127.0.0.1:5000/salut/Ciprian?extrainfo=BUNA&extrainfo2=CeMaiFaci
#
# Exercitiu - eliminat unii decoratori: /salut, /salut/ si de vazut ce se intampla
#
# Ex. Comentez: #@app.route('/salut/')    
#
# La URL-ul: http://127.0.0.1:5000/salut/
# raspunsul este:
# 
# Not Found
# The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
#
# Daca las decoratorul de mai sus decomentat - nu mai apare acest mesaj, oarecum neasteptat

# Ruta cu parametrii
@app.route('/salut')
@app.route('/salut/')    
@app.route('/salut/<nume>')
def salut(nume=""):
    ret = f"<a href={url_for('index')}>Acasa</a><br/>"
    ret += "1) Scrieti un nume in URL si dati ENTER<br/>"
    ret += "2) Scrieti un nume si apoi dati niste parametrii ca in exemplul: http://127.0.0.1:5000/salut/Ciprian?extrainfo=BUNA&extrainfo2=CeMaiFaci<br/><br/>"
    

    # ACCESS variabila 'request' - care contine informatii despre cererea trimisa catre server
    extra1 = request.args.get('extrainfo')
    extra2 = request.args.get('extrainfo2')
    
    # DEBUG - mesaje in consola
    print(extra1)
    print(extra2)
    
    print(request.url)
    print(request.base_url)
    print(request.host)
    
    # Tratare erori - daca extra1 sau extra2 sunt None - sa nu se mai afiseze in pagina WEB
    ret += f"<h1>Salut -{nume}- {extra1} {extra2}</h1>"
    
    return ret

# URL care va folosi aceasta ruta: http://127.0.0.1:5000/dateintrare
# Afisare date de intrare    
@app.route('/dateintrare')
def afisare_date_intrare():
    ret = "<pre>"
    
    ret += "sir_cchende = "
    ret += sir_cchende
    
    ret += "\nlst_cchende = "
    ret += str(lst_cchende)
    
    ret += "\ndict_cchende = "
    ret += str(dict_cchende)    
    
    ret += "</pre>"
    
    return ret


# URL care va folosi aceasta ruta: http://127.0.0.1:5000/dict_nume
# Afisare nume din dictionar    
@app.route('/dict_nume')
def nume_dict():
    return functiilib.ia_nume_din_dict()

if __name__ == "__main__":
    app.run(debug=1)
