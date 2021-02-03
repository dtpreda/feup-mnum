#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>

using namespace std;

double f(double t, double T) {
  return -0.25*(T - 37);
}

double euler(double t0, double T0, double step, double (*f)(double, double), int n){
  double t = t0, T = T0, dT = 0;
  for(int i = 0; i < n; i++){
    dT = f(t, T)*step;
    T += dT;
    t += step;
  }
  return T;
}

int main(int argv, char* argc[]){
  cout << fixed << setprecision(5);

  cout << "Result: " << euler(5, 3, 0.4, f, 2) << endl;

  return 0;
}
