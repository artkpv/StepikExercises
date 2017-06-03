struct Rational
{
	Rational(int numerator = 0, int denominator = 1);

	void add(Rational rational);
	void sub(Rational rational);
	void mul(Rational rational);
	void div(Rational rational);

	void neg();
	void inv();
	double to_double() const;

	Rational& operator+=(Rational rational);
	Rational& operator-=(Rational rational);
	Rational& operator*=(Rational rational);
	Rational& operator/=(Rational rational);

	Rational operator-() const;
	Rational operator+() const;

	friend bool operator==(Rational const & left, Rational const & right) {
		long long num = left.numerator_ * right.denominator_ - right.numerator_ * left.denominator_;
		return num == 0;
	}

	friend bool operator<(Rational const & left, Rational const & right) {
		long long left_num = left.numerator_ * right.denominator_;
		long long right_num = right.numerator_ * left.denominator_;
		return left_num < right_num;
	}

	friend bool operator!=(Rational const & left, Rational const & right) {
		return !(left == right);
	}

	friend bool operator<=(Rational const & left, Rational const & right) {
		if( left == right) return true;
		return left < right;
	}

	friend bool operator>(Rational const & left, Rational const & right) {
		return !(left <= right);
	}

	friend bool operator>=(Rational const & left, Rational const & right) {
		return !(left < right);
	}


	private:
	int numerator_;
	int denominator_;
};

Rational operator+(Rational lhs, Rational rhs);
Rational operator-(Rational lhs, Rational rhs);
Rational operator*(Rational lhs, Rational rhs);
Rational operator/(Rational lhs, Rational rhs);



#include <iostream>
using namespace std;
int main () {
	Rational r1(5, 10);
	Rational r2(1, 2);
	cout << (r1 == r2) << endl;
}
