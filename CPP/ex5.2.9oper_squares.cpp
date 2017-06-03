#include <iostream>
using namespace std;

#include <cstddef> // size_t

struct Substring {
	Substring(char *str, size_t size, int i) {
		_str = new char[size];
		for(int j = 0; j < size; j++)
			_str[j] = str[j];
		_str[size] = '\0';
		_i = i;
		_size = size;
	}
	~Substring() {
		delete _str;
		delete _substr;
	}
	char * _str;
	char * _substr;
	int _i;
	size_t _size;

	char* operator [] (int j) {
		int i = _i;
		if(i == j) return (char*)"";
		if(i > j) throw;
		j = j <= _size ? j : _size;

		int mysize = j - i + 1;
		_substr = new char[mysize];
		int k = 0;
		for(; k < mysize - 1; k++, i++) {
			_substr[k] = _str[i];
		}
		_substr[k] = '\0';
		return _substr;
	}
};


struct String {
	String(const char *str = "");
	String(size_t n, char c);
	~String();

    String(const String &other);
    String &operator=(const String &other);

	void append(const String &other);

	size_t size;
	char *str;

	Substring operator [] (int i) const {
		return Substring(str, size, i);
	}
};

*/

struct String {
	String(const char *str = "") {

		int i = 0;
		while(str[i++] != '\0') 
			;
		size = i;

		this->str = new char[size];
		for(int j = 0; j < size; j++)
			this->str[j] = str[j];
	}
	String(size_t n, char c);
	~String() {
	}

    String(const String &other);
    String &operator=(const String &other);

	void append(const String &other);

	size_t size;
	char *str;

	Substring operator [] (int i) const {
		return Substring(str, size, i);
	}
};


int main () {
	String const hello("hello");
	String const hell = hello[0][4]; // теперь в hell хранится подстрока "hell"
	String const ell  = hello[1][4]; // теперь в ell хранится подстрока "ell"
	String const e = hello[1][2];
	cout << hell.str << endl;
	cout << ell.str << endl;
	cout << e.str << endl;
}
