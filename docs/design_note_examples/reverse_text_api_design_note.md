# Design Note Example: Reverse Text API

## Problem

Build a simple FastAPI service with one endpoint that accepts a string and returns the reversed string.

## Scope

Included:
- one API endpoint
- one request model
- one response body containing the reversed text
- basic input validation

Excluded:
- authentication
- database storage
- rate limiting
- deployment configuration

## Inputs

- HTTP POST request
- JSON body with one field: `text`

Example request:

```json
{
  "text": "hello world"
}
```

## Outputs

Example response:

```json
{
  "reversed_text": "dlrow olleh"
}
```

## Constraints

- use FastAPI and Pydantic
- endpoint must be `POST`, not `GET`
- reject missing or empty text values
- keep the implementation in one small file for teaching purposes

## Validation

- valid request returns status `200`
- empty text returns a validation or client error
- the reversed text matches the original input exactly in reverse order
- the API can be run locally with a simple development server
