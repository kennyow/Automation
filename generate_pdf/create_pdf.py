#pip install fpdf
from fpdf import FPDF



pdf = FPDF(orientation='P', unit = 'pt', format='A4') #P - portrait, L - Landscape


pdf.add_page()

#w = width, h=height, x = axis x
pdf.image('Automation/generate_pdf/manutd.png', w=80, h=50)
#B= bold
pdf.set_font(family='Times', style='B', size=18)
#C = Center, ln= jump 1 line
pdf.cell(w=0, h=50, txt="MANCHESTER UNITED FA CHAMPION 2024", align='C', border=1, ln = 1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=35, txt="Congratulations!", align='C', ln=1)

pdf.set_font(family='Times',  size=12)
txt1 = """
O Manchester United Football Club, mais conhecido como Manchester United (também estilizado como Man United ou Man Utd) ou simplesmente United, é um clube de futebol profissional inglês sediado em Trafford, na região metropolitana de Manchester. Fundado em 1878, é um dos clubes mais populares e mais bem sucedidos da Inglaterra e do mundo
"""
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=100, h=25, txt="MASCOTE")

pdf.set_font(family='Times', size=12)
pdf.cell(w=100, h=25, txt="Fred The Devil", ln=1)

pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=100, h=25, txt="PRINCIPAL RIVAL")

pdf.set_font(family='Times', size=12)
pdf.cell(w=200, h=25, txt="Liverpool", ln=1)


pdf.output('Automation/generate_pdf/output.pdf')