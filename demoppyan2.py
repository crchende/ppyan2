from flask import Flask, request, url_for
from grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice
from date_intrare_proiect import *
import functiilib

import threading

# Logging - utilizare pachet logging

app = Flask(__name__)

# Pagina Principala
@app.route('/')
def index():
    ret = "<h1>Exemplu Proiect Python Pentru Studentii din anul II</h1>"
    
    ret += "<a href=" + url_for("salut") + ">Salut</a>" + "<br/>" 
    
    ret += "<a href=" + url_for("grafic_x_patrat") + ">Grafice functie grad 2</a>" + "<br/>"
    
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
    
# Exemple grafice functi de grad 2
@app.route('/xpatrat')
def grafic_x_patrat():

    genereaza_grafice(valori_x, valori_y, "static/imagini")
    #t1 = threading.Thread(target=genereaza_grafice, args = (valori_x, valori_y, "static/imagini"))
    #t1.start()
    #t1.join()
    ret = f"<a href={url_for('index')}>Acasa</a><br/>"
    
    ret += "valori x: " + str(valori_x) + "<br/>"
    ret += "valori y = x*x: " + str(valori_y) + "<br/>"
    
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_punct.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_steluta.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/afisare_cu_x.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/grafic_continuu_v1.png")}>' + "<br/>"
    ret += f'<img src={url_for("static", filename="imagini/grafic_continuu_v2.png")}>' + "<br/>"
    
    
    return ret
    


if __name__ == "__main__":
    app.run(debug=1)
