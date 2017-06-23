#include <iostream>
#include <string>
#include <vector>
//#include <cstdlib>
//#include <cassert>
//#include <tuple>
#include <sstream>
#include <iterator>


template<typename Out>
void split(const std::string &s, char delim, Out result) {
	std::stringstream ss;
	ss.str(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		*(result++) = item;
	}
}


std::vector<std::string> split(const std::string &s, char delim) {
	std::vector<std::string> elems;
	split(s, delim, std::back_inserter(elems));
	return elems;
}

int main() {
	int n = 15;
	std::cin >> n;
	//std::cout << "n=" << n << std::endl;
	for (int i = 0; i < n; i++) {
		std::string command; // = "abcde fghi";
		std::getline(std::cin, command);

		std::cout << "before split:" << i << std::endl;
		std::vector<std::string> v = split(command, ' ');
		std::cout << "after split:" << i << std::endl;
	}
}
