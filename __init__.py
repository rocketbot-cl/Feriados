# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import requests

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "getFeriadoArgentina":

    try:

        date_ = GetParams('date_')
        var_ = GetParams('var_')
        year = date_[0:4]
        url = r"http://nolaborables.com.ar/api/v2/feriados/{year}?formato=mensual".format(year=year)
        response = requests.get(url)
        data = response.json()
        try:
            month = int(date_[5:7]) - 1
            day = str(int(date_[8:10]))
            feriado = data[month][day]
            if feriado is not None:
                res = True
        except:
            res = False
        SetVar(var_, res)
    except Exception as e:
        PrintException()
        raise e

if module == "getFeriado":

    try:

        date_ = GetParams('date_')
        var_ = GetParams('var_')
        print(date_, var_)

        URL_ = r"https://apis.digital.gob.cl/fl/feriados/{fecha}".format(fecha=date_)

        headers = {
            'User-Agent': 'My User Agent 1.0',
        }

        data = requests.get(URL_, headers=headers)
        data = data.json()

        print(data)

        if "error" in data:
            res = False
        else:
            res = True

        SetVar(var_, res)
    except Exception as e:
        PrintException()
        raise e

if module == "getFeriadoColombia":
    try:

        date_ = GetParams('date_')
        api_key = GetParams('api_key')
        var_ = GetParams('var_')
        year = date_[0:4]
        url = r"https://calendarific.com/api/v2/holidays?api_key={api_key}&country=CO&year={year}".format(api_key=api_key, year=year)
        response = requests.get(url)
        data = response.json()
        holydays = data['response']['holidays']
        date_with_slash = date_.replace("/", "-")
        res = False
        for holyday in holydays:
            if holyday['date']['iso'] == date_with_slash:
                res = True
        SetVar(var_, res)
    except Exception as e:
        PrintException()
        raise e

if module == "esFeriado":
    res = GetParams("res")
    try:
        url = "https://deperu.com/api/rest/esFeriado.json"
        response = requests.get(url)
        alerta = response.json()['alerta']
        es_feriado = True
        if alerta == "No es feriado":
            es_feriado = False
        SetVar(es_feriado, res)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
