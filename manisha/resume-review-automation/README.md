# Resume Review Automation

This project automates the process of reviewing resumes and sending emails to candidates based on job requirements. It utilizes PDF parsing, text matching, and email functionality to streamline the recruitment process.

## Project Structure

```
resume-review-automation
├── src
│   ├── main.py            # Entry point of the application
│   ├── resume_parser.py   # Functions to parse resumes
│   ├── matcher.py         # Logic for matching resumes to job descriptions
│   ├── emailer.py         # Email sending functionality
│   └── utils.py           # Utility functions
├── job_description
│   └── job_description.pdf # PDF file containing the job description
├── resumes
│   └── sample_resume1.pdf  # Sample resume for testing
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd resume-review-automation
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your job description PDF in the `job_description` folder.
2. Add resumes in PDF format to the `resumes` folder.
3. Run the application:
   ```
   python src/main.py
   ```

The application will load the job description, scan the resumes, match candidates based on their qualifications, and send emails to the top candidates.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.