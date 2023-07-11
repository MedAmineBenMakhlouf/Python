/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

let str1 = "object oriented programming";
let expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

function acronymize(str) {
  var acro = "";
  var ch = "";
  acro = str.split(" ");

  for (var i = 0; i <= acro.length - 1; i++) {
    if (acro[i] != "") ch += acro[i][0];
  }
  console.log(ch.toUpperCase());
}

function acronymize2(str)
{
  var result=""
  if(str[0]!=" ")
  {
    result+= str[0].toUpperCase()
  }
  for(var i=1;i<str.length-2;i++)
  {
    if(str[i]==" " && str[i+1]!=" ")
    result+=str[i+1].toUpperCase()
  }
  console.log(result)
}
acronymize(str1);
acronymize(str2);
acronymize(str3);
acronymize(str4);
