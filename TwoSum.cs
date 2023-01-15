/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.*/


/*Approach 

hashTable ={}
nums = [2,7,11,15], target = 9

for each num in nums => 2
    The result of "target" minus the "current element", is the index we're looking, cause this index gives the element that sum with the current value (nums[i]), results in the target;
    Here we just look for the result of the complement variable, that sums with the current value (nums[i]) results in the target.
    If not has the complement, just add in the hash table
*/

public class Solution {
    public int[] TwoSum(int[] nums, int target) {

      var hashTable = new Dictionary<int,int>();

      for(int i=0; i< nums.Length; i++)
      {
        var complement = target - nums[i]; 

        if(hashTable.ContainsKey(complement)) 
        {
            return new int[] {hashTable[complement],i};
        }else{
            hashTable[nums[i]] = i; 
        }
      }
    }
}
