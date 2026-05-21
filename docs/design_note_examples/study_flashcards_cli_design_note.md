# Design Note Example: Study Flashcards CLI

## Problem

Create a command-line study tool that asks a user flashcard questions from a small in-memory list and reports the final score.

## Scope

Included:
- a built-in list of flashcards
- one question shown at a time
- user answer input from the terminal
- score tracking
- final summary

Excluded:
- file persistence
- spaced repetition
- categories or tags
- GUI interface

## Inputs

- user text entered in the terminal
- an internal list of flashcards such as question-answer pairs

Example flashcard:

```text
Question: What is the capital of France?
Answer: Paris
```

## Outputs

- each question shown in the terminal
- immediate feedback such as correct or incorrect
- final score, for example `3/5 correct`

## Constraints

- use plain Python
- prefer standard library only
- answers should be checked case-insensitively
- keep the program short enough for a beginner to read in one sitting

## Validation

- the program asks all questions in the set
- score increases only for correct answers
- uppercase and lowercase answers are treated the same
- final output shows total correct answers and total questions
