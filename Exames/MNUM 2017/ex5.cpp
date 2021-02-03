#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>
using namespace std;

double f(double x, double y){
  return -1.1*x*y + 12*y + 7*pow(x, 2) - 8*x;
}

double dfx(double x, double y){
  return -1.1*y + 14*x - 8;
}

double dfy(double x, double y){
  return -1.1*x + 12;
}

vector<double> gradient(double x0, double y0, double (*f)(double, double), double (*dfx)(double, double), double (*dfy)(double, double), double lambda, int n){
  double x = x0, y = y0;
  for(int i = 0; i < n; i++){
      x = x0 - lambda*dfx(x0, y0);
      y = y0 - lambda*dfy(x0, y0);
      if(f(x, y) < f(x0, y0)){
        lambda *= 2;
        x0 = x;
        y0 = y;
      } else{
        lambda *= 0.5;
      }
  }

  vector<double> ret;
  ret.push_back(x);
  ret.push_back(y);
  return ret;
}

int main(int argv, char* argc[]){
  cout << fixed << setprecision(5);

  vector<double> ret = gradient(3, 1, f, dfx, dfy, 0.1, 1);

  cout << "---Result---" << endl;
  cout << "x: " << ret[0] << endl;
  cout << "y: " << ret[1] << endl;
  cout << "w(x, y): " << f(ret[0], ret[1]) << endl;
  return 0;
}
