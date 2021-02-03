#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

double z(double x, double y){
  return 3*pow(x, 2) - x*y + 11*y + pow(y, 2) - 8*x;
}

double dzx(double x, double y){
  return 6*x - y - 8;
}

double dzy(double x, double y){
  return -x + 11 + 2*y;
}

void grad(double x0, double y0, double lambda, double (*f)(double, double), double (*dfx)(double, double), double (*dfy)(double, double), int n){
  double x = x0, y = y0;
  for(int i = 0; i < n; i++){
    cout << "x: " << x << "    y: " << y << endl;
    cout << "z(x, y): " << z(x,y) << "    dzx(x, y): " << dzx(x,y) << "    dzy(x, y): " << dzy(x,y) << endl;
    cout << endl;
    x = x0 - lambda*dfx(x0, y0);
    y = y0 - lambda*dfy(x0, y0);
    if(f(x, y) < f(x0, y0)){
      lambda *= 2;
      x0 = x;
      y0 = y;
    } else {
      lambda *= 0.5;
    }
  }
  cout << "x: " << x << "    y: " << y << endl;
  cout << "z(x, y): " << z(x,y) << "    dzx(x, y): " << dzx(x,y) << "    dzy(x, y): " << dzy(x,y) << endl;
}

int main(int argc, char* argv[]){

  grad(2, 2, 0.5, z, dzx, dzy, 1);

  return 0;
}
