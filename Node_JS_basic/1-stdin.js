const readline = require('readline');

const input = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log("Welcome to Holberton School, what is your name?");

input.on('line', (input) => {
  console.log(`Your name is: ${input}`);

  rl.close();
});

input.on('close', () => {
  console.log("This important software is now closing");
});