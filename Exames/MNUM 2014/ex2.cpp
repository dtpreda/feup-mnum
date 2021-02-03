#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

double f(double x){
  return -x + 40*cos(sqrt(x)) + 3;
}

double df(double x){
  return -1 - 20*sin(sqrt(x))/sqrt(x);
}

void newton(double x0, double (*f)(double), double (*df)(double), int n){
  double x = x0;
  for(int i = 0; i < n; i++){
    cout << "x: " << x << "    g(x): " << f(x) << endl;
    x0 = x;
    x = x - f(x)/df(x);
  }
  cout << "x: " << x << endl;
  cout << "absolute error: " << x - x0 << endl; // rounds to 0.1 => implies that we don't have any exact decimal cases
}

int main(int argc, char* agrv[]){
  cout << fixed << setprecision(6);

  newton(1.7, f, df, 2);
  return 0;
}
