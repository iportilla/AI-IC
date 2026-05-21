# Lab 1: Continue Chat Mode Examples

This README collects the Continue Chat mode examples from the main Continue guide and focuses them on Lab 1.

## When To Use Chat Mode

Use Chat mode when you want explanation, drafting, or suggestions before making any file changes.

Chat mode is a good fit for Lab 1 when you want to:
- explain the Fibonacci script
- draft README content before editing files
- ask for markdown you can paste into documentation
- understand edge cases without changing code

## Chat Mode Example 1

Use this prompt when you want Continue to draft a README for the Fibonacci example.

```text
Write a concise README for a Python script that calculates Fibonacci numbers.

The script:
- defines fibonacci(n)
- returns 0 for negative input
- includes example calls for 0, 1, 2, 3, 4, 5, 10, and -1

Please give me:
1. a short project description
2. a function overview
3. example usage with expected outputs
4. a final markdown version I can paste into a docs README
```

## Chat Mode Example 2

Use this prompt when you want a plain-language explanation before writing documentation.

```text
Explain this Fibonacci script in simple language.

Focus on:
- what fibonacci(n) does
- how the loop works
- how edge cases are handled
- what should be documented in a README

Do not modify files. Just give me the explanation and a suggested README outline.
```

## Suggested Lab 1 Prompt

This version is tailored to the files in this lab.

```text
Explain CalculateFibonacci.py in simple language.

Include:
- what the script does
- how fibonacci(n) behaves for negative input, 0, and positive numbers
- how the iterative loop computes the result
- a short README outline for docs

Do not edit any files.
```

## Expected Outcome

After using Chat mode, you should have:
- a short explanation of the Fibonacci script
- a draft README structure
- example usage text you can reuse in markdown

If you want Continue to update files for you after that, switch to Agent mode.