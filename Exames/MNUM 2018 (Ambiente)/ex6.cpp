#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main(int argv, char* argc[]){
  cout << fixed << setprecision(10);

  double a = 0.4523 * pow(10, 4), b = 0.2115 * pow(10, -3), c = 0.2583*10;
  cout << 4526.00000 << endl;
  cout << a + b + c << endl;
  cout << "Absolute error: " << 4526.00000 - (a + b + c) << endl;
  cout << "Relative error(%): " << (4526.00000 - (a + b + c))/4526.00000 * 100 << "%" << endl;
  return 0;
}
