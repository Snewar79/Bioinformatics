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


int main() {
    string src;
    string pattern;
    cin >> pattern;
    cin >> src;
    
    
    cout << StrMatchCount(src, pattern);
    
    return 0;
}
