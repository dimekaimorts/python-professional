
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def make_report_of(build_report):
    def wrapper(*args, **kwargs):
        return build_report(*args, **kwargs)
    return wrapper

@make_report_of
def build_report(id:int, nombre:str, materias:dict):
    w, h = A4
    w0, h0 = 50, h-50
    canva = canvas.Canvas("{}-{}.pdf".format(id, nombre), pagesize=A4)
    canva.drawString(w0, h0, f"Boleta:{id}")
    canva.drawString(w0, h0-10, f"Nombre: {nombre}")
    canva.drawString(w0, h0-20, f"")
    renglon = 30
    for materia,nota in materias.items():
        canva.drawString(w0, h0-renglon, f"{materia}: {nota}")
        renglon += 12
    
    canva.save()


def main():
    data = {
        "Programacion Orientada a Objetos" : 10,
        "Estructuras de Datos" : 9,
        "Algoritmos Geneticos" : 9,
        "Mineria de Datos" : 8,
        "Machine Learning" : 10
    }
    build_report("2022650332", "Roberto Martinez Juarez", data)


if __name__ == "__main__":
    main()