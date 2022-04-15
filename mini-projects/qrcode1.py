from barcode import EAN13
from barcode.writer import ImageWriter

number = "580124123457"
my_code = EAN13(number, writer=ImageWriter)

my_code.save("New_code1")