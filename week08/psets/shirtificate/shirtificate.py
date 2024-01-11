# CS50 Shirtificate

from fpdf import FPDF, Align, YPos


class PDF(FPDF):
    def __init__(self, name):
        super().__init__(orientation="portrait", format="A4")
        if not name:
            raise ValueError()
        self.name = name
        self.set_title(f"CS50 Shirtificate of {name}")
        self.set_author("Shirtifications Corporate")

    def header(self):
        self.set_font(family="helvetica", style="B", size=40)
        self.cell(text="CS50 Shirtificate", center=True)
        self.image("./shirtificate.png", x=Align.C, y=50, w=(self.epw * .9))

    def footer(self):
        self.set_text_color(r=255, g=255, b=255)
        self.set_font(family="helvetica", style="B", size=24)
        self.set_y(self.eph/2.65)
        self.cell(text=f"{self.name} took CS50", center=True)


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.add_page('')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()