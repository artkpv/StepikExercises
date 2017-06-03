int strstr(const char *text, const char *pattern)
{
	if(*pattern == '\0') return 0;

	const char * pText = text;
	const char * pPattern = pattern;

	while(*pText != '\0') {
		int charsMatched = 0;

		while(*pPattern != '\0' 
			  && *pText != '\0' 
			  &&  *pText == *pPattern)  {
			charsMatched++;
			pText++;
			pPattern++;
		}
		if(*pPattern == '\0') { // found
			return (pText - text) - charsMatched;
		}
		else { // back to next char
			pPattern = pattern;
			pText = pText - charsMatched + 1;
		}
	}
	return -1;
}


#include <iostream>
using namespace std;

int main() {
	cout << strstr("ab", "cd") << endl;
	cout << strstr("cd", "cd") << endl;
	cout << strstr("abcdefg", "cd") << endl;
	cout << strstr("ababcdefg", "abc") << endl;
	cout << strstr("gfedabc", "abc") << endl;
	cout << strstr("ababac", "abac") << endl;
	cout << strstr("ababac", "") << endl;
	cout << strstr("", "") << endl;


cout << "others:" << endl;
cout << strstr("abc", "") << endl; // 0
cout << strstr("", "") << endl; // 0
cout << strstr("", "abc") << endl; // -1
cout << strstr("abc", "abc") << endl; // 0
cout << strstr("abcqq", "abc") << endl; // 0
cout << strstr("qqabc", "abc") << endl; // 2
cout << strstr("abcabc", "abc") << endl; // 0
cout << strstr("ababc", "abc") << endl; // 2
cout << strstr("ababcq", "abc") << endl; // 2
}
