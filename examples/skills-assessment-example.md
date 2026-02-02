# Example: Skills Self-Assessment

This example shows how to perform a self-assessment of your developer skills.

## Using Python

```python
from src.utils.developer_tools import assess_skills, calculate_developer_level

# Assess your skills (rate yourself 1-100 in each category)
my_skills = {
    'version_control': 80,    # Git, GitHub workflows
    'programming': 85,         # Coding ability
    'testing': 70,            # Writing and maintaining tests
    'collaboration': 75,      # Teamwork and communication
    'system_design': 65,      # Architecture and design
    'debugging': 80           # Problem-solving
}

# Get assessment
assessment = assess_skills(my_skills)
print(f"Overall Score: {assessment['overall_score']}")
print(f"Strong Areas: {', '.join(assessment['strong_areas'])}")
print(f"Improvement Areas: {', '.join(assessment['improvement_areas'])}")
print(f"Recommendation: {assessment['recommendation']}")

# Calculate your level
level = calculate_developer_level(
    years_experience=4,
    skills_score=assessment['overall_score'],
    impact_score=75
)
print(f"\nYour Developer Level: {level}")
```

## Using JavaScript

```javascript
const { assessSkills, calculateDeveloperLevel } = require('./src/utils/developer_tools');

// Assess your skills (rate yourself 1-100 in each category)
const mySkills = {
  versionControl: 80,    // Git, GitHub workflows
  programming: 85,       // Coding ability
  testing: 70,          // Writing and maintaining tests
  collaboration: 75,    // Teamwork and communication
  systemDesign: 65,     // Architecture and design
  debugging: 80         // Problem-solving
};

// Get assessment
const assessment = assessSkills(mySkills);
console.log(`Overall Score: ${assessment.overallScore}`);
console.log(`Strong Areas: ${assessment.strongAreas.join(', ')}`);
console.log(`Improvement Areas: ${assessment.improvementAreas.join(', ')}`);
console.log(`Recommendation: ${assessment.recommendation}`);

// Calculate your level
const level = calculateDeveloperLevel(4, assessment.overallScore, 75);
console.log(`\nYour Developer Level: ${level}`);
```

## Expected Output

```
Overall Score: 75.83
Strong Areas: version_control, programming, debugging
Improvement Areas: system_design
Recommendation: Good progress. Work on improvement areas to advance to next level.

Your Developer Level: Senior Developer
```

## Next Steps

Based on your assessment:
1. Review the improvement areas
2. Create a development plan (see [development-plan-example.md](./development-plan-example.md))
3. Identify resources to strengthen weak areas
4. Find a mentor in your improvement areas
5. Reassess in 3-6 months
