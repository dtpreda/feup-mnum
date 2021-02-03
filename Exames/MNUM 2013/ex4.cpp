#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

double f(double x){
  return (x - 3.7) + pow(cos(x + 1.2), 3);
}

double df(double x){
  return 1 - 3*pow(cos(x + 1.2), 2)*sin(x + 1.2);
}

double newton(double x, double (*f)(double), double(*df)(double), int n){
  for(int i = 0; i < n; i++){
    x = x - f(x)/df(x);
  }
  return x;
}

int main(int argc, char* argv[]){

  cout << "Newton Result: " << setprecision(7) << newton(3.8, f, df, 1) << endl;

  return 0;
}
