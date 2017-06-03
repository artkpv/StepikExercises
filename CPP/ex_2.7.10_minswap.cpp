#include <iostream>
using namespace std;

void swap_min(int *m[], unsigned rows, unsigned cols)
{
	if( rows == 0 && cols == 0) return;
    int min = m[0][0];
	int minrow = 0;
	for(unsigned i = 0; i < rows; i++) {
		for(unsigned j = 0; j < cols; j++) {
			if(min > m[i][j]) {
				min = m[i][j];
				minrow = i;
			}
		}
	}
	for(unsigned j = 0; j < cols; j++) {
		int t = m[0][j];
		m[0][j] = m[minrow][j];
		m[minrow][j] = t;
	}
}

int main() {
	const unsigned rows = 3;
	const unsigned cols = 2;

    int ** m = new int * [rows];
	m[0] = new int[cols * rows];
	for(unsigned i = 1; i != rows; i++) {
		m[i] = m[i - 1] + cols;
	}
	m[0][0] = 1;
	m[0][1] = 2;
	m[1][0] = 3;
	m[1][1] = 4;
	m[2][0] = -10;
	m[2][1] = 6;
	swap_min((int**)m, rows, cols);
	for(unsigned i = 0; i < rows; i++) {
		for(unsigned j = 0; j < cols; j++) {
			cout << m[i][j] << ' ';
		}
		cout << endl;
	}
}
