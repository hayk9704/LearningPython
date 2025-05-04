from fpdf  import FPDF
name = input("Name: ")
class PDF(FPDF):
    def header(self):
        self.image(
            "C:/Users/haykg/Documents/python tutorials/lec8_object-oriented/shirtificate.png", 
            x=(self.w - 200)/2, y=50, w = 200
        )
        self.set_font("helvetica", style="B", size=50)
        self.cell(0, 30, "CS50 Shirtificate", align="C")
        self.ln(20)


pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=25)
pdf.set_text_color(255, 255, 255)
pdf.cell(0,200, f'{name} took CSV', align='C')
pdf.output("shirtificate.pdf")