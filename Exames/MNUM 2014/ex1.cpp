#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

double m = 20;
double c = 1;
double k = 20;

double f(double t, double x, double z){
  return -(c*z + k*x)/m;
}

double g(double t, double x, double z){
  return z;
}

void euler(double t0, double x0, double z0, double h, double(*f)(double, double, double), double(*g)(double, double, double), int n){
  double t = t0, x = x0, z = z0, dt = h, dx = 0, dz = 0;
  for(int i = 0; i < n; i++){
    cout << "(" << t << ", " << x << ")" << endl;
    dx = g(t, x, z)*dt;
    dz = f(t, x, z)*dt;
    x += dx;
    z += dz;
    t += dt;
  }
}

int main(int argc, char* agrv[]){
  cout << fixed << setprecision(6);

  euler(0, 1, 0, 0.1, f, g, 50);
  return 0;
}
