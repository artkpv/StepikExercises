#include "ex4.3.8virt_methods.cpp"
#include <iostream>

bool check_equals(Expression const *left, Expression const *right)
{
	 return *((int**)left) ==*((int**)right);
}


int main() {
	Expression * sube = new BinaryOperation(new Number(4.5), '*', new Number(5));
	Expression * another = new Number(4.5);
	std::cout << check_equals(sube, sube) << std::endl;
}
