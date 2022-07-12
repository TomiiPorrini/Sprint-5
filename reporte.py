class GetHTML():
    def __init__(self,errores):
        self.errores = errores

    def get_html(self):
        html='<ol>'
        
        for estado in self.errores:
            row="<li>"+ estado +"</li>"
            html+=row
        html+='</ol>'

        self.html = html
        with open("output.html", "w") as text_file:
            text_file.write(self.html)