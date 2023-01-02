/*

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

*/

public class Solution {
    public int[] TwoSum(int[] nums, int target) {

      var hashTable = new Dictionary<int,int>(); //Using hashtable to store the index

      for(int i=0; i< nums.Length; i++)
      {
        // The result of "target" minus the "current element", is the index we're looking, cause this index gives the element that sum with the current value (nums[i]), results in the target;
        var complement = target - nums[i]; 

        if(hashTable.ContainsKey(complement)) // here we just look for the result of the complement variable, that sums with the current value (nums[i]) results in the target.
        {
            return new int[] {hashTable[complement],i};
        }else{
            hashTable[nums[i]] = i; //if not has the  complement, just add in the hash table
        }
      }

        throw new Exception("Not found");




    }
}
