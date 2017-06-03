
void rotate(int a[], unsigned size, int shift)
{
	if(shift == 0) return;

	// 1: 1 2 3 4 
	//    size = 4
	//    shift = 2
	//    copy -> new ; from 0 + shift
	//
	// 2: size = 4; shift = 7
	//    1234
	// 3: size = 4; shift = 3
	//    1234
	//

	int firstInNew = shift % size;
	int b[size];
	for(int i = 0; i < size; i++) {
		int j = (firstInNew + i) % size;
		b[i] = a[j];
	}
	for(int i = 0; i < size; i++) {
		a[i] = b[i];
	}
}

#include <iostream>
using namespace std;

int main() { 
	int a[] = {1, 2, 3, 4, 5, 6};
	rotate(a, 6, 2);
	for(int i = 0; i < 6; i++) {
		cout << a[i] << ' ';
	}
	cout << endl;
}
