# Quiz Game
A Python-based quiz application that reads multiple-choice questions from PDF files and presents them in an interactive terminal interface.

## Features
- PDF question parsing
- Interactive terminal interface
- Randomized question order
- Score tracking
- Performance feedback
- New terminal window launch option

## Requirements
- Python 3.x
- PyPDF2
- Linux-based system with one of these terminal emulators:
  - GNOME Terminal
  - Konsole
  - xterm

## Installation
1. Clone the repository:
```bash
git clone [your-repo-url]
cd quiz-game
```

2. Install required packages:
```bash
pip install PyPDF2
```

## Usage
The application can be run in two ways:

### Standard Mode
```bash
python3 quiz.py
```

### New Terminal Window Mode
```bash
python3 launch_quiz.py
```

## PDF Format Requirements
The quiz PDF must follow this specific format:

```
Question text goes here?
A) First option
B) Second option
C) Third option
D) Fourth option
Answer: B

Next question?
A) Option 1
B) Option 2
C) Option 3
D) Option 4
Answer: A
```

Key formatting rules:
- Each question must be followed by exactly 4 options
- Options must be labeled A) through D)
- Answer line must start with "Answer:" followed by the correct letter
- Leave a blank line between questions

## Project Structure
```
quiz-game/
├── quiz.py          # Main quiz implementation
├── launch_quiz.py   # Terminal launcher script
└── README.md        # Documentation
```

## Files
- `quiz.py`: Contains the core quiz functionality including PDF parsing and quiz logic
- `launch_quiz.py`: Handles launching the quiz in a new terminal window

## License
MIT License


## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors
- arkade

## Acknowledgments
- Course material from GEL 403
- PyPDF2 library

Feel free to modify this documentation based on any additional features or changes you make to the project!