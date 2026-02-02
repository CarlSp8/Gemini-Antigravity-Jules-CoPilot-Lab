#!/usr/bin/env node

/**
 * GitHub Developers Suite - JavaScript Utilities
 * Helper functions for GitHub developers working with JavaScript
 */

/**
 * Calculate developer level based on experience and skills
 * @param {number} yearsExperience - Years of professional experience
 * @param {number} skillsScore - Technical skills score (1-100)
 * @param {number} impactScore - Impact and collaboration score (1-100)
 * @returns {string} Developer level
 */
function calculateDeveloperLevel(yearsExperience, skillsScore, impactScore) {
  const totalScore = (yearsExperience * 10) + (skillsScore * 0.5) + (impactScore * 0.5);
  
  if (totalScore < 30) return "Junior Developer";
  if (totalScore < 60) return "Mid-Level Developer";
  if (totalScore < 90) return "Senior Developer";
  if (totalScore < 120) return "Staff Developer";
  return "Principal Developer";
}

/**
 * Assess developer skills across different categories
 * @param {Object} skills - Object with skill categories and scores
 * @returns {Object} Assessment results
 */
function assessSkills(skills) {
  if (!skills || Object.keys(skills).length === 0) {
    return { error: "No skills provided" };
  }
  
  const scores = Object.values(skills);
  const overallScore = scores.reduce((a, b) => a + b, 0) / scores.length;
  
  const weakAreas = Object.entries(skills)
    .filter(([, score]) => score < 70)
    .map(([skill]) => skill);
  
  const strongAreas = Object.entries(skills)
    .filter(([, score]) => score >= 85)
    .map(([skill]) => skill);
  
  return {
    overallScore: Math.round(overallScore * 100) / 100,
    strongAreas,
    improvementAreas: weakAreas,
    recommendation: getRecommendation(overallScore)
  };
}

/**
 * Get recommendation based on score
 * @param {number} score - Overall score
 * @returns {string} Recommendation
 */
function getRecommendation(score) {
  if (score >= 90) return "Excellent! Focus on mentoring and leading technical initiatives.";
  if (score >= 75) return "Good progress. Work on improvement areas to advance to next level.";
  if (score >= 60) return "Solid foundation. Focus on strengthening weak areas.";
  return "Keep learning! Focus on fundamentals and seek mentorship.";
}

/**
 * Create a development plan
 * @param {string} currentLevel - Current developer level
 * @param {string} targetLevel - Target developer level
 * @param {number} timelineMonths - Timeline in months
 * @returns {Object} Development plan
 */
function createDevelopmentPlan(currentLevel, targetLevel, timelineMonths) {
  const levels = ["Junior", "Mid-Level", "Senior", "Staff", "Principal"];
  
  const currentIdx = levels.findIndex(lvl => currentLevel.includes(lvl));
  const targetIdx = levels.findIndex(lvl => targetLevel.includes(lvl));
  
  if (targetIdx <= currentIdx) {
    return { error: "Target level must be higher than current level" };
  }
  
  const milestones = {
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
  };
  
  const targetLevelKey = levels[targetIdx];
  const levelMilestones = milestones[targetLevelKey] || [];
  const monthsPerMilestone = Math.max(1, Math.floor(timelineMonths / 4));
  
  return {
    currentLevel,
    targetLevel,
    timelineMonths,
    milestones: levelMilestones,
    monthsPerMilestone,
    nextSteps: levelMilestones.map((milestone, i) => 
      `Month ${i * monthsPerMilestone + 1}: ${milestone}`
    )
  };
}

/**
 * Calculate PR quality score
 * @param {Object} prData - Pull request data
 * @returns {Object} Quality score and feedback
 */
function calculatePRQualityScore(prData) {
  let score = 100;
  const feedback = [];
  
  // Check PR size
  const linesChanged = prData.linesChanged || 0;
  if (linesChanged > 500) {
    score -= 20;
    feedback.push("PR is too large. Consider breaking into smaller PRs.");
  } else if (linesChanged > 200) {
    score -= 10;
    feedback.push("PR is moderately large. Ensure it's focused.");
  }
  
  // Check tests
  if (!prData.hasTests) {
    score -= 30;
    feedback.push("No tests included. Add tests for new functionality.");
  }
  
  // Check description
  const descLength = (prData.description || "").length;
  if (descLength < 50) {
    score -= 15;
    feedback.push("Add more detailed PR description.");
  }
  
  // Check review comments
  const { commentsAddressed = 0, totalComments = 0 } = prData;
  if (totalComments > 0 && commentsAddressed < totalComments) {
    score -= 10;
    feedback.push("Address all review comments.");
  }
  
  const qualityLevel = score >= 90 ? "Excellent" : score >= 75 ? "Good" : "Needs Improvement";
  
  return {
    score: Math.max(0, score),
    qualityLevel,
    feedback: feedback.length ? feedback : ["Great PR! No major issues."]
  };
}

// Export for use as module
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    calculateDeveloperLevel,
    assessSkills,
    createDevelopmentPlan,
    calculatePRQualityScore
  };
}

// Example usage
if (require.main === module) {
  console.log("GitHub Developers Suite - JavaScript Utilities\n");
  
  // Example 1: Calculate developer level
  const level = calculateDeveloperLevel(3, 75, 70);
  console.log(`Developer Level: ${level}\n`);
  
  // Example 2: Assess skills
  const skills = {
    versionControl: 85,
    programming: 90,
    testing: 65,
    collaboration: 80
  };
  const assessment = assessSkills(skills);
  console.log("Skills Assessment:", assessment, "\n");
  
  // Example 3: Create development plan
  const plan = createDevelopmentPlan("Junior Developer", "Senior Developer", 24);
  console.log("Development Plan:", plan, "\n");
  
  // Example 4: Calculate PR quality
  const pr = {
    linesChanged: 150,
    hasTests: true,
    description: "Added user authentication feature with OAuth 2.0 support.",
    commentsAddressed: 5,
    totalComments: 5
  };
  const quality = calculatePRQualityScore(pr);
  console.log("PR Quality Score:", quality);
}
