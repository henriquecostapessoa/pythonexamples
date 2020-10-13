import PyPDF2
pdffileobj=open("report.pdf","rb")
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(0)
text=pageobj.extractText()

file1=open(r"C:\Users\hcost\Desktop\Python\\report.txt","a")
file1.writelines(text)
file1.close()

#Extract images

from PIL import Image

input1 = PyPDF2.PdfFileReader(open("report.pdf", "rb"))
page0 = input1.getPage(0)
xObject = page0["/Resources"]["/XObject"].getObject()

for obj in xObject:
    if xObject[obj]["/Subtype"] == "/Image":
        size = (xObject[obj]["/Width"], xObject[obj]["/Height"])
        data = xObject[obj].getData()
        print(dir(xObject[obj].getData()))

        # if xObject[obj]["/ColorSpace"] == "/DeviceRGB":
        #     mode = "RGB"
        # else:
        #     mode = "P"

        # if xObject[obj]["/Filter"] == "/FlateDecode":
        #     img = Image.frombytes(mode, size, data)
        #     img.save(obj[1:] + ".png")
        # elif xObject[obj]["/Filter"] == "/DCTDecode":
        #     img = open(obj[1:] + ".jpg", "wb")
        #     img.write(data)
        #     img.close()
        # elif xObject[obj]["/Filter"] == "/JPXDecode":
        #     img = open(obj[1:] + ".jp2", "wb")
        #     img.write(data)
        #     img.close()                