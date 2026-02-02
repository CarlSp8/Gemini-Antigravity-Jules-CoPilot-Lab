# Git Best Practices

## Commit Guidelines

### Write Clear Commit Messages
- Use imperative mood: "Add feature" not "Added feature"
- Keep subject line under 50 characters
- Separate subject from body with a blank line
- Explain what and why, not how

### Example
```
Add user authentication feature

Implements OAuth 2.0 authentication to improve security.
This change allows users to log in using their GitHub accounts.
```

## Branching Strategy

### Feature Branches
- Create a new branch for each feature
- Use descriptive names: `feature/user-authentication`
- Keep branches short-lived

### Main Branches
- `main` - Production-ready code
- `develop` - Integration branch for features

## Pull Request Best Practices

1. Keep PRs small and focused
2. Write descriptive PR descriptions
3. Reference related issues
4. Ensure all tests pass
5. Request reviews from relevant team members

## Code Review

- Review code promptly
- Be constructive and respectful
- Focus on the code, not the person
- Ask questions for clarity
- Suggest improvements with examples

## Tips

- Commit often with logical changes
- Use `.gitignore` appropriately
- Don't commit sensitive data
- Test before pushing
- Keep your local repository clean
