#include <iostream>
#include <string>
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



string freqPattern(string src, int count)
{

     string pattern;
     string out;
     int max_count = 0;
    
 for (int i = 0; i < src.length() - count + 1; i++)
     {  
        string pt =  src.substr(i, count);
        int tcount;
    // cout << pt << "\n";
         tcount = StrMatchCount(src, pt);
         if (tcount > max_count)
         {
             max_count = tcount;
             // переформировать строки
             out = "";
         }
         if (tcount == max_count)
         {
             if (StrMatchCount(out, pt) == 0)
             out += pt + " ";
         }
     }
    return out;
}


int main() {
    string src;
    int count;
    cin >> src;
    cin >> count;
    
    
    string out;
    
     cout << freqPattern(src, count);
    
    return 0;
}
