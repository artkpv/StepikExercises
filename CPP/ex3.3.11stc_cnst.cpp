#include <cstddef> // size_t
#include <cstring> // strlen, strcpy
#include <cstdlib> 
#include <iostream>

using namespace std;

struct String {

    /* Реализуйте этот конструктор */
	String(size_t n, char c) {
		this->str = new char[n + 1];
		//this->str = (char*)std::calloc(n + 1, sizeof(char));
		for(int i = 0; i < n; i++) {
			this->str[i] = c;
		}
		this->str[n] = '\0';
		this->size = n;
	}

    /* и деструктор */
	~String() {
		delete [] this->str;
	}

    /* Реализуйте этот метод. */
	void append(String &other) {
		size_t newsize = this->size + other.size;
		char * str2 = new char[newsize + 1];
		int i = 0;
		for(; i < this->size; i++) {
			str2[i] = this->str[i];
		}
		for(int j = 0; j < other.size; j++) {
			str2[i++] = other.str[j];
		}
		str2[i] = '\0';
		delete [] this->str;
		this->str = str2;
		this->size = newsize;
	}

	size_t size;
	char *str;
};

int main() {
	String str = String(10, 'l');
	std::cout << str.str << std::endl;
	String str2 = String(10, 'r');
	str.append(str2);
	std::cout << str.str << std::endl;
}


