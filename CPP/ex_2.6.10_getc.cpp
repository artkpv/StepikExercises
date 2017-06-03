#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int DEFAULT_SIZE = 10;

char *getline()
{
    unsigned size = DEFAULT_SIZE;
    char * str = new char[size];
    char c = '\0';
    unsigned i = 0;
    while(cin.get(c)) {
        if(c == '\n') break;
        if(i + 1 == size) { 
            size = size * 2;
			char * str2 = new char[size];
			for(int j = 0; j < i + 1; j++) {
				str2[j] = str[j];
			}
			delete [] str;
            str = str2;
        }
        str[i] = c;
        i++;
    }
    str[i] = '\0';
    return str;
}

int main() {
	while(true) {
		char * str = getline();
		cout << str << endl;
		delete str;
	}
}
