#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>

using namespace std;

void gauss_elimination(vector<vector<double>>& matrix){
  for(int i = 0; i < matrix.size() - 1; i++){
    for(int k = i + 1; k < matrix.size(); k++){
      double coef = -matrix[k][i]/matrix[i][i];
      for(int j = 0; j < matrix[i].size(); j++){
        matrix[k][j] += matrix[i][j]*coef;
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

int main(int argv, char* argc[]){
  cout << fixed << setprecision(5);

  vector<vector<double>>matrix;
  vector<double> temp;
  temp.push_back(1);
  temp.push_back(0.5);
  temp.push_back(0.33333);
  temp.push_back(-1);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(0.5);
  temp.push_back(0.33333);
  temp.push_back(0.25);
  temp.push_back(1);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(0.33333);
  temp.push_back(0.25);
  temp.push_back(0.2);
  temp.push_back(1);
  matrix.push_back(temp);
  temp.clear();

  gauss_elimination(matrix);

  for(int i = 0; i < matrix.size(); i++){
    for(int j = 0; j < matrix[i].size(); j++){
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }

  double x3 = matrix[2][3];
  double x2 = matrix[1][3] - x3;
  double x1 = matrix[0][3] - (matrix[0][1]*x2 + matrix[0][2]*x3);

  cout << "x1: " << x1 << endl;
  cout << "x2: " << x2 << endl;
  cout << "x3: " << x3 << endl;

  double delta = 0.05;

  matrix.clear();

  temp.push_back(1);
  temp.push_back(0.5);
  temp.push_back(0.33333);
  temp.push_back(delta - (x1*delta + x2*delta + x3*delta));
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(0.5);
  temp.push_back(0.33333);
  temp.push_back(0.25);
  temp.push_back(delta - (x1*delta + x2*delta + x3*delta));
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(0.33333);
  temp.push_back(0.25);
  temp.push_back(0.2);
  temp.push_back(delta - (x1*delta + x2*delta + x3*delta));
  matrix.push_back(temp);

  gauss_elimination(matrix);

  for(int i = 0; i < matrix.size(); i++){
    for(int j = 0; j < matrix[i].size(); j++){
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }

  double delta3 = matrix[2][3];
  double delta2 = matrix[1][3] - delta3;
  double delta1 = matrix[0][3] - (matrix[0][1]*delta2 + matrix[0][2]*delta3);

  cout << "delta1: " << delta1 << endl;
  cout << "delta2: " << delta2 << endl;
  cout << "delta3: " << delta3 << endl;

  // x3 é mais sensível a erros dado que |delta3| > |delta2| > |delta1|
  return 0;
}
