#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

double dc(double t, double c){
  return -exp(-0.5/(t + 273.0))*c;
}

double dt(double t, double c){
  return 30.0*exp(-0.5/(t + 273.0))*c - 0.5*(t - 20);
}

double euler(double t0, double T0, double c0, double step ,double (*dT)(double, double), double (*dc)(double, double), int n){
  double t = t0, T = T0, c = c0, dt = 0, dC = 0;
  for(int i = 0; i < n; i++){
    dt = dT(T, c)*step;
    dC = dc(T, c)*step;
    T += dt;
    c += dC;
    t += step;
  }
  return T;
}

double rk4(double t0, double T0, double c0, double step ,double (*dT)(double, double), double (*dc)(double, double), int n){
  double t = t0, T = T0, c = c0;
  double dt1, dt2, dt3, dt4, dc1, dc2, dc3, dc4, dt, dC;
  for(int i = 0; i < n; i++){
    cout << endl;
    dt1 = dT(T, c)*step;
    dc1 = dc(T, c)*step;
    dt2 = dT(T + dt1/2, c + dc1/2)*step;
    dc2 = dc(T + dt1/2, c + dc1/2)*step;
    dt3 = dT(T + dt2/2, c + dc2/2)*step;
    dc3 = dc(T + dt2/2, c + dc2/2)*step;
    dt4 = dT(T + dt3, c + dc3)*step;
    dc4 = dc(T + dt3, c + dc3)*step;
    dt = dt1/6 + dt2/3 + dt3/3 + dt4/6;
    dC = dc1/6 + dc2/3 + dc3/3 + dc4/6;
    T += dt;
    c += dC;
    t += step;
  }
  return T;
}

int main(int argv, char* argc[]){
  cout << fixed << setprecision(5);

  double l1 = euler(0, 25.0, 2.5, 0.25, dt, dc, 2);
  double l2 = euler(0, 25.0, 2.5, 0.125, dt, dc, 2*2);
  double l3 = euler(0, 25.0, 2.5, 0.0625, dt, dc, 2*4);

  cout << "Th: " << l1 << endl;
  cout << "Th': " << l2 << endl;
  cout << "Th'': " << l3 << endl;

  double QC = (l2 - l1) / (l3 - l2);
  double estimate = (l3 - l2)/15;

  cout << "QC: " << QC << endl;
  cout << "Epsilon'': " << estimate << endl;

  return 0;
}
