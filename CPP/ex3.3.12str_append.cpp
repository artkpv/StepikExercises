#include <cstddef> // size_t
#include <cstring> // strlen, strcpy

struct String {
	String(const char *str = "");
	String(size_t n, char c);
	~String();



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
