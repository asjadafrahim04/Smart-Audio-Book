import pyttsx3
import PyPDF2
book = open('OS.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
friend = pyttsx3.init()
page = pdfReader.pages[3]
text = page.extract_text()
friend.say(text)
friend.runAndWait()
book.close()