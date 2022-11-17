#include <iostream>
using namespace std;


int main() {
  int ultAmmo = 3;
  bool endult;
  bool run = true;
  int inputcheck = 0;
  while(run){
    // imitating how many buttons pressed, and using it to count down
    // enter 1, and it will function as intended. anything higher (ex. 2) it will never end.
    cout << "Input?" << endl;
    cin >> inputcheck;
    ultAmmo = ultAmmo - inputcheck;
      if (ultAmmo == 0){
        
    /*will only end if value is actually zero
    meaning if you get less than 0, it will continue
    while this works, its not logical because there are       factors that can cause the program to count down differently than just -1, and therefore skip 0.
    in overwatch's case, there are 2 inputs for using his ult. this means it will count down by 2 when both are pressed, resulting in negative numbers.
      changing it from == to <= will make it so that even if the count reaches a negative number, it will still end.
    */
        endult = true;
        break;
    
      }
    }
  

  
}