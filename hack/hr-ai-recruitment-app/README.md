# HR AI Recruitment Application

This project is an AI-powered recruitment application designed to streamline the hiring process for HR professionals. It allows HR to upload job descriptions, enables candidates to apply with their resumes, and uses machine learning models to match candidates with job openings. The application also provides a dashboard to visualize match percentages and candidate details, along with the capability to send automatic email notifications to selected candidates.

## Features

- **Job Description Upload**: HR can upload job descriptions in PDF format.
- **Candidate Application**: Candidates can apply for job openings with their resumes stored in a database.
- **Machine Learning Matching**: Utilizes machine learning models to match candidates based on their resumes and job descriptions.
- **Dashboard**: Displays match percentages and candidate details in a user-friendly format.
- **Automatic Email Notifications**: Sends emails to selected candidates for further communication.

## Project Structure

```
hr-ai-recruitment-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── agent
│   │   └── ai_agent.py       # AI agent for processing job descriptions and matching candidates
│   ├── database
│   │   └── models.py         # Database models for candidates and job descriptions
│   ├── ml
│   │   └── matcher.py        # Machine learning matching logic
│   ├── dashboard
│   │   └── dashboard.py      # Dashboard for visualizing match results
│   ├── emailer
│   │   └── send_email.py     # Email sending functionality
│   ├── utils
│   │   └── file_upload.py     # Utility functions for file uploads
│   └── types
│       └── index.py          # Type definitions and interfaces
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd hr-ai-recruitment-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```
   python src/main.py
   ```

2. Follow the prompts to upload job descriptions and manage candidate applications.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.