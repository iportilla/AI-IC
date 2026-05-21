# Lab 2: Continue Plan Mode Examples

This README collects the Continue Plan mode examples from the main Continue guide and focuses them on Lab 2.

## When To Use Plan Mode

Use Plan mode when you want Continue to inspect the repo and propose exact steps before editing anything.

Plan mode is a good fit for Lab 2 when you want to:
- inspect the Fibonacci script before writing documentation
- decide what sections a README should contain
- identify which existing content should be replaced
- get a verification checklist before any edits happen

## Plan Mode Example 1

Use this prompt when you want Continue to plan documentation work for the Fibonacci example.

```text
Create a plan to document the Fibonacci Python script in README.md

Constraints:
- source file: CalculateFibonacci.py
- target file: README.md
- do not edit anything yet
- inspect the script and return the full plan in one response
- do not stop after inspection and do not ask to continue
- propose the exact README sections
- include what content should be replaced in the current README
- include a verification step to confirm the README matches the script
```

## Plan Mode Example 2

Use this prompt when you want a step-by-step outline before rewriting documentation.

```text
Plan how to replace the existing docs README with documentation for the Fibonacci example.

Requirements:
- identify what the script does
- describe the fibonacci(n) function
- include negative-input behavior
- include example outputs
- keep the README short and beginner-friendly
- return the complete step-by-step plan in one message

Do not write the file yet. Give me a step-by-step plan only.
```

## Suggested Lab 2 Prompt

This version is tailored to the files in this lab.

```text
Create a plan to document CalculateFibonacci.py.

Include:
- the sections that should appear in the README
- what the README should say about negative input, base cases, and the loop
- which example outputs from the script should be included
- a final verification step to check the README matches the script
- return the full plan in one response after inspecting the file

Do not edit any files.
```

## Expected Outcome

After using Plan mode, you should have:
- a step-by-step documentation plan
- a clear README structure
- a checklist for verifying the final markdown

If you want Continue to carry out the edits after that, switch to Agent mode.