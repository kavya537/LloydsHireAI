import textract

def extract_text_from_resume(file_path):
    try:
        return textract.process(file_path).decode('utf-8')
    except Exception as e:
        print(f"Error reading resume: {e}")
        return ""
