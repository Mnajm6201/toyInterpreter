# toyInterpreter
Interpreter for the toy langauge 🚀 

### Description  
The **toyInterpreter** is a basic interpreter designed to parse, evaluate, and execute instructions written in a toy programming language. This project is a learning-oriented implementation aimed at understanding interpreters, syntax trees, and evaluation of instructions.

### Language
```bnf
Program:
	Assignment*

Assignment:
	Identifier = Exp;

Exp: 
	Exp + Term | Exp - Term | Term

Term:
	Term * Fact  | Fact

Fact:
	( Exp ) | - Fact | + Fact | Literal | Identifier

Identifier:
     	Letter [Letter | Digit]*

Letter:
	a|...|z|A|...|Z|_

Literal:
	0 | NonZeroDigit Digit*
		
NonZeroDigit:
	1|...|9

Digit:
	0|1|...|9
```

### Features
- 🧩 **Lexer** Transforms input into a list of token/ lexume pairs using a simple regex.
- 🚀 **Parsing**: Reads and interprets tokens in the toy language syntax.  Returns a parse tree.
- 📝 **Evaluator**: Supports basic operations (arithmetic, variable assignments, etc.). 

### Requirements  
To run the project, ensure you have:  
- **Python 3.x** installed on your machine.  
- A text editor or IDE (e.g., VSCode, PyCharm).  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Mnajm6201/toyInterpreter.git
   cd toyInterpreter

### Run the Interpreter
Write your toy code in a txt in the directory (like **test.txt**).
Run 
```bash
python3 toy.py nameOfYour.txt
```
in terminal.
Alternatively, run
```bash
python3 toy.py 
```
And type your code in the terminal. To exit input, presses Ctrl+D on Unix/ Ctrl+Z+Enter on Windows.

### Future plans
This was a fun project, and I look forward to further my understanding in interpreter / compiler logic.