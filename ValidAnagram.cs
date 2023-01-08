public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){
        
         return false;
        } 


        var s = CreateDictionary(s);
        var anagram = CreateDictionary(t);


        foreach (var item in s)
        {

            if (!anagram.ContainsKey(item.Key)){ //checks if the s.key not contain in anagram

              return false;
            }


            if (item.Value != anagram[item.Key]){ //checks if the number of characters are equal
              
              return false;
            } 
        }


        return true;
    }


    private Dictionary<char, int> CreateDictionary(string s) //check the number of characters present
    {
        var map = new Dictionary<char, int>();


        for (int i = 0; i < s.Length; i++)
        {
            
            if (!map.ContainsKey(s[i])){ //if map not have the character add 

                map.Add(s[i], 1);
            }
            else{

                map[s[i]]++; //if map have the character sum the value
            }
        }


        return map;
    }
}