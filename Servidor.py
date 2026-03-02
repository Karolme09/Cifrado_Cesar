# BY: Karol Melissa Chacon
# ==========================================================


from flask import Flask, render_template, request
import CifradoIn2  

# Se inicialliza
Servidor = Flask(__name__)

@Servidor.route("/", methods=["GET", "POST"])
def index():
 
    resultado = ""
    aviso = ""

    if request.method == "POST":
        texto = request.form.get("texto", "")
        #llave = int(request.form.get("llave", 0))
        #accion = request.form.get("accion", "")
        llave_str = request.form.get("llave", "0")  # Se optiene la llave como texto
        try:
            llave = int(llave_str)  # La llave la converte a entero
        except ValueError:
            llave = 0  # si falla, se usa 0 como valor por defecto

        # Validación de que la llave esté en el rango 1–26 
        if llave < 1 or llave > 26: 
            aviso = "La llave debe estar entre 1 y 26." 
        else: 
        # Se normaliza el rango 0–25 para el algoritmo 
            llave = (llave - 1) % 26    

        #Se obtiene la accion que se quiere (cifrar, decifrar o fuerza bruta)
        accion = request.form.get("accion", "")

        #Se realiza la acción que se selecciono y se ejecuta
        if accion == "cifrar":
            resultado = CifradoIn2.cifrar(texto, llave)
        elif accion == "descifrar":
            resultado = CifradoIn2.descifrar(texto, llave)
        elif accion == "criptoanalisis":
            resultado = CifradoIn2.criptoanalisis_fuerza_bruta(texto)

    #Pasa la info para que se muestre en la interfaz
    return render_template("index.html", resultado=resultado, aviso=aviso)

if __name__ == "__main__":
    # Ejecuta el servidor
    Servidor.run(debug=True)

