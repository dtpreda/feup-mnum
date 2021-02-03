#include <iostream>
#include <math.h>

using namespace std;

double f(double x) {
  return pow(x-6, 2) + pow(x, 4);
}

double df(double x) {
  return 2*(x-6) + 4*pow(x, 3);
}

double ddf(double x) {
  return 2 + 12*pow(x, 2);
}

double levenberg_marquardt(double x0, double lambda, double (*f)(double), double(*gradient)(double), double(*hessian)(double), double e=0.0001){
  double grad, hess, x; int counter = 0;
  while(true){
    grad = gradient(x0);
    if(hessian(x0) != 0){
      hess = 1/hessian(x0);
    }
    else{
      hess = 0;
    }
    x = x0 - lambda*grad - grad*hess;
    if(f(x) < f(x0)){
      if(abs(x - x0) < e){
        return x;
      }
      lambda *= 0.5;
      x0 = x;
    }
    else {
      lambda *= 2;
    }
  }
}

int main(int argc, char* argv[]){
  cout << "Levenberg-Marquardt result: " << levenberg_marquardt(1.0, 0.01, f, df, ddf) << endl;
  return 0;
}
