#include <iostream>
#include <iomanip>
#include <math.h>
#include <vector>

using namespace std;

void gauss_elimination(vector<vector<double>>& matrix){
  for(int i = 0; i < matrix.size() - 1; i++){
    for(int j = i + 1; j < matrix.size(); j++){
      double coef = -matrix[j][i]/matrix[i][i];
      for(int k = 0; k < matrix[j].size(); k++){
        matrix[j][k] += matrix[i][k]*coef;
      }
    }
  }
  for (int i = 0; i < matrix.size(); i++){
    double coef = matrix[i][i];
    for(int j = 0; j < matrix[i].size(); j++){
      matrix[i][j] /= coef;
    }
  }
}

int main(int argc, char* argv[]){
  cout << fixed << setprecision(6);

  vector<vector<double>> matrix;
  vector<double> temp;
  temp.push_back(0.1);
  temp.push_back(0.5);
  temp.push_back(3.0);
  temp.push_back(0.25);
  temp.push_back(0.0);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(1.2);
  temp.push_back(0.2);
  temp.push_back(0.25);
  temp.push_back(0.2);
  temp.push_back(1.0);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(-1.0);
  temp.push_back(0.25);
  temp.push_back(0.3);
  temp.push_back(2.0);
  temp.push_back(2.0);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(2.0);
  temp.push_back(0.00001);
  temp.push_back(1.0);
  temp.push_back(0.4);
  temp.push_back(3.0);
  matrix.push_back(temp);
  temp.clear();

  gauss_elimination(matrix);

  for(int i = 0; i < matrix.size(); i++){
    for(int j = 0; j < matrix[i].size(); j++){
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }

  double x4 = matrix[3][4];
  double x3 = matrix[2][4] - matrix[2][3]*x4;
  double x2 = matrix[1][4] - matrix[1][3]*x4 - matrix[1][2]*x3;
  double x1 = matrix[0][4] - matrix[0][3]*x4 - matrix[0][2]*x3 - matrix[0][1]*x2;

  cout << "x1: " << x1 << endl;
  cout << "x2: " << x2 << endl;
  cout << "x3: " << x3 << endl;
  cout << "x4: " << x4 << endl;

  matrix.clear();

  double delta = 0.3;

  temp.push_back(0.1);
  temp.push_back(0.5);
  temp.push_back(3.0);
  temp.push_back(0.25);
  temp.push_back(delta - x1*delta - x2*delta - x3*delta - x4*delta);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(1.2);
  temp.push_back(0.2);
  temp.push_back(0.25);
  temp.push_back(0.2);
  temp.push_back(delta - x1*delta - x2*delta - x3*delta - x4*delta);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(-1.0);
  temp.push_back(0.25);
  temp.push_back(0.3);
  temp.push_back(2.0);
  temp.push_back(delta - x1*delta - x2*delta - x3*delta - x4*delta);
  matrix.push_back(temp);
  temp.clear();

  temp.push_back(2.0);
  temp.push_back(0.00001);
  temp.push_back(1.0);
  temp.push_back(0.4);
  temp.push_back(delta - x1*delta - x2*delta - x3*delta - x4*delta);
  matrix.push_back(temp);
  temp.clear();

  gauss_elimination(matrix);

  double delta4 = matrix[3][4];
  double delta3 = matrix[2][4] - matrix[2][3]*delta4;
  double delta2 = matrix[1][4] - matrix[1][3]*delta4 - matrix[1][2]*delta3;
  double delta1 = matrix[0][4] - matrix[0][3]*delta4 - matrix[0][2]*delta3 - matrix[0][1]*delta2;

  cout << "delta1: " << delta1 << endl;
  cout << "delta2: " << delta2 << endl;
  cout << "delta3: " << delta3 << endl;
  cout << "delta4: " << delta4 << endl;

  return 0;
}
