import PyPDF2, pyttsx3


pdfreader = PyPDF2.PdfReader(open("FT-german-housing.pdf", "rb"))
speaker = pyttsx3.init("nsss")

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
speaker.save_to_file(clean_text, 'news.mp3')
speaker.runAndWait()

speaker.stop()