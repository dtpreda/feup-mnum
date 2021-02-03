#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>

using namespace std;

double g(double x){
  return 2*log(2*x);
}

void picard_peano(double x, double(*g)(double), int n){
  double previous = x;
  for(int i = 0; i < n; i++){
    cout << x << endl;
    previous = x;
    x = g(x);
  }
  cout << "Result: " << x << endl;
  cout << "Absolute error: " << x - previous << endl;
}

int main(int argv, char* argc[]){
  cout << fixed << setprecision(5);

  // a) -> X1 e X2
  // b) -> nenhuma raiz
  // c) -> X1 e X2
  picard_peano(1.1, g, 1);
  return 0;
}
