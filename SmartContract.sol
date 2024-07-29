// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract SolidityTest {
   constructor() {

   }
   function printName() public pure returns (string memory) {
        return "Anvita Kumar";
   }
   function getResult() public pure returns(uint){
      uint a = 1;
      uint b = 2;
      uint result = a + b;
      return result;
   }
   function isPalindrome(uint num) public pure returns(bool){
        uint numOfDigits = numDigits(num);
        uint i = 0;
        uint rightNum = 0;
        while (i < numOfDigits / 2) {
            uint temp = num % 10;
            rightNum += (10 ** (numOfDigits / 2 - (i + 1))) * temp;
            num = num / 10;
            i++;
        }
        i = 0;
        if (numOfDigits % 2 == 1) num = num / 10;
        if (num == rightNum) return true;
        else return false;
   }
   function numDigits(uint num) private pure returns (uint) {
    uint numOfDigits = 0;
    while (num != 0) {
        num /= 10;
        numOfDigits++;
    }
    return  numOfDigits;
   }
   function distinct(uint[] memory values, uint n) public pure returns (uint) {
      uint num = 0;
      for (uint i = 0; i < n; i++) {
         bool isDistinct = true;
         for (uint j = 0; j < i; j++) {
            if (values[i] == values[j]) {
               isDistinct = false;
               break;
            }
         }
         if (isDistinct) {
            num++;
         }
      }
      return num;
   }
   function concatenateStrings(string memory s1, string memory s2) public pure returns (string memory) {
      return string.concat(s1, s2);
   }
}