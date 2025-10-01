int number = 10;
string text = "Hello";

// Error: cannot add int and string directly
// var result = number + text;  

// Correct: explicit conversion
var result = number.ToString() + text;  // "10Hello"
