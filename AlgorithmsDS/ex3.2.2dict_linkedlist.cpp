#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

struct MyDict {

	MyDict(int m) {
		this->_m = m;
		this->_a = new char*[m];
		for(int i = 0; i < m; i++) {
			this->_a[i] = 0;
		}
	}

	void add(string s) {
	}

	string check(int i) {
		return "[check]";
	}

	int _m;
	char ** _a;
	
};

int main() {
	int m = 0, n = 0;
	cin >> m;
	cin >> n;
	MyDict d = MyDict(m);
	for(int i = 0; i<n; i++){
		string command, p1;
		cin >> command >> p1;
		if(command == "add"){
			d.add(p1);
		} else if(command == "check"){
			string r = d.check(stoi(p1));
			cout << r << endl;
		}

	}
	return 0;
}
