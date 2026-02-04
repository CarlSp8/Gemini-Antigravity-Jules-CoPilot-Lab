#!/usr/bin/env node

/**
 * GitHub Developers Suite - JavaScript Utilities (OPTIMIZED)
 * Helper functions for GitHub developers with performance improvements
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
 * Assess developer skills across different categories - OPTIMIZED
 * 
 * Improvements:
 * - Single pass through entries instead of multiple passes
 * - More efficient filtering and aggregation
 * 
 * @param {Object} skills - Object with skill categories and scores
 * @returns {Object} Assessment results
 */
function assessSkills(skills) {
  if (!skills || Object.keys(skills).length === 0) {
    return { error: "No skills provided" };
  }
  
  // OPTIMIZED: Single pass through entries instead of multiple passes
  let totalScore = 0;
  const weakAreas = [];
  const strongAreas = [];
  
  for (const [skill, score] of Object.entries(skills)) {
    totalScore += score;
    if (score < 70) {
      weakAreas.push(skill);
    }
    if (score >= 85) {
      strongAreas.push(skill);
    }
  }
  
  const overallScore = totalScore / Object.keys(skills).length;
  
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

// OPTIMIZED: Cache milestones at module level to avoid recreating on every call
const LEVEL_MILESTONES = {
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

const LEVELS = ["Junior", "Mid-Level", "Senior", "Staff", "Principal"];

/**
 * Create a development plan - OPTIMIZED
 * 
 * Improvements:
 * - Uses cached milestone data at module level
 * - More efficient level index lookup
 * 
 * @param {string} currentLevel - Current developer level
 * @param {string} targetLevel - Target developer level
 * @param {number} timelineMonths - Timeline in months
 * @returns {Object} Development plan
 */
function createDevelopmentPlan(currentLevel, targetLevel, timelineMonths) {
  // OPTIMIZED: More efficient index finding
  let currentIdx = -1;
  let targetIdx = -1;
  
  for (let i = 0; i < LEVELS.length; i++) {
    if (currentLevel.includes(LEVELS[i]) && currentIdx === -1) {
      currentIdx = i;
    }
    if (targetLevel.includes(LEVELS[i]) && targetIdx === -1) {
      targetIdx = i;
    }
  }
  
  if (currentIdx === -1) currentIdx = 0;
  if (targetIdx === -1) targetIdx = 0;
  
  if (targetIdx <= currentIdx) {
    return { error: "Target level must be higher than current level" };
  }
  
  const targetLevelKey = LEVELS[targetIdx];
  const levelMilestones = LEVEL_MILESTONES[targetLevelKey] || [];
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
 * Calculate PR quality score - OPTIMIZED
 * 
 * Improvements:
 * - Early extraction of values to avoid repeated property access
 * - More efficient score calculation logic
 * 
 * @param {Object} prData - Pull request data
 * @returns {Object} Quality score and feedback
 */
function calculatePRQualityScore(prData) {
  // OPTIMIZED: Extract all values once at the beginning
  const linesChanged = prData.linesChanged || 0;
  const hasTests = prData.hasTests || false;
  const description = prData.description || "";
  const commentsAddressed = prData.commentsAddressed || 0;
  const totalComments = prData.totalComments || 0;
  
  let score = 100;
  const feedback = [];
  
  // Check PR size
  if (linesChanged > 500) {
    score -= 20;
    feedback.push("PR is too large. Consider breaking into smaller PRs.");
  } else if (linesChanged > 200) {
    score -= 10;
    feedback.push("PR is moderately large. Ensure it's focused.");
  }
  
  // Check tests
  if (!hasTests) {
    score -= 30;
    feedback.push("No tests included. Add tests for new functionality.");
  }
  
  // Check description
  if (description.length < 50) {
    score -= 15;
    feedback.push("Add more detailed PR description.");
  }
  
  // Check review comments
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
  console.log("GitHub Developers Suite - JavaScript Utilities (Optimized)\n");
  
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
