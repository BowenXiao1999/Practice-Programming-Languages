#include <iostream> 
#include <string> 
using namespace std; 

void demo() 
{ 
    // static variable 
    static int count = 3; 
    cout << count << " "; 
    
    // value is updated and 
    // will be carried to next 
    // function calls 
    count++; 
} 

int main() 
{ 
    for (int i=0; i<5; i++)  
        demo(); 
    return 0; 
} 