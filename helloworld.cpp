#include <iostream>
#include <string>
using namespace std;

int main() {
   string name;
   cout << "\033[32mHello World!\033[0m\n";
   cout << "\n\033[34mHello, What is your name?\n> ";
   getline(cin, name);
   cout << "\n\033[35mHello, \033[92m" << name << "\033[0m!";
   return 0;
}
