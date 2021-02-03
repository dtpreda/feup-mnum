#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

double f(double x){
  return exp(1.5*x);
}

double simpson(double a, double b, double h, double (*f)(double)){
  double ret = f(a) + f(b);
  int n = (b-a)/h;
  for(int i = 1; i < n; i++){
    if(i % 2 == 0){
      ret += 2*f(a + i*h);
    } else {
      ret += 4*f(a + i*h);
    }
  }
  return ret*h/3;
}

void show(double a, double b, double h, double(*f)(double)){
  double hh = h/2;
  double hhh = hh/2;

  double s = simpson(a, b, h, f);
  double ss = simpson(a, b, hh, f);
  double sss = simpson(a, b, hhh, f);

  cout << "h: " << h << "    s: " << s << endl;
  cout << "hh: " << h << "    ss: " << ss << endl;
  cout << "hhh: " << h << "    sss: " << sss << endl;

  double QC = (ss - s)/(sss - ss);
  double estimate = ((sss - ss)/15)/sss;

  cout << "QC: " << QC << endl;
  cout << "Relative error: " << setprecision(10) <<estimate << endl;
}

int main(int argc, char* argv[]){
  cout << fixed << setprecision(5);

  show(1, 1.5, 0.125, f);
}
