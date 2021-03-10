// https://www.codewars.com/kata/56606694ec01347ce800001b/solutions/javascript

// Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

// (In this case, all triangles must have surface greater than 0 to be accepted).

// The sum of the lengths of any two sides of a triangle is greater than the length of the third side. Similarly, the difference between the lengths of any two sides of a triangle is less than the length of the third side.


const isTriangle = (a, b, c) => {
  console.log(a, b, c)
  if (a === null || b === null || c === null ){
    return 0
  }
  if ((a + b) > c){
  	console.log('1')
  	if ((b+c) > a){
  		console.log('2');
  		if ((a+c) > b){
  			console.log('3');
  			return true
  		} else {
  			return false
  		}
  	} else {
  		return false
  	}
  }  else {
  	return false
  }
}

console.log(isTriangle(1,2,2)); /* => true*/
 /*=> false*/
console.log(isTriangle(7,2,2));

// Test.describe("PublicTest", function() {
//     Test.assertEquals(isTriangle(1,2,2), true);
//     Test.assertEquals(isTriangle(7,2,2), false);
// });