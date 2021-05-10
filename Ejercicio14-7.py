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
birthday = input('¿Cuándo es tu cumpleaños? ')
nombrebirthday = birthday.split('/')
nombremes = numeroAmes(nombrebirthday[1])
print('Tu cumpleaños es el día ' + nombrebirthday[0] + ' del mes de ' + nombremes + ' del año ' + nombrebirthday[2])
