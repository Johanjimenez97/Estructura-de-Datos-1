class Generador:
    def generaTabla(self, tabla):
        codigo = ""
        for t in tabla:
            codigo = codigo + "<tr>"
            for j in t.split(","):
                if j == 'Oro':
                    j= '<img src="static/img/Oro.jpg" width="50px" heigth="50px">'
                elif j== 'Plata':
                    j = '<img src="static/img/Plata.jpg" width="50px" heigth="50px">'
                elif j== 'Bronce':
                    j = '<img src="static/img/Bronce.jpg" width="50px" heigth="50px">'
                elif j== 'Cobre':
                    j = '<img src="static/img/Cobre.jpg" width="50px" heigth="50px">'
                if j == '1':
                    j= '<img src="static/img/Rugal.jpg" width="50px" heigth="50px">'
                codigo = codigo + "<td>" + j + "</td>"



            codigo = codigo + "</tr>"
        codigo = "<table>" + codigo + "</table>"

        return codigo

    def generarTituloParrafo(self, titulo, parrafo):
        titulo = "<h1 >" + titulo + "</h1>"
        parrafo = "<p>" + parrafo + "</p>"
        return titulo + parrafo






