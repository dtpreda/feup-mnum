#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

double g(double x){
  return log(x + 5);
}

double f(double x){
  return exp(x) - x - 5;
}

double df(double x){
  return exp(x) - 1;
}


double picard_peano(double x0, double(*f)(double), double e=0.00001){
  double xn = f(x0);
  int iter = 0;
  while(abs(xn - x0) >= e){
    x0 = xn;
    xn = f(x0);
    iter++;
  }
  cout << "PP iterations: " << iter << endl;
  return xn;
}

double newton(double x0, double(*f)(double), double(*df)(double), double e=0.00001){
  double xn = x0 - f(x0)/df(x0);
  int iter = 0;
  while(abs(xn - x0) >= e){
    x0 = xn;
    xn = x0 - f(x0)/df(x0);
    iter++;
  }
  cout << "Newton iterations: " << iter << endl;
  return xn;
}

int main(int argv, char* argc[]){
  cout << fixed << setprecision(5);

  cout << "Picard Peano result: " << picard_peano(1, g) << endl;
  cout << endl;
  cout << "Newton result: " << newton(1, f, df) << endl;
  return 0;
}
