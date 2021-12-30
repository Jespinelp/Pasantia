import os
import requests
import psycopg2
import re
from datetime import datetime

from flask import Flask, session, render_template, request, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__,template_folder='pages')


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

''' conexion con la base de datos '''

conexion=psycopg2.connect(user='wewrjlyy',
                          password='BolLeBii2KIWInrC3OAgg1X4vFBIKwco',
                          host='castor.db.elephantsql.com',
                          port='5432',
                          database='wewrjlyy')

db=conexion.cursor()

'''Rutas de la aplicacion '''

@app.route("/")
def index():
    return render_template("examples/login0.html")

'''Rutas de Desarrollador '''

@app.route("/Des_list_Doc")
def Des_list_Doc():
    return render_template("tables/Des_list_Doc.html")

@app.route("/Des_Crea_Doc")
def Des_Crea_Doc():
    return render_template("tables/Des_Crea_Doc.html")

@app.route("/Des_Edit_Doc")
def Des_Edit_Doc():
    return render_template("tables/Des_Edit_Doc.html")



'''Rutas de Arquitecto '''

@app.route("/arqlist")
def arqlist():
    return render_template("tables/Arqlist.html")

@app.route("/arqdocs")
def arqdocs():
    return render_template("forms/ArqDocs.html")

'''Rutas de Director '''

@app.route("/Dir_aprov_doc")
def Dir_aprov_doc():
    return render_template("tables/Dir_aprov_doc.html")

@app.route("/Dir_list_doc")
def Dir_list_doc():
    return render_template("tables/Dir_list_doc.html")

'''Rutas de Administrador '''

@app.route("/admuser")
def admusers():
    return render_template("tables/AdmUsers.html")

@app.route("/amduserscreate")
def admuserscreate():
    return render_template("forms/AdmCreateuser.html")

@app.route("/AdmEdituser")
def AdmEdituser():
    return render_template("forms/AdmEdituser.html")

@app.route("/creauser_admin", methods=["POST"])
def creauser_admin():


    nombre = request.form.get("nombres")
    apellido = request.form.get("apellidos")
    usuario = request.form.get("usuario")
    contraseña = request.form.get("contraseña")
    rol = request.form.get("rol")

    cursor=conexion.cursor()

    sql=("SELECT * FROM users WHERE username = '%s'" % (nombre))
    cursor.execute(sql)
    registros=cursor.rowcount

    if registros == 1:
        return render_template("error.html", message="Ese usuario ya existe")

    db.execute("INSERT INTO persona (nombres, apellidos, usuario, rol, contrasenia) VALUES ('%s', '%s', '%s', '%s', '%s' )" % (nombre, apellido, usuario, rol, contraseña))
    conexion.commit()
    return render_template("tables/AdmUsers.html", nombre=nombre)



@app.route("/edituser_admin", methods=["POST"])
def edituser_admin():


    nombre = request.form.get("nombres")
    apellido = request.form.get("apellidos")
    usuario = request.form.get("usuario")
    contraseña = request.form.get("contraseña")
    rol = request.form.get("rol")

    cursor=conexion.cursor()

    sql=("SELECT * FROM users WHERE username = '%s'" % (nombre))
    cursor.execute(sql)
    registros=cursor.rowcount

    if registros == 1:
        return render_template("error.html", message="Ese usuario ya existe")

    db.execute("UPDATE persona SET nombres = '%s', apellidos = '%s', usuario = '%s', rol = '%s', contrasenia = '%s' WHERE usuario = '%s'" % (nombre, apellido, usuario, rol, contraseña, usuario))
    conexion.commit()
    return render_template("tables/AdmUsers.html", nombre=nombre)

@app.route("/Admindelete")
def Admindelete():
    return render_template("Admindelete.html")

@app.route("/Admindeletecre", methods=["POST"])
def deleteuser_admin():

    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    usuario = request.form.get("usuario")
    cursor=conexion.cursor()

    db.execute("DELETE FROM persona WHERE  usuario = '%s'" % (usuario))
    conexion.commit()
    return render_template("registersuccess.html", nombre=nombre)


'''Login '''

@app.route("/login", methods=["POST"])

def login():


    try:
        usuario = request.form.get("usuario")
        contraseña = request.form.get("contraseña")
    except ValueError:
        return render_template("error.html"),404

    cursor=conexion.cursor()

    sql=("SELECT * FROM persona WHERE usuario = '%s' AND contrasenia = '%s'" % (usuario,contraseña))
    cursor.execute(sql)
    registros=cursor.rowcount
    print(registros)
    if registros == 1:
        cursor=conexion.cursor()
        sql=("SELECT nombres, apellidos FROM persona where usuario= '%s' AND contrasenia= '%s'" % (usuario, contraseña))
        cursor.execute(sql)
        m=cursor.fetchone()
        x=''.join(m)
        lista=[]
        lista1=[]
        lista.append(x)



        for i in range(len(lista)):
          nombresuser=lista[i]
          nombresuser=re.sub('[^A-Za-z0-9]\'|\)|\,',' ',nombresuser)
        session["usuario"] = nombresuser

        cursor=conexion.cursor()
        sql=("SELECT rol FROM persona WHERE usuario = '%s' AND contrasenia = '%s'" % (usuario,contraseña))
        cursor.execute(sql)
        r=cursor.fetchone()
        x=''.join(r)
        lista=[]
        lista1=[]
        lista.append(x)



        for i in range(len(lista)):
          datos=lista[i]
          datos=re.sub('[^A-Za-z0-9]\'|\)|\,',' ',datos)


        if datos == "Administrador":
            return render_template("tables/AdmUsers.html",fullname=nombresuser,roles=datos)
        elif datos == "Arquitecto":
            return render_template("tables/Arqlist.html", fullname=nombresuser,roles=datos)
        elif datos == "Desarrollador":
            return render_template("tables/Des_list_Doc.html", fullname=nombresuser,roles=datos )
        elif datos == "Director":
            return render_template("tables/Dir_list_doc.html",fullname=nombresuser,roles=datos)

    else:
        return render_template("examples/login0.html", message="Usuario o Contraseña incorrecta")


@app.route("/logout")
def logout():
    return render_template("examples/login0.html")

@app.route("/creadoc_des", methods=["POST"])
def creadoc_des():


    codigo = request.form.get("codigo")
    fecha_rev = request.form.get("fecha_rev")
    fecha_elab = request.form.get("fecha_elab")
    tipo_rev = request.form.get("tipo_rev")
    descripcion = request.form.get("descripcion")
    observaciones = request.form.get("observaciones")
    resultados = request.form.get("resultados")

    cursor=conexion.cursor()


    db.execute("INSERT INTO documentos (codigo, fecha_rev, fecha_elab, tipo_rev, descripcion, observaciones, resultado) VALUES ('%s', '%s', '%s', '%s', '%s' , '%s', '%s' )" % (codigo, fecha_rev, fecha_elab, tipo_rev, descripcion, observaciones, resultados))
    conexion.commit()
    return render_template("tables/Des_list_Doc.html")

@app.route("/editdoc_des", methods=["POST"])
def editdoc_des():


    codigo = request.form.get("codigo")
    fecha_rev = request.form.get("fecha_rev")
    fecha_elab = request.form.get("fecha_elab")
    tipo_rev = request.form.get("tipo_rev")
    descripcion = request.form.get("descripcion")
    observaciones = request.form.get("observaciones")
    resultados = request.form.get("resultados")

    cursor=conexion.cursor()



    db.execute("UPDATE documentos SET fecha_elab = '%s', tipo_rev = '%s', descripcion = '%s', observaciones = '%s', resultado = '%s' WHERE codigo = '%s'" % (fecha_elab, tipo_rev, descripcion, observaciones, resultados, codigo))
    conexion.commit()
    return render_template("tables/Des_list_Doc.html")
@app.route("/ArqDocs", methods=["POST"])
def Docs_dir():
    time=datetime.today().strftime('%Y-%m-%d')
    observaciones = request.form.get("observaciones")
    si = request.form.get("si")
    print(si)
    aux=''
    if(si == 'true'):
        aux='Cumple'
    else :
        aux='No cumple'



    cursor=conexion.cursor()



    db.execute("INSERT INTO revision (estado, fecha, observaciones_generales, ) values ('%s', '%s','%s','25')" % (aux, time, observaciones))
    conexion.commit()
    return render_template("tables/Arqlist.html")
