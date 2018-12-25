#include <iostream>
#include <string>
#include <vector>
using namespace std;


int StrMatchCount(string src, string pattern)
{
    int count = 0;

    if (src.length() < pattern.length()) 
        return 0;
    
    for (int i = 0; i < src.length() - pattern.length() + 1; i++)
        for (int j = 0; j < pattern.length(); j++)
        {    
           // cout << i << " ";
            if (pattern[j] != src[i+j])
            {   
                break;
            //    cout << "\n";
            }
            if (j == pattern.length() - 1) 
            {   
                count++;
            //    cout << "i = "<< i << "\n";
            }
        }
    return count;
}



string revertDNA(string scr)
{

    string out = "";
    for (int i = scr.length() - 1; i >=0; i--)
    {
         if (scr[i] == 'A') out += "T";
         if (scr[i] == 'T') out += "A";
         if (scr[i] == 'C') out += "G";
         if (scr[i] == 'G') out += "C";
    }
    
    return out;

}


struct map
{
    string key;
    string val;
};

    string find_by_key(string _key, map *m, int count)
    {
        for (int i = 0; i < count; i++)
            if (m[i].key == _key) return m[i].val;
        
        return "";
    }
    


string revertSt(string st)
{
    string out = "";
    for (int i = st.length() - 1; i >=0; i--)
    {  
      //  cout << st[i];
        out += st[i];
         
    }
    return out;
}


vector<string> find_by_value(string val, map *m, int count)
{
    vector<string> out;
    for (int i = 0; i < count; i++)
    {
        if (m[i].val == val) out.push_back(m[i].key);    
    }
    
    return out;
}


int main() {
    
    string idna;
    string ip;
    // HardCode Table;
    map * list = new map[64];
    map * list_uu = new map[64];
    string input_table = "AAA K AAC N AAG K AAU N ACA T ACC T ACG T ACU T AGA R AGC S AGG R AGU S AUA I AUC I AUG M AUU I CAA Q CAC H CAG Q CAU H CCA P CCC P CCG P CCU P CGA R CGC R CGG R CGU R CUA L CUC L CUG L CUU L GAA E GAC D GAG E GAU D GCA A GCC A GCG A GCU A GGA G GGC G GGG G GGU G GUA V GUC V GUG V GUU V UAA 0 UAC Y UAG 0 UAU Y UCA S UCC S UCG S UCU S UGA 0 UGC C UGG W UGU C UUA L UUC F UUG L UUU F";
    
    for (int i = 0; i < 64; i++)
    {
        list[i].key = input_table.substr(i * 6, 3);
        list[i].val = input_table.substr(i * 6 + 4, 1);
        //cout << list[i].key << " " <<  list[i].val << "\n";
    }
    
    
    for (int i = 0; i < 64; i++)
    {
        list_uu[i] = list[i];
        for (int j = 0; j < 3; j++)
            if (list_uu[i].key[j] == 'U') list_uu[i].key[j] = 'T';    
    }
    
    
    //End_hard_code
    
    cin >> idna;
    cin >> ip;
    
    string rev = revertDNA(idna);
    
    string cur_res = "";
    
    
        for (int i = 0; i < idna.length(); i++)
    {
          int flag = 1;
          cur_res = "";
        string cur_triod;
        int string_pointer = i;
        int iteration = 0;
        while (flag == 1)
        {
            cur_triod = idna.substr(string_pointer, 3);
       //     cout << cur_triod << " = " << find_by_key(cur_triod, list_uu, 64) << "\n";
            string pt = ip.substr(iteration, 1);
            if (pt == find_by_key(cur_triod, list_uu, 64))
            {
                cur_res += cur_triod;
                iteration++;
                string_pointer +=3;
                if (iteration == ip.length())
                {
                    cout << cur_res << "\n";
                    flag = 0;
                }
            }
            else
            {
                flag = 0;
          //      cout << "govno\n";
            }
        }
    }
    
        for (int i = 0; i < rev.length(); i++)
    {
          int flag = 1;
          cur_res = "";
        string cur_triod;
        int string_pointer = i;
        int iteration = 0;
        while (flag == 1)
        {
            cur_triod = rev.substr(string_pointer, 3);
         //   cout << cur_triod << " = " << find_by_key(cur_triod, list_uu, 64) << "\n";
            string pt = ip.substr(iteration, 1);
            if (pt == find_by_key(cur_triod, list_uu, 64))
            {
                cur_res += cur_triod;
                iteration++;
                string_pointer +=3;
                if (iteration == ip.length())
                {
                    cout << revertDNA(cur_res) << "\n";
                    flag = 0;
                }
            }
            else
            {
                flag = 0;
       //         cout << "govno\n";
            }
        }
    }
    
 return 0;   
}
    
