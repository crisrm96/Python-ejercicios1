def numeroAmes (indice):
    m = {
        '01':"Enero",
        '1':'Enero',
        '02':'Febrero',
        '2':'Febrero',
        '03':'Marzo',
        '3': 'Marzo',
        '04':'Abril',
        '4':'Abril',
        '05':'Mayo',
        '5':'Mayo',
        '06':'Junio',
        '6':'Junio',
        '07':'Julio',
        '7':'Julio',
        '08':'Agosto',
        '8':'Agosto',
        '09':'Septiembre',
        '9':'Septiembre',
        '10':'Octubre',
        '11':'Noviembre',
        '12':'Diciembre'
    }
    return m[indice]
dia = input('¿Qué día es mañana? ')
nombredia = dia.split('/')
nombremes = numeroAmes(nombredia[1])
print('Mañana es día ' + nombredia[0] + ' del mes de ' + nombremes + ' del año ' + nombredia[2])
