#include <iostream>
#include <string>

using namespace std;

struct map
{
    string key;
    string val;
};

    string find_by_key(string _key, map * m, int count)
    {
        for (int i = 0; i < count; i++)
            if (m[i].key == _key) return m[i].val;
        
        return "";
    }
    

int main() {
    
    string input;
    string out;
    // HardCode Table;
    map * list = new map[64];
    string input_table = "AAA K AAC N AAG K AAU N ACA T ACC T ACG T ACU T AGA R AGC S AGG R AGU S AUA I AUC I AUG M AUU I CAA Q CAC H CAG Q CAU H CCA P CCC P CCG P CCU P CGA R CGC R CGG R CGU R CUA L CUC L CUG L CUU L GAA E GAC D GAG E GAU D GCA A GCC A GCG A GCU A GGA G GGC G GGG G GGU G GUA V GUC V GUG V GUU V UAA 0 UAC Y UAG 0 UAU Y UCA S UCC S UCG S UCU S UGA 0 UGC C UGG W UGU C UUA L UUC F UUG L UUU F";
    
    for (int i = 0; i < 64; i++)
    {
        list[i].key = input_table.substr(i * 6, 3);
        list[i].val = input_table.substr(i * 6 + 4, 1);
        //cout << list[i].key << " " <<  list[i].val << "\n";
    }
    
    
    cin >> input;
    
    for (int i = 0; i < input.length() - 2; i += 3)
    {
        string _key = input.substr(i, 3);    
        string buf = find_by_key(_key, list, 64);
   //     cout << "key = " << _key << " buf =" << buf << "\n";
        if (buf != "0" && buf != "")
            out += buf;       
    }
    
    cout << out << "\n";
    // end hard_code
    
    return 0;
}
