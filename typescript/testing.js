// Declare a variable with a type annotation
var message = "Hello, TypeScript!";
// Define a function with typed parameters and a return type
function greetUser(name) {
    return "Welcome, ".concat(name, "!");
}
// Call the function and store the result in a typed variable
var greeting = greetUser("Alice");
// Log the variables to the console
console.log(message);
console.log(greeting);
// Demonstrate a potential type error (commented out)
// message = 123; // This would cause a TypeScript error because 'message' is a string
