/**
 * Determines whether or not the strings are equal, ignoring case.
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */

var strA1 = "ABC";
var strB1 = "abc";
var expected1 = true;

var strA2 = "ABC";
var strB2 = "abd";
var expected2 = false;

var strA3 = "ABC";
var strB3 = "bc";
var expected3 = false;

var strA4 = "Dad ";
var strB4 = " dAd";
var expected3 = true;

function caseInsensitiveStringCompare(strA, strB) {
    if(strA.length-1 != strB.length-1)
    {
        return false
    }
    else{
        strA = strA.trim()
        strB = strB.trim()
        for(var i=0;i<strA.length;i++)
        {
            if(strA[i].toUpperCase()!=strB[i].toUpperCase())
            return false
        }
        return true
    }
}
result1 = caseInsensitiveStringCompare(strA1, strB1)
result2 = caseInsensitiveStringCompare(strA2, strB2)
result3 = caseInsensitiveStringCompare(strA3, strB3)
result4 = caseInsensitiveStringCompare(strA4, strB4)
console.log(result1)
console.log(result2)
console.log(result3)
console.log(result4)