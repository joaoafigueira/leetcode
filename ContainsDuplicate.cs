/* Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.*/

/*Approach:  

Hashtable = {}
nums = [1,2,3,1]

for each num in nums => 1
    Check if the num is present in hashTable, returns true
    If the num is not present in the hashTable, add it as a key. 
*/

public class Solution {
    public bool ContainsDuplicate(int[] nums) {

    var hashtable = new Dictionary<int,int>();

    for (int i = 0; i < nums.Length; i++){

        if(hashtable.ContainsKey(nums[i])){

            return true;
        }


        hashtable[nums[i]] = i; //Dictionary[key] = value;
    }


    return false;
}
}