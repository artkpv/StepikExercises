#include <cstddef> // size_t
#include <cstring> // strlen, strcpy


struct String {

    /* Реализуйте этот конструктор */
    String(const char *str = "") {
        this->size = strlen(str);
        this->str = new char[this->size + 1];
		strcpy(this->str, str);
    }

	size_t size;
	char *str;
};

#include <iostream>
using namespace std;

int main(){
	const char * cstring = "abcde";
	String s = String(cstring);
	cout << s.str << endl;

}
