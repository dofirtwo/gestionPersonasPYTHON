from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

p = []

@app.route("/")
def gestionPersona():   
    return render_template("gestionPersona.html")

@app.route("/person",methods=["POST"])
def personas():
    mensaje=""
    consulta=""
    if request.method=="POST":
        accion= request.form["btnAccion"]
        if (accion == "agregar"):
            identificacion= int(request.form["txtIdentificacion"])
            nombre = (request.form["txtNombre"])
            if (nombre==""):
                mensaje="Ingrese el Nombre"
            else:
                correo = (request.form["txtCorreo"])
                if (correo==""):
                    mensaje="Ingrese el Correo"
                else:
                    fechaNacimiento = (request.form["txtFechaNacimiento"])
                    if (fechaNacimiento==""):
                        mensaje="Ingrese la Fecha de Nacimiento"
                    else:
                        for persona in p:
                            if (persona[0]==identificacion or persona[2]==correo):
                                mensaje=f"Persona con esa identificacion o correo ya existe"
                                break
                        else:
                            p.append([identificacion,nombre,correo,fechaNacimiento])
                            mensaje="Persona Agregada"
        elif (accion == "consultar"):
            identificacion= int(request.form["txtIdentificacion"])
            for persona in p:
                if (persona[0]==identificacion):
                    consulta=(persona[0],persona[1],persona[2],persona[3])
                    break
            else:
                mensaje=f"No existe persona con esa identificacion"
        elif (accion == "actualizar"):
            idAnterior = int(request.form["txtIdAnterior"])
            identificacion = int(request.form["txtIdentificacion"])
            nombre = request.form["txtNombre"]
            correo = request.form["txtCorreo"]
            fechaNacimiento = request.form["txtFechaNacimiento"]
            for persona in p:     
                contador=p.index(persona)           
                if(persona[0]!=identificacion or persona[2]!=correo) and (persona[0]==idAnterior):
                    p[contador][0]=identificacion
                    p[contador][1]=nombre
                    p[contador][2]=correo
                    p[contador][3]=fechaNacimiento
                    mensaje="Persona Actualizada"   
                    break
            else:
                mensaje="Persona ya existe con identificación o correo"
        elif (accion == "eliminar"):
            identificacion = int(request.form["txtIdentificacion"])
            for persona in p:     
                contador=p.index(persona)           
                if(persona[0]==identificacion):
                    del p[contador]
                    mensaje="Persona Eliminada"   
                    break
            else:
                mensaje="Persona con esa identificacion o existe"
        return render_template("gestionPersona.html",p=p,consulta=consulta,mensaje=mensaje)
if __name__ == "__main__":
    app.run(port=3000, debug=True)