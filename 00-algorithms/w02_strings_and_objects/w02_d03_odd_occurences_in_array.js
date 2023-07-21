/* 
Given a non-empty array of odd length containing ints where every int but one
belongs to a pair (the int is duplicated once)
return the only int that has no matching pair.
*/
// import { makeFrequencyTable } from "./w02_d02_make_frequency_table";
const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

function makeFrequencyTable(arr) {
    var expected = {};
    for (var i = 0; i < arr.length; i++) {
        // if(expected.hasOwnProperty(arr[i])){
        if (expected[arr[i]]) {
        expected[arr[i]] += 1;
        //
        } else {
        expected[arr[i]] = 1;
        }
    }
    console.log(expected);
    return expected;
}

function oddOccurrencesInArray(nums) {
  freqTab = makeFrequencyTable(nums);
  for(var key in freqTab)
  {
    if (freqTab[key] % 2 != 0) 
    return freqTab[key]
  }
}

console.log(oddOccurrencesInArray(nums1), "should equal", expected1);
console.log(oddOccurrencesInArray(nums2), "should equal", expected2);
console.log(oddOccurrencesInArray(nums3), "should equal", expected3);
console.log(oddOccurrencesInArray(nums4), "should equal", expected4);
