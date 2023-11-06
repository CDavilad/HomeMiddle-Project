from abc import ABC, abstractmethod
from reportlab.pdfgen import canvas
import os
import datetime
 
class PaymentProvider(ABC):
    @abstractmethod
    def generate_payment_pdf(self, recipient, amount, order):
        pass

class PDFPaymentProvider(PaymentProvider):
    def generate_payment_pdf(self, recipient, amount, order):
        # Lógica para generar un cheque de pago en PDF usando ReportLab
        date= datetime.datetime.now()

        pdf_file = f'payment_{recipient.replace(" ", "_")}_{date.year}_{date.month}_{date.day}_{date.hour}_{date.minute}_{date.second}.pdf'
        name_file= os.path.join(os.getcwd(), 'media/PDF/', pdf_file)
        c = canvas.Canvas(name_file)
        c.drawString(260, 770, f"HomeMiddle")
        c.drawString(100, 740, f"Thank you for purchasing")
        c.drawString(100, 720, f"Order Id: {order.id}")
        c.drawString(100, 700, f"Order date: {order.date_ordered}")
        c.drawString(100, 680, f"Bought by: {recipient}")
        c.drawString(100, 660, f"Products in your order: ")
        count=640
        for item in order.items.all():
            c.drawString(100, count, f" - {item.name}      ${item.price}")
            count-=20
        c.drawString(100, count-10, f"Total: ${amount}")
        # Agregar más detalles según tus necesidades
        c.save()
        return pdf_file
 
class FakePaymentProvider(PaymentProvider):
    def generate_payment_pdf(self, recipient, amount, order):
        # Esta clase simplemente muestra detalles del pago, no genera un PDF
        print(f"Generando cheque de pago falso para {recipient}")
        print(f"Monto: ${amount}")