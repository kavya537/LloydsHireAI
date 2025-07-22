import fitz
doc = fitz.open("C:/Users/kavya/Documents/Hackathon_01/resumes/Resume_Kavya_PythonDev.pdf")
print(doc.page_count)
doc.close()