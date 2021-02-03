#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

// y' = z
// z' = A + t**2 + t*z

double f(double t, double y, double z){
  return z;
}

double g(double t, double y, double z){
  return 0.5 + pow(t, 2) + t*z;
}

void euler(double t0, double y0, double z0, double h, double(*f)(double, double, double), double(*g)(double, double, double), int n){
  double t = t0, y = y0, z = z0, dt = h, dy = 0, dz = 0;
  for(int i = 0; i < n; i++){
    cout << "t: " << t << "    y: " << y << endl;
    dy = f(t, y, z)*dt;
    dz = g(t, y, z)*dt;
    y += dy;
    z += dz;
    t += dt;
  }
  cout << "t: " << t << "    y: " << y << endl;
}

void rk4(double t0, double y0, double z0, double h, double(*f)(double, double, double), double(*g)(double, double, double), int n){
  double t = t0, y = y0, z = z0, dt = h, dy = 0, dz = 0;
  double dy1, dy2, dy3, dy4, dz1, dz2, dz3, dz4;
  for(int i = 0; i < n; i++){
    cout << "t: " << t << "    y: " << y << endl;
    dy1 = f(t, y, z)*dt;
    dz1 = g(t, y, z)*dt;

    dy2 = f(t + dt/2, y + dy1/2, z + dz1/2)*dt;
    dz2 = g(t + dt/2, y + dy1/2, z + dz1/2)*dt;

    dy3 = f(t + dt/2, y + dy2/2, z + dz2/2)*dt;
    dz3 = g(t + dt/2, y + dy2/2, z + dz2/2)*dt;

    dy4 = f(t + dt, y + dy3, z + dz3)*dt;
    dz4 = g(t + dt, y + dy3, z + dz3)*dt;

    dy = dy1/6 + dy2/3 + dy3/3 + dy4/6;
    dz = dz1/6 + dz2/3 + dz3/3 + dz4/6;
    y += dy;
    z += dz;
    t += dt;
  }
  cout << "t: " << t << "    y: " << y << endl;
}

int main(int argc, char* argv[]){
  cout << fixed << setprecision(5);

  double t0 = 0, y0 = 0, z0 = 1;
  double h = 0.25;
  euler(t0, y0, z0, h, f, g, 2);
  cout << endl;
  rk4(t0, y0, z0, h, f, g, 2);
}
