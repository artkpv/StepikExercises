#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

struct Interval {
	Interval() : x(-1), y(-1) {}
	Interval(int x, int y) : x(x), y(y) {}
	int x, y;
	bool no() { return x == -1; }
};

struct Point { 
	Point() : x(-1), interval(0) { }

	Point(int x, Interval & interval) : x(x), interval(interval) {
		starts = 0;
		ends = 0;
	}
	int x;
	int starts;
	int ends;
	Interval * interval;
};

bool operator<(const Point &left, const Point &right) {
    return left.x < right.x;
}
 

int main() {
	int & someint = null;
	int n, m;
	cin >> n >> m;

	// init with intervals also to count there starts and ends:
	int size = 2*n + m;
	vector<Point> points(size);

	// collect all interval starts:
	for(int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;

		Point p(x, &Interval(x, y))
		points[i] = &p;
		points[n + m + i] = Point(y, Interval(x, y));
	}
	// collect points:
	vector<Point> in_points(m);
	for(int i = 0; i < m; i++) {
		int x;
		cin >> x;
		Point point(x);
		in_points[i] = &point;
		points[n + i] = &point;  // place after interval starts
	}

	stable_sort(points.begin(), points.end());

	int left_ends = 0;
	int right_starts = 0;
	for(int i = 0; i < size; i++) {
		Point & left = points.at(i);
		Interval li = left.interval;
		if(!li.no() && li.y == left.x) { left_ends++; }
		else left.ends = left_ends;
		cout << "Left at " << left.x << ": interval=" << (!li.no()) << ";" ;
		cout << " left_ends=" << left_ends << endl;


		Point & right = points[size - i - 1];
		Interval ri = right.interval;
		if (!ri.no() && ri.x == right.x) right_starts++;
		else right.starts = right_starts;
		cout << "Right at " << right.x << ": interval=" << (!ri.no()) << ";" ;
		cout << " right_starts=" << right_starts << endl;

	}

	// print result:
	for(int i = 0; i < m; i++) {
		Point & p = in_points.at(i);
		cout << " POint " << p.x << " starts= " << p.starts << " ends=" << p.ends << endl;
		int count = n - p.starts - p.ends;
		cout << n << ' ';
	}
}
