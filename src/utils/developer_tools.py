"""
GitHub Developers Suite - Utility Functions
A collection of utility functions for GitHub developers
"""

def calculate_developer_level(years_experience, skills_score, impact_score):
    """
    Calculate developer level based on experience and skills
    
    Args:
        years_experience (int): Years of professional experience
        skills_score (int): Technical skills score (1-100)
        impact_score (int): Impact and collaboration score (1-100)
    
    Returns:
        str: Developer level (Junior, Mid, Senior, Staff, Principal)
    """
    total_score = (years_experience * 10) + (skills_score * 0.5) + (impact_score * 0.5)
    
    if total_score < 30:
        return "Junior Developer"
    elif total_score < 60:
        return "Mid-Level Developer"
    elif total_score < 90:
        return "Senior Developer"
    elif total_score < 120:
        return "Staff Developer"
    else:
        return "Principal Developer"


def assess_skills(skills_dict):
    """
    Assess developer skills across different categories
    
    Args:
        skills_dict (dict): Dictionary of skill categories and scores
            Example: {
                'version_control': 85,
                'programming': 90,
                'testing': 75,
                'collaboration': 80
            }
    
    Returns:
        dict: Assessment results with overall score and recommendations
    """
    if not skills_dict:
        return {"error": "No skills provided"}
    
    overall_score = sum(skills_dict.values()) / len(skills_dict)
    weak_areas = [skill for skill, score in skills_dict.items() if score < 70]
    strong_areas = [skill for skill, score in skills_dict.items() if score >= 85]
    
    return {
        'overall_score': round(overall_score, 2),
        'strong_areas': strong_areas,
        'improvement_areas': weak_areas,
        'recommendation': get_recommendation(overall_score)
    }


def get_recommendation(score):
    """Get recommendation based on overall score"""
    if score >= 90:
        return "Excellent! Focus on mentoring and leading technical initiatives."
    elif score >= 75:
        return "Good progress. Work on improvement areas to advance to next level."
    elif score >= 60:
        return "Solid foundation. Focus on strengthening weak areas."
    else:
        return "Keep learning! Focus on fundamentals and seek mentorship."


def create_development_plan(current_level, target_level, timeline_months):
    """
    Create a development plan to progress from current to target level
    
    Args:
        current_level (str): Current developer level
        target_level (str): Target developer level
        timeline_months (int): Timeline in months
    
    Returns:
        dict: Development plan with milestones and goals
    """
    levels = ["Junior", "Mid-Level", "Senior", "Staff", "Principal"]
    
    # Find level indices
    current_idx = next((i for i, lvl in enumerate(levels) if lvl in current_level), 0)
    target_idx = next((i for i, lvl in enumerate(levels) if lvl in target_level), 0)
    
    if target_idx <= current_idx:
        return {"error": "Target level must be higher than current level"}
    
    milestones_per_level = {
        "Junior": [
            "Master Git basics",
            "Write clean, functional code",
            "Complete code reviews",
            "Document work clearly"
        ],
        "Mid-Level": [
            "Design features independently",
            "Lead small projects",
            "Mentor junior developers",
            "Optimize code performance"
        ],
        "Senior": [
            "Design system architecture",
            "Lead technical decisions",
            "Mentor multiple developers",
            "Drive technical excellence"
        ],
        "Staff": [
            "Define technical strategy",
            "Lead cross-team initiatives",
            "Mentor senior developers",
            "Drive organizational impact"
        ]
    }
    
    months_per_milestone = max(1, timeline_months // 4)
    
    target_level_key = levels[target_idx]
    milestones = milestones_per_level.get(target_level_key, [])
    
    return {
        'current_level': current_level,
        'target_level': target_level,
        'timeline_months': timeline_months,
        'milestones': milestones,
        'months_per_milestone': months_per_milestone,
        'next_steps': [
            f"Month {i*months_per_milestone + 1}: {milestone}"
            for i, milestone in enumerate(milestones)
        ]
    }


def calculate_pr_quality_score(pr_data):
    """
    Calculate pull request quality score
    
    Args:
        pr_data (dict): PR data including size, tests, comments, etc.
    
    Returns:
        dict: Quality score and feedback
    """
    score = 100
    feedback = []
    
    # Check PR size (smaller is better)
    lines_changed = pr_data.get('lines_changed', 0)
    if lines_changed > 500:
        score -= 20
        feedback.append("PR is too large. Consider breaking into smaller PRs.")
    elif lines_changed > 200:
        score -= 10
        feedback.append("PR is moderately large. Ensure it's focused.")
    
    # Check tests
    has_tests = pr_data.get('has_tests', False)
    if not has_tests:
        score -= 30
        feedback.append("No tests included. Add tests for new functionality.")
    
    # Check description
    description_length = len(pr_data.get('description', ''))
    if description_length < 50:
        score -= 15
        feedback.append("Add more detailed PR description.")
    
    # Check review comments addressed
    comments_addressed = pr_data.get('comments_addressed', 0)
    total_comments = pr_data.get('total_comments', 0)
    if total_comments > 0 and comments_addressed < total_comments:
        score -= 10
        feedback.append("Address all review comments.")
    
    quality_level = "Excellent" if score >= 90 else "Good" if score >= 75 else "Needs Improvement"
    
    return {
        'score': max(0, score),
        'quality_level': quality_level,
        'feedback': feedback if feedback else ["Great PR! No major issues."]
    }


if __name__ == "__main__":
    # Example usage
    print("GitHub Developers Suite - Utility Examples\n")
    
    # Example 1: Calculate developer level
    level = calculate_developer_level(years_experience=3, skills_score=75, impact_score=70)
    print(f"Developer Level: {level}\n")
    
    # Example 2: Assess skills
    skills = {
        'version_control': 85,
        'programming': 90,
        'testing': 65,
        'collaboration': 80
    }
    assessment = assess_skills(skills)
    print(f"Skills Assessment: {assessment}\n")
    
    # Example 3: Create development plan
    plan = create_development_plan("Junior Developer", "Senior Developer", 24)
    print(f"Development Plan: {plan}\n")
    
    # Example 4: Calculate PR quality
    pr = {
        'lines_changed': 150,
        'has_tests': True,
        'description': 'Added user authentication feature with OAuth 2.0 support. Includes comprehensive tests.',
        'comments_addressed': 5,
        'total_comments': 5
    }
    quality = calculate_pr_quality_score(pr)
    print(f"PR Quality Score: {quality}")
