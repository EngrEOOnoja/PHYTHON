const prompt = require("prompt-sync")();
function getScore() {  rl.question('Please enter a value between 0 and 100: ', score => {
score = parseInt(score);
 if (score >= 0 && score <= 100) {
let grade = calculateGrade(score);
let feedback = getFeedback(grade);
console.log(`Grade: ${grade}`);
console.log(`Feedback: ${feedback}`);
 askAgain();
    } else {
 console.log('Invalid input. Please try again.');
getScore();
 }
  });
}



function calculateGrade(score) {
  if (score >= 90) {
    return 'A';
  } else if (score >= 80) {
    return 'B';
  } else if (score >= 70) {
    return 'C';
  } else if (score >= 60) {
    return 'D';
  } else {
    return 'F';
  }
}



function getFeedback(grade) {
  if (grade === 'A') {
    return 'Excellent performance';
  } else if (grade === 'B') {
    return 'Good job, Keep improving';
  } else if (grade === 'C') {
    return 'Fair effort, keep working on it';
  } else if (grade === 'D') {
    return 'You can do better, don’t give up';
  } else {
    return 'Needs Improvement, Ask for help';
  }
}





function askAgain() {
 rl.question('Try another score? (yes/no): ', answer => {
 if (answer.toLowerCase() === 'yes') {
 getScore();
 } else {
 rl.close();
 }
 });
}

getScore();
















const prompt = require("prompt-sync")();

let value = prompt("Enter your score between 0 and 100: ")
console.log(`Congratulatios you got ${value} as your score`)
