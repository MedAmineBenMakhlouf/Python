/*Book Index

Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

const nums2 = [5, 6, 7, 8, 9];
const expected2 = "5-9";

const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
const expected3 = "1-3, 7, 9, 15-17";


// function bookIndex(nums) {
//     tableau= []
//     debut = nums[0]

//     fin = nums[0]
//     for (var i=1; i<=nums.length-1;i++)
//     {
        
//         if(nums[i]-nums[i-1]==1)
//         {
//             fin = nums[i]
//         }
//         else
//         {
//             tableau.push(debut[i]+"-"+fin[i])
//             debut = nums[i]
//             fin = nums[i]

//         }
        
//     }
    
//     // expected = ch[0]+"-"+ch[ch.length-1]
//     return tableau
// }



// function bookIndex(nums) {
//     myString =""
//     for(var i = 0; i < nums.length; i++ ){
//         if( nums[i] != nums[i - 1] + 1) {
//             if(i != 0){
//                 myString +=', '
//             }
//             myString += nums[i]
//             } else if ( nums[i] != nums[i + 1] - 1) {
//                 myString += '-' + nums[i];
//             }
//     }
//     return myString
// }


console.log(bookIndex(nums3));