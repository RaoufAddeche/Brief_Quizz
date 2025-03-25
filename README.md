# Brief Quizz Project

## Description
This project is a simple quiz application built using Streamlit. It allows users to create quizzes, save them, and then take the quizzes while tracking their scores. The application supports multiple-choice questions and provides feedback on the correctness of answers.

## Features
- **Create a Quiz**: Users can input questions, multiple-choice answers, and specify the correct answer.
- **Save Questions**: Questions can be saved to a JSON file for persistence.
- **Launch a Quiz**: Users can take the quiz, answer questions, and receive feedback on their answers.
- **Score Tracking**: The application tracks the user's score and displays it at the end of the quiz.
- **Reset Quiz**: Users can reset the quiz to start over.

## Directory Structure
```
raoufaddeche-brief_quizz/
├── README.md
├── brouillon.py
├── main.py
├── quizz_questions.json
└── requirements.txt
```

## Files
- **README.md**: This file, providing an overview of the project.
- **brouillon.py**: A draft file containing experimental code and ideas for the project.
- **main.py**: The main application file containing the Streamlit implementation of the quiz.
- **quizz_questions.json**: A JSON file storing the quiz questions and answers.
- **requirements.txt**: A file listing the Python dependencies required to run the project.

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:RaoufAddeche/Brief_Quizz.git
   cd raoufaddeche-brief_quizz
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   streamlit run main.py
   ```
2. Use the sidebar menu to choose between creating a quiz or launching a quiz.
3. Follow the on-screen instructions to create questions, save them, and take the quiz.

## Dependencies
- Streamlit==1.40.1
- Pydantic

## Notes
- Ensure that the `quizz_questions.json` file is in the same directory as `main.py`.
- Images used in the application should be placed in the appropriate directory and their paths updated in the code if necessary.

## License
This project is licensed under the MIT License.
