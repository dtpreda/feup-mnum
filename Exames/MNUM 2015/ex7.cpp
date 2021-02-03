#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>

using namespace std;

double f(double x){
  return pow(x, 3) - 10 * sin(x) + 2.8;
}

double bissection(double a, double b, double(*f)(double), int n){
  double m;
  for(int i = 0; i < n; i++){
    m = (b + a) / 2;
    if(f(m)*f(a) < 0) {
      b = m;
    } else if (f(m)*f(b) < 0) {
      a = m;
    }
    else {
      return m;
    }
  }
  return b;
}

int main(int argv, char* argc[]){
  cout << fixed << setprecision(5);


  cout << "Bissection superior limit: " << bissection(1.5, 4.2, f, 2) << endl;
  return 0;
}
