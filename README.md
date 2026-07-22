# Rule-Based Expert System Using Forward Chaining

## Overview
This project is a simple Artificial Intelligence (AI) expert system developed in Python. It uses forward chaining and if-then rules to infer conclusions based on user-provided facts.

## Features
- Rule-based reasoning
- Forward chaining inference
- User-friendly console interface
- Displays reasoning path
- Multi-step inference
- Handles cases where no disease is identified

## Technologies Used
- Python 3
- Rule-Based AI
- Forward Chaining

## Project Structure

Rule-Based-Expert-System/
│── expert_system.py
│── README.md
│── requirements.txt

## How to Run

1. Open the project in VS Code.
2. Run:

python expert_system.py

3. Enter the symptoms.
4. View the diagnosis and reasoning path.

## Sample Rules

IF Fever AND Cough → Flu

IF Flu → Visit Doctor

IF Fever AND Headache → Viral Fever

IF Viral Fever → Take Rest

## Output

The system displays:
- Disease
- Recommendation
- Reasoning Path
- Final Facts

## Author

Nidhi Hatgaonkar