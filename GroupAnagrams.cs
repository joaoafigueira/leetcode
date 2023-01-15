
/*Given an array of strings strs, group the anagrams together. You can return the answer in any order.  */

/*Approach:

Hashtable = {}
strs = ["eat", "tea","tan", "ate", "nat", "bat"]

for each str in strs => "bat"
    Split str in to char[] => ['b','a','t']
    Sort the char[] => ['a','b','t']
    Join in to a String => key = "abt"
    If key not exists in HashTable, create new key= {key} and value ={new String[][0] = str}

    
In the end of for each loop we have this HashTable  
{
    'a,e,t': ['eat', 'tea','ate],
    'a,n,t':['tan','nat'],
    'a,b,t': ['bat']
}


O (strs * n)

strs = numbers of strings

n = average length of each string;

*/

public class Solution {

    public IList<IList<string>> GroupAnagrams(string[] strs) {
        
     Dictionary<string, IList<string>> hashTable = new Dictionary<string, IList<string>>();

     foreach(string str in strs){

        char[] chars = str.ToArray();

        Array.Sort(chars);

        string key = new string(chars);

        if(!hashTable.ContainsKey(key)){
            IList<string> list = new List<string>();
            list.Add(str);
            hashTable.Add(key, list);
        }else{
            hashTable[key].Add(str);
        }

     }

     return new List<IList<string>>(hashTable.Values);

    }
}
