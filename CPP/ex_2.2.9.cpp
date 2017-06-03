#include <iostream>
using namespace std;

int foo(int n) {
	cout << "foo(" << n << ")\n";
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);
}

int main()
{
	cout << (int)0.66<< endl;
	foo(3);
	return 0;
}
