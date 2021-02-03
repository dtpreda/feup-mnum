#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>

using namespace std;

double g(double x){
  return 2 * log(2*x);
}

void picard_peano(double x, double (*g)(double), int n){
  double xn = x;
  for(int i = 0; i < n; i++){
    cout << xn << endl;
    x = xn;
    xn = g(x);
  }
  cout << x << endl;
  cout << "Residue: " << xn - x << endl;
}

double f(double x, double t){
  return sin(x) + sin(2*t);
}

double rk4(double t0, double x0, double h, double(*f)(double, double), int n){
  double x = x0, t = t0, dt = h, dx = 0;
  double dx1, dx2, dx3, dx4;
  for(int i = 0; i < n; i++){
    cout << "t: " << t << "    x: " << x << endl;
    dx1 = f(x, t)*dt;
    dx2 = f(x + dx1/2, t + dt/2)*dt;
    dx3 = f(x + dx2/2, t + dt/2)*dt;
    dx4 = f(x + dx3, t + dt)*dt;
    dx = dx1/6 + dx2/3 + dx3/3 + dx4/6;
    x += dx;
    t += dt;
  }
  cout << "t: " << t << "    x: " << x << endl;
  return x;
}

double z(double x, double y){
  return 6*pow(x, 2) -x*y + 12*y + pow(y, 2) -8*x; 
}

double dzx(double x, double y){
  return 12*x -y - 8;
}

double dzy(double x, double y){
  return -x + 12 + 2*y;
}

void grad(double x0, double y0, double lambda, double (*f)(double, double), double (*dfx)(double, double), double (*dfy)(double, double), int n){
  double x = x0, y = y0;
  for(int i = 0; i < n; i++){
    cout << "x: " << x << "    y: " << y << endl;
    cout << "Z(x, y): " << f(x, y) << endl;
    cout << "Grad: (" << dfx(x,y) << ", " << dfy(x, y) << ")" << endl;
    x = x0 - lambda*dfx(x0, y0);
    y = y0 - lambda*dfy(x0, y0);
    if(f(x, y) < f(x0, y0)){
      lambda *= 2;
      x0 = x;
      y0 = y;
    }
    else {
      lambda *= 0.5;
    }
  }
  cout << "x: " << x << "    y: " << y << endl;
    cout << "Z(x, y): " << f(x, y) << endl;
}

void gauss_elimination(vector<vector<double>>& matrix){
  for(int i = 0; i < matrix.size() - 1; i++){
    for(int j = i + 1; j < matrix.size(); j++){
      double coef = matrix[j][i]/matrix[i][i];
      for(int k = 0; k < matrix[j].size(); k++){
        matrix[j][k] -= matrix[i][k]*coef;
      }
    }
  }
  for(int i = 0; i < matrix.size(); i++){
    double coef = matrix[i][i];
    for(int j = 0; j < matrix[i].size(); j++){
      matrix[i][j] /= coef;
    }
  }
}


int main(int argc, char* argv[]){
  cout << fixed << setprecision(6);

  //Ex1
  //a) -> X1 e X2
  //b) -> X1 e X2
  //c) -> Nenhum

  picard_peano(0.9, g, 1);
  cout << endl;

  double s = rk4(1, 0, 0.5/2, f, 1);
  cout << endl;
  double ss = rk4(1, 0, 0.5/4, f, 1*2);
  cout << endl;
  double sss = rk4(1, 0, 0.5/8, f, 1*4);
  cout << endl;

  double QC = (ss - s)/(sss - ss); double estimate = (sss - ss)/15;

  cout << "QC: " << QC << endl << "Error estimate: " << estimate << endl;
  cout << endl;

  //Ex4
  //a) I, diagonal dominante
  //b) III, primeiro coefieciente da diagonal principal já está normalizado, temos uma linha já na forma pretendida
  //c)
  //xn+1 = (2 - 6*yn - zn)/10
  //yn+1 = (0 - xn+1 - 3*zn)/11
  //zn+1 = (-8 - 2*xn+1 -7*yn+1)/13

  grad(0, 0, 0.25, z, dzx, dzy, 1);
  cout << endl;

  vector<vector<double>> matrix;
  vector<double> temp;
  double x1 = 0.552949, x2 = -0.15347, x3 = -0.10655;
  temp.push_back(18);
  temp.push_back(-1);
  temp.push_back(1);
  temp.push_back(0.1 - x1*0.1 - x2*0.1 - x3*0.1);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(3);
  temp.push_back(-5);
  temp.push_back(4);
  temp.push_back(0.1 - x1*0.1 - x2*0.1 - x3*0.1);
  matrix.push_back(temp);
  temp.clear();
  
  temp.push_back(6);
  temp.push_back(8);
  temp.push_back(29);
  temp.push_back(0.1 - x1*0.1 - x2*0.1 - x3*0.1);
  matrix.push_back(temp);
  temp.clear();

  cout << endl;

  gauss_elimination(matrix);

  for(int i = 0; i < matrix.size(); i++){
    for(int j = 0; j < matrix[i].size(); j++){
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;

  double d3 = matrix[2][3];
  double d2 = matrix[1][3] - matrix[1][2]*d3;
  double d1 = matrix[0][3] - matrix[0][2]*d3 - matrix[0][1]*d2;

  cout << d1 << endl << d2 << endl << d3 << endl;
  return 0;
}
