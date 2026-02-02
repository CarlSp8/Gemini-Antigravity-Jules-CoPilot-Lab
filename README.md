<div align="center">

<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />

  <h1>GitHub Developers Suite</h1>

  <p>A comprehensive toolkit for professional development, career progression, and excellence in software development.</p>

</div>

---

## 📖 Documentation

- **[Getting Started Guide](./GETTING_STARTED.md)** - Quick start guide for new users
- **[API Reference](./API_REFERENCE.md)** - Complete API documentation for utilities

---

## 📚 Overview

The **GitHub Developers Suite** is a complete framework designed to help developers at all levels grow their skills, advance their careers, and maintain high standards of excellence. This suite includes:

- **Professional Development Handbook (PDH)** - Best practices, guidelines, and resources for technical excellence
- **Level Developers Framework** - Clear career progression paths with skills assessment and development planning
- **Developer Utilities** - Practical tools for self-assessment and quality measurement

## 🎯 Key Features

### Professional Development Handbook (PDH)
Comprehensive guidance on:
- Version control mastery and Git workflows
- Code review excellence
- Technical and soft skills development
- Career advancement strategies

[📖 Read the PDH →](./docs/pdh/README.md)

### Level Developers Framework
Structured career progression:
- **Level 1:** Junior Developer (0-2 years)
- **Level 2:** Mid-Level Developer (2-5 years)
- **Level 3:** Senior Developer (5-8 years)
- **Level 4:** Staff/Principal Developer (8+ years)

Each level includes specific competencies, growth areas, and advancement criteria.

[📊 Explore Developer Levels →](./docs/level-developers/README.md)

### Developer Utilities
Practical tools for:
- Skills self-assessment
- Career development planning
- PR quality evaluation
- Level calculation

Available in Python and JavaScript!

[🛠️ View Utilities →](./src/utils/)

## 🚀 Quick Start

### 1. Assess Your Skills
```python
# Python example
from src.utils.developer_tools import assess_skills

my_skills = {
    'version_control': 80,
    'programming': 85,
    'testing': 70,
    'collaboration': 75
}

assessment = assess_skills(my_skills)
print(assessment)
```

### 2. Create a Development Plan
```javascript
// JavaScript example
const { createDevelopmentPlan } = require('./src/utils/developer_tools');

const plan = createDevelopmentPlan(
  "Junior Developer",
  "Senior Developer",
  24
);
console.log(plan);
```

### 3. Check Your PR Quality
```python
from src.utils.developer_tools import calculate_pr_quality_score

pr_data = {
    'lines_changed': 150,
    'has_tests': True,
    'description': 'Added authentication feature with tests',
    'comments_addressed': 5,
    'total_comments': 5
}

quality = calculate_pr_quality_score(pr_data)
print(f"Quality Score: {quality['score']}/100")
```

## 📋 Documentation Structure

```
├── docs/
│   ├── pdh/                          # Professional Development Handbook
│   │   ├── README.md                 # PDH Overview
│   │   ├── git-best-practices.md     # Git guidelines
│   │   └── code-review-guide.md      # Code review standards
│   │
│   └── level-developers/             # Developer Levels Framework
│       ├── README.md                 # Levels overview
│       ├── skill-development.md      # Skill building guide
│       ├── career-progression.md     # Career paths
│       └── mentorship.md             # Mentorship guide
│
├── src/
│   └── utils/                        # Utility tools
│       ├── developer_tools.py        # Python utilities
│       └── developer_tools.js        # JavaScript utilities
│
└── examples/                         # Usage examples
    ├── skills-assessment-example.md
    ├── development-plan-example.md
    └── pr-quality-check-example.md
```

## 💡 Use Cases

### For Junior Developers
- Understand what's expected at your level
- Create a clear path to mid-level
- Learn Git and code review best practices
- Track your skill development

### For Mid-Level Developers
- Identify skills needed for senior level
- Build mentoring capabilities
- Strengthen architectural thinking
- Plan your career progression

### For Senior+ Developers
- Guide and mentor team members
- Establish team standards
- Assess team skill levels
- Drive technical excellence

### For Managers
- Evaluate developer levels objectively
- Create career development plans
- Set clear expectations
- Track team growth

## 🎓 Learning Paths

1. **Git Mastery Path**
   - [Git Best Practices](./docs/pdh/git-best-practices.md)
   - [Code Review Guide](./docs/pdh/code-review-guide.md)

2. **Career Growth Path**
   - [Developer Levels](./docs/level-developers/README.md)
   - [Career Progression](./docs/level-developers/career-progression.md)
   - [Skill Development](./docs/level-developers/skill-development.md)

3. **Leadership Path**
   - [Mentorship Guide](./docs/level-developers/mentorship.md)
   - [Code Review Guide](./docs/pdh/code-review-guide.md)

## 🤝 Contributing

Contributions are welcome! Whether it's:
- Adding new utilities
- Improving documentation
- Sharing best practices
- Reporting issues

## 📝 Examples

Check out the [examples](./examples/) directory for practical demonstrations:
- [Skills Assessment Example](./examples/skills-assessment-example.md)
- [Development Plan Example](./examples/development-plan-example.md)
- [PR Quality Check Example](./examples/pr-quality-check-example.md)

## 📄 License

This project is open source and available for use by all GitHub developers.

---

<div align="center">
  <p>Built with ❤️ for the developer community</p>
  <p><a href="https://aistudio.google.com/apps">Powered by AI Studio</a></p>
</div>
