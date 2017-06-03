#include <iostream>

#include <cstddef>

// Параметры функции copy_n идут в следующем
// порядке:
//   1. целевой массив
//   2. массив источник
//   3. количество элементов, которые нужно
//      скопировать
//
// Вам нужно реализовать только функцию copy_n,
// чтобы ее можно было вызвать так, как показано
// в примере.

// put your code here

template<class U, class T>
void copy_n(T * ta, U * ua, int n) {
	for(int i = 0; i < n; i++) {
		ta[i] = (T)(ua[i]);
	}
}


int main() {
	int ints[] = {1, 2, 3, 4};
	double doubles[4] = {};
	copy_n(doubles, ints, 4); // теперь в массиве doubles содержатся элементы 1.0, 2.0, 3.0 и 4.0
	for(int i = 0; i < 4; i++){
		std::cout << doubles[i] << std::endl;

	}
}
