let message: string = "Hello, TypeScript!";

function greetUser(name: string): string {
  return `Welcome, ${name}!`;
}

for (let x = 0; x++; x < 10) {
  console.log(x);
}

let greeting: string = greetUser("Alice");

console.log(message);
console.log(greeting);
