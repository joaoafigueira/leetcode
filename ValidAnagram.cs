/*Given two strings s and t, return true if t is an anagram of s, and false otherwise.*/

/*Approach:

s = "anagram", t = "nagaram"

for each item in sAnagram => a
    checks if the s.key not contain in anagram
    checks if the number of characters are different

    check the number of characters present
    if map not have the character add 
    if map have the character sum the value

    check if tAnagram contains the same keys as sAnagram
    check if sAnagram has the same value as tAnagram
*/

public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){
        
         return false;
        } 

        var sAnagram = CreateDictionary(s);
        var tAnagram = CreateDictionary(t);

        foreach (var item in sAnagram)
        {

            if (!tAnagram.ContainsKey(item.Key)){ 

              return false;
            }

            if (item.Value != tAnagram[item.Key]){ 
              
              return false;
            } 
        }

        return true;
    }

    private Dictionary<char, int> CreateDictionary(string s) 
    {
        var map = new Dictionary<char, int>();

        for (int i = 0; i < s.Length; i++)
        {
            if (!map.ContainsKey(s[i])){ 

                map.Add(s[i], 1);
            }
            else{
                map[s[i]]++; 
            }
        }

        return map;
    }
}