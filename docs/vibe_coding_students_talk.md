# Vibe Coding for Students

This companion file is a presentation-friendly outline for students learning how to use AI-assisted coding without outsourcing their understanding.

## Main Idea

AI can make you faster, but it does not automatically make you better. You still need to understand what you are building, why it works, and where it can fail.

## Practical Progression

### 1. Start Small

Use AI for:
- explaining errors
- generating small functions
- showing examples
- drafting tests

Do not start by asking for a whole app if you cannot review the result.

### 2. Learn the Modes

- **Chat** for explanation, examples, and small local fixes
- **Plan** for larger features, refactors, and architecture
- **Agent** for scoped tasks with tools, tests, and clear validation

Choosing the wrong mode creates unnecessary confusion and weak review.

### 3. Review Everything

Before you trust generated code, ask:
- Can I explain what this does?
- What assumptions is it making?
- What edge cases are missing?
- How would I test this?

## Habits That Build Real Skill

### Prompt Precisely

Instead of saying "build this," say what constraints matter.

Reference examples:
- [Prompt Engineering Examples](prompt_eng_examples/README.md)

Examples:
- write a pure function
- validate input
- use standard libraries only
- follow the existing project pattern
- write the test first

### Work in Small Batches

Small changes are easier to understand, test, and fix.

### Ask for Explanations, Not Just Fixes

If something breaks, ask why it broke before asking for a patch.

### Keep Ownership

If you cannot explain the code, you do not own it yet.

## Common Student Mistakes

| Mistake | Better Move |
| :--- | :--- |
| **Copy-paste without review** | Read the code line by line and explain it back. |
| **Huge prompts for huge features** | Break the task into small, testable steps. |
| **Skipping tests** | Write or generate tests before trusting the output. |
| **Using AI as a final answer machine** | Use AI as a collaborator that still needs supervision. |
| **Ignoring design** | Write a short note on scope, inputs, outputs, and constraints first. |

Example design notes:
- [Design Note Examples](design_note_examples/README.md)
- [CSV Trend Plot](design_note_examples/csv_trend_plot_design_note.md)
- [Reverse Text API](design_note_examples/reverse_text_api_design_note.md)
- [Study Flashcards CLI](design_note_examples/study_flashcards_cli_design_note.md)

## What Strong Students Do Differently

- They use AI to accelerate learning, not replace it.
- They ask sharper questions over time.
- They get better at spotting hallucinations and weak logic.
- They focus more on systems, design, and tradeoffs than on typing speed.

## Closing Message

Use AI to remove friction, not to remove thinking. The students who benefit most are the ones who stay curious, skeptical, and responsible.
