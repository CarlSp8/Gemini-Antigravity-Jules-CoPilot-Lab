# Code Review Guide

## Purpose
Code reviews are essential for maintaining code quality, sharing knowledge, and catching bugs early.

## Before Submitting for Review

### Checklist
- [ ] Code compiles/runs without errors
- [ ] All tests pass
- [ ] Added tests for new functionality
- [ ] Updated documentation
- [ ] Followed coding standards
- [ ] No debug code or console logs
- [ ] Self-reviewed the changes

## As a Reviewer

### What to Look For

#### Functionality
- Does the code do what it's supposed to do?
- Are there edge cases not handled?
- Is error handling appropriate?

#### Code Quality
- Is the code readable and maintainable?
- Are variable names descriptive?
- Is the code well-organized?
- Are there code smells?

#### Security
- Are there any security vulnerabilities?
- Is user input validated?
- Are secrets properly managed?

#### Performance
- Are there obvious performance issues?
- Could algorithms be optimized?
- Are resources properly managed?

#### Testing
- Are tests comprehensive?
- Do tests actually test the functionality?
- Are edge cases covered?

## Review Etiquette

### Do
- Be respectful and constructive
- Explain your reasoning
- Provide examples or suggestions
- Ask questions for clarification
- Recognize good work

### Don't
- Make personal attacks
- Be dismissive
- Nitpick style if it follows standards
- Block progress on minor issues

## Response Time
- Try to review within 24 hours
- Communicate if you need more time
- Prioritize blocking PRs

## Example Comments

### Good
- "Consider using a Set here for O(1) lookup instead of array iteration. Example: `const userIds = new Set(users.map(u => u.id));`"
- "This function is quite long. Could we extract the validation logic into a separate function for better readability?"

### Avoid
- "This is wrong."
- "Why would you do it this way?"
