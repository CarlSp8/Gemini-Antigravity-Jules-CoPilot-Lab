# Example: PR Quality Check

This example demonstrates how to evaluate the quality of a pull request.

## Using Python

```python
from src.utils.developer_tools import calculate_pr_quality_score

# Example PR data
pr_data = {
    'lines_changed': 250,
    'has_tests': True,
    'description': '''
# Feature: User Authentication

## Summary
Implements OAuth 2.0 authentication for user login.

## Changes
- Added OAuth provider integration
- Created authentication middleware
- Updated user model with OAuth fields
- Added comprehensive tests

## Testing
- All unit tests pass
- Integration tests added
- Manual testing completed
    ''',
    'comments_addressed': 8,
    'total_comments': 8
}

# Calculate quality score
result = calculate_pr_quality_score(pr_data)

print(f"PR Quality Score: {result['score']}/100")
print(f"Quality Level: {result['quality_level']}")
print("\nFeedback:")
for feedback_item in result['feedback']:
    print(f"  - {feedback_item}")
```

## Using JavaScript

```javascript
const { calculatePRQualityScore } = require('./src/utils/developer_tools');

// Example PR data
const prData = {
  linesChanged: 250,
  hasTests: true,
  description: `
# Feature: User Authentication

## Summary
Implements OAuth 2.0 authentication for user login.

## Changes
- Added OAuth provider integration
- Created authentication middleware
- Updated user model with OAuth fields
- Added comprehensive tests

## Testing
- All unit tests pass
- Integration tests added
- Manual testing completed
  `,
  commentsAddressed: 8,
  totalComments: 8
};

// Calculate quality score
const result = calculatePRQualityScore(prData);

console.log(`PR Quality Score: ${result.score}/100`);
console.log(`Quality Level: ${result.qualityLevel}`);
console.log('\nFeedback:');
result.feedback.forEach(item => console.log(`  - ${item}`));
```

## Expected Output

```
PR Quality Score: 90/100
Quality Level: Excellent

Feedback:
  - PR is moderately large. Ensure it's focused.
```

## PR Quality Guidelines

### Size
- **Small (< 200 lines):** Easy to review, fast to merge ✅
- **Medium (200-500 lines):** Acceptable if focused ⚠️
- **Large (> 500 lines):** Consider breaking up ❌

### Description
A good PR description includes:
- **Summary:** What does this PR do?
- **Why:** Why is this change needed?
- **Changes:** What changed?
- **Testing:** How was it tested?
- **Screenshots:** For UI changes
- **Related Issues:** Links to issues

### Tests
- Unit tests for new functions
- Integration tests for new features
- Edge case coverage
- All tests passing

### Review Comments
- Address all comments
- Explain if you disagree
- Update code based on feedback
- Re-request review after changes

## Checklist Before Submitting PR

```markdown
## PR Checklist

### Code Quality
- [ ] Code follows project style guide
- [ ] No linting errors
- [ ] No debug/console statements
- [ ] Functions have clear names
- [ ] Complex logic is commented

### Testing
- [ ] All existing tests pass
- [ ] New tests added for new code
- [ ] Edge cases covered
- [ ] Manual testing completed

### Documentation
- [ ] README updated (if needed)
- [ ] API documentation updated
- [ ] Inline comments for complex logic
- [ ] CHANGELOG updated

### Review
- [ ] PR description is clear
- [ ] Commits are logical
- [ ] Small, focused changes
- [ ] Related issues linked
- [ ] Reviewers assigned

### Security
- [ ] No secrets in code
- [ ] Input validation added
- [ ] Security best practices followed
- [ ] Dependencies up to date
```

## Example PR Templates

### Feature PR

```markdown
## Feature: [Feature Name]

### Summary
Brief description of what this feature does.

### Motivation
Why is this feature needed? What problem does it solve?

### Changes
- Change 1
- Change 2
- Change 3

### Testing
How was this tested?
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

### Screenshots
[Add screenshots for UI changes]

### Related Issues
Closes #123
```

### Bug Fix PR

```markdown
## Bug Fix: [Bug Description]

### Issue
What was the bug?

### Root Cause
What caused the bug?

### Solution
How is it fixed?

### Testing
How did you verify the fix?
- [ ] Reproduction test added
- [ ] Edge cases covered
- [ ] Manual verification

### Closes
Fixes #456
```
