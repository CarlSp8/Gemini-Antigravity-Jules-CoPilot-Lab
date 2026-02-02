# Developer Utilities - API Reference

This document provides a complete API reference for the developer utilities available in both Python and JavaScript.

## Python API (`src/utils/developer_tools.py`)

### Functions

#### `calculate_developer_level(years_experience, skills_score, impact_score)`

Calculate developer level based on experience and skills.

**Parameters:**
- `years_experience` (int): Years of professional experience
- `skills_score` (int): Technical skills score (1-100)
- `impact_score` (int): Impact and collaboration score (1-100)

**Returns:** str - Developer level (Junior, Mid-Level, Senior, Staff, Principal)

**Example:**
```python
level = calculate_developer_level(years_experience=3, skills_score=75, impact_score=70)
print(level)  # Output: "Senior Developer"
```

---

#### `assess_skills(skills_dict)`

Assess developer skills across different categories.

**Parameters:**
- `skills_dict` (dict): Dictionary of skill categories and scores
  ```python
  {
      'version_control': 85,
      'programming': 90,
      'testing': 75,
      'collaboration': 80
  }
  ```

**Returns:** dict - Assessment results
```python
{
    'overall_score': 82.5,
    'strong_areas': ['version_control', 'programming'],
    'improvement_areas': ['testing'],
    'recommendation': 'Good progress. Work on improvement areas...'
}
```

**Example:**
```python
skills = {
    'version_control': 85,
    'programming': 90,
    'testing': 65,
    'collaboration': 80
}
assessment = assess_skills(skills)
print(f"Overall Score: {assessment['overall_score']}")
```

---

#### `create_development_plan(current_level, target_level, timeline_months)`

Create a development plan to progress from current to target level.

**Parameters:**
- `current_level` (str): Current developer level
- `target_level` (str): Target developer level  
- `timeline_months` (int): Timeline in months

**Returns:** dict - Development plan
```python
{
    'current_level': 'Junior Developer',
    'target_level': 'Senior Developer',
    'timeline_months': 24,
    'milestones': [...],
    'months_per_milestone': 6,
    'next_steps': [...]
}
```

**Example:**
```python
plan = create_development_plan("Junior Developer", "Senior Developer", 24)
for step in plan['next_steps']:
    print(step)
```

---

#### `calculate_pr_quality_score(pr_data)`

Calculate pull request quality score.

**Parameters:**
- `pr_data` (dict): PR data
  ```python
  {
      'lines_changed': 150,
      'has_tests': True,
      'description': 'PR description...',
      'comments_addressed': 5,
      'total_comments': 5
  }
  ```

**Returns:** dict - Quality score and feedback
```python
{
    'score': 90,
    'quality_level': 'Excellent',
    'feedback': [...]
}
```

**Example:**
```python
pr = {
    'lines_changed': 150,
    'has_tests': True,
    'description': 'Added authentication feature',
    'comments_addressed': 5,
    'total_comments': 5
}
quality = calculate_pr_quality_score(pr)
print(f"Score: {quality['score']}/100")
```

---

## JavaScript API (`src/utils/developer_tools.js`)

### Functions

#### `calculateDeveloperLevel(yearsExperience, skillsScore, impactScore)`

Calculate developer level based on experience and skills.

**Parameters:**
- `yearsExperience` (number): Years of professional experience
- `skillsScore` (number): Technical skills score (1-100)
- `impactScore` (number): Impact and collaboration score (1-100)

**Returns:** string - Developer level

**Example:**
```javascript
const level = calculateDeveloperLevel(3, 75, 70);
console.log(level);  // Output: "Senior Developer"
```

---

#### `assessSkills(skills)`

Assess developer skills across different categories.

**Parameters:**
- `skills` (Object): Object with skill categories and scores
  ```javascript
  {
    versionControl: 85,
    programming: 90,
    testing: 75,
    collaboration: 80
  }
  ```

**Returns:** Object - Assessment results
```javascript
{
  overallScore: 82.5,
  strongAreas: ['versionControl', 'programming'],
  improvementAreas: ['testing'],
  recommendation: 'Good progress. Work on improvement areas...'
}
```

**Example:**
```javascript
const skills = {
  versionControl: 85,
  programming: 90,
  testing: 65,
  collaboration: 80
};
const assessment = assessSkills(skills);
console.log(`Overall Score: ${assessment.overallScore}`);
```

---

#### `createDevelopmentPlan(currentLevel, targetLevel, timelineMonths)`

Create a development plan to progress from current to target level.

**Parameters:**
- `currentLevel` (string): Current developer level
- `targetLevel` (string): Target developer level
- `timelineMonths` (number): Timeline in months

**Returns:** Object - Development plan
```javascript
{
  currentLevel: 'Junior Developer',
  targetLevel: 'Senior Developer',
  timelineMonths: 24,
  milestones: [...],
  monthsPerMilestone: 6,
  nextSteps: [...]
}
```

**Example:**
```javascript
const plan = createDevelopmentPlan("Junior Developer", "Senior Developer", 24);
plan.nextSteps.forEach(step => console.log(step));
```

---

#### `calculatePRQualityScore(prData)`

Calculate pull request quality score.

**Parameters:**
- `prData` (Object): PR data
  ```javascript
  {
    linesChanged: 150,
    hasTests: true,
    description: 'PR description...',
    commentsAddressed: 5,
    totalComments: 5
  }
  ```

**Returns:** Object - Quality score and feedback
```javascript
{
  score: 90,
  qualityLevel: 'Excellent',
  feedback: [...]
}
```

**Example:**
```javascript
const pr = {
  linesChanged: 150,
  hasTests: true,
  description: 'Added authentication feature',
  commentsAddressed: 5,
  totalComments: 5
};
const quality = calculatePRQualityScore(pr);
console.log(`Score: ${quality.score}/100`);
```

---

## Usage Examples

### Complete Python Script

```python
#!/usr/bin/env python3
from src.utils.developer_tools import (
    calculate_developer_level,
    assess_skills,
    create_development_plan,
    calculate_pr_quality_score
)

# Your skills
my_skills = {
    'version_control': 80,
    'programming': 85,
    'testing': 70,
    'collaboration': 75,
    'system_design': 65
}

# Assess skills
assessment = assess_skills(my_skills)
print(f"Overall Score: {assessment['overall_score']}")
print(f"Areas to improve: {', '.join(assessment['improvement_areas'])}")

# Calculate level
level = calculate_developer_level(
    years_experience=4,
    skills_score=assessment['overall_score'],
    impact_score=75
)
print(f"Current Level: {level}")

# Create development plan
plan = create_development_plan(level, "Staff Developer", 24)
print(f"\nDevelopment Plan:")
for step in plan['next_steps']:
    print(f"  - {step}")

# Check PR quality
pr = {
    'lines_changed': 200,
    'has_tests': True,
    'description': 'Implemented new feature with comprehensive tests',
    'comments_addressed': 5,
    'total_comments': 5
}
quality = calculate_pr_quality_score(pr)
print(f"\nPR Quality: {quality['score']}/100 ({quality['quality_level']})")
```

### Complete JavaScript Script

```javascript
const {
  calculateDeveloperLevel,
  assessSkills,
  createDevelopmentPlan,
  calculatePRQualityScore
} = require('./src/utils/developer_tools');

// Your skills
const mySkills = {
  versionControl: 80,
  programming: 85,
  testing: 70,
  collaboration: 75,
  systemDesign: 65
};

// Assess skills
const assessment = assessSkills(mySkills);
console.log(`Overall Score: ${assessment.overallScore}`);
console.log(`Areas to improve: ${assessment.improvementAreas.join(', ')}`);

// Calculate level
const level = calculateDeveloperLevel(4, assessment.overallScore, 75);
console.log(`Current Level: ${level}`);

// Create development plan
const plan = createDevelopmentPlan(level, "Staff Developer", 24);
console.log('\nDevelopment Plan:');
plan.nextSteps.forEach(step => console.log(`  - ${step}`));

// Check PR quality
const pr = {
  linesChanged: 200,
  hasTests: true,
  description: 'Implemented new feature with comprehensive tests',
  commentsAddressed: 5,
  totalComments: 5
};
const quality = calculatePRQualityScore(pr);
console.log(`\nPR Quality: ${quality.score}/100 (${quality.qualityLevel})`);
```

---

## Common Patterns

### Skills Assessment Workflow

```python
# 1. Self-assess skills
skills = {...}

# 2. Get assessment
assessment = assess_skills(skills)

# 3. Identify improvement areas
weak_skills = assessment['improvement_areas']

# 4. Focus development efforts
for skill in weak_skills:
    print(f"TODO: Improve {skill}")
```

### Career Progression Workflow

```python
# 1. Determine current level
level = calculate_developer_level(years, skills, impact)

# 2. Choose target level
target = "Senior Developer"

# 3. Create plan
plan = create_development_plan(level, target, 24)

# 4. Execute milestones
for milestone in plan['milestones']:
    print(f"Work on: {milestone}")
```

### PR Quality Workflow

```javascript
// 1. Gather PR data
const prData = getPRData();

// 2. Check quality
const quality = calculatePRQualityScore(prData);

// 3. Review feedback
if (quality.score < 75) {
  console.log("Improvements needed:");
  quality.feedback.forEach(f => console.log(`  - ${f}`));
}

// 4. Make improvements
// ... address feedback ...

// 5. Re-check
const updatedQuality = calculatePRQualityScore(updatedPRData);
```

---

## Tips

1. **Regular Assessment**: Run skills assessment quarterly to track progress
2. **Realistic Scoring**: Be honest in self-assessment (60-70 is good!)
3. **Small PRs**: Keep PRs under 200 lines when possible
4. **Continuous Improvement**: Use the tools regularly, not just once
5. **Share Results**: Discuss with mentors or managers for alignment

## See Also

- [Getting Started Guide](./GETTING_STARTED.md)
- [Examples Directory](./examples/)
- [Developer Levels](./docs/level-developers/README.md)
- [PDH Documentation](./docs/pdh/README.md)
