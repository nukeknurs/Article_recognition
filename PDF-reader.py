from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import crossref.restful
import os
import shutil
import pprint
import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('PeDeFy.log','wt',encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

def convert_pdf_to_txt(path):

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    sys.stdout = Logger()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
        break #to convert pdf's first page only
    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    return text

onlyfiles = [f for f in os.listdir(os.getcwd())]
pdffiles = []
forbidden_elements = ['/', '\\', '*', '<', '>', ':', '|', '?', '\"']
print('\nAll files in current directory:\n')
for file in onlyfiles:
    print(file)
    if file[-3:] == 'pdf':
        pdffiles.append(file)
print('\n')

print('All PDF files in current directory:\n')
for i in pdffiles:
    print(i)
print('\n')

try:
    os.mkdir('Archive')
except:
    pass
file = open('Dictionary.log', 'a',encoding='utf-8')
try:
    dictionarycontent = open('Dictionary.log', 'r',encoding='utf-8')
except:
    pass

dictionarycontent2 = dictionarycontent.read()
dictionarycontent.close()

for pdf in pdffiles:
    dictionary = ''
    dictionary += pdf + ' \t =-> \t '
    path = os.getcwd() + '/' + pdf

    content = convert_pdf_to_txt(path)
    content = content.lower()
    doi_position = content.find('doi')
    doi_position2 = content[doi_position:-1]
    doi_position2 = doi_position2.find('10.')

    doi23 = content[doi_position2 + doi_position:doi_position2 + content[doi_position2 + doi_position:-1].find('\n') + doi_position]
    print('Found DOI:\t',doi23)
    file_metadata = crossref.restful.Works().doi(doi23)
    if str(doi23) in dictionarycontent2:
        print('Present:\t', pdf,'\n')
        continue

    try:
        file_name = file_metadata['author'][0]['given'] + ' ' + file_metadata['author'][0]['family'] + ' - ' +file_metadata['title'][0] + ', ' + file_metadata['publisher'] + ', ' + str(file_metadata['published-print']['date-parts'][0][1]) + '_' + str(file_metadata['published-print']['date-parts'][0][0]) + '.pdf'
        print('Filename:\t',file_name)
    except:
        continue
    dictionary += file_name + '  '+doi23+'\n'

    
    if file_name not in dictionarycontent2:
        print('Absent file:\t', file_name)
        shutil.copyfile(path, os.getcwd() + '\\Archive\\' + pdf)

        for elem in forbidden_elements:

            if elem in file_name:
                file_name = file_name[:file_name.find(elem)] + ' ' + file_name[file_name.find(elem) + 1:]

        os.rename(path, os.getcwd() + '\\' + file_name)
        print('Final filename:\t',file_name,'\n')
        file.write(dictionary)

file.close()