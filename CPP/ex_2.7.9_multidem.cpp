#include <iostream>
using namespace std;

int ** transpose(const int * const * m, unsigned rows, unsigned cols)
{
    int ** mt = new int * [cols];
	mt[0] = new int[cols * rows];
	for(unsigned i = 1; i != cols; i++) {
		mt[i] = mt[i - 1] + rows;
	}

	for(unsigned i = 0; i < rows; i++) { 
		for(unsigned j = 0; j < cols; j++) { 
			mt[j][i] = m[i][j];
		}
	}
	return mt;
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
	m[2][0] = 5;
	m[2][1] = 6;
	int ** mt = transpose((int**)m, rows, cols);
	for(unsigned i = 0; i < cols; i++) {
		for(unsigned j = 0; j < rows; j++) {
			cout << mt[i][j] << ' ';
		}
		cout << endl;
	}
}
