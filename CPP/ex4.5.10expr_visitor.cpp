// TODO make it compile
// https://stepik.org/lesson/%D0%9E%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BD%D0%BE-%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-556/step/10?course=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5-C%2B%2B&unit=879
struct Number;
struct BinaryOperation;

struct Visitor {
    virtual void visitNumber(Number const * number) = 0;
    virtual void visitBinaryOperation(BinaryOperation const * operation) = 0;
    virtual ~Visitor() { }
};

struct Expression
{
    virtual double evaluate() const = 0;
    virtual void visit(Visitor * vistitor) const = 0;
    virtual ~Expression();
};

struct Number : Expression
{
	Number(double value)
		: value(value)
	{}
	double evaluate() const;

	double get_value() const { return value; }

	void visit(Visitor * visitor) const { visitor->visitNumber(this); }

	private:
	double value;
};

struct BinaryOperation : Expression
{
	BinaryOperation(Expression const * left, char op, Expression const * right)
		: left(left), op(op), right(right)
	{ }
	~BinaryOperation();
	double evaluate() const;

	Expression const * get_left() const { return left; }
	Expression const * get_right() const { return right; }
	char get_op() const { return op; }

	void visit(Visitor * visitor) const { visitor->visitBinaryOperation(this); }

	private:
	Expression const * left;
	Expression const * right;
	char op;
};

#include <iostream>
using namespace std;

/* Этот класс вам нужно реализовать */
struct PrintVisitor : Visitor {
	void visitNumber(Number const * number)
	{
		cout << number->get_value();
	}

	void visitBinaryOperation(BinaryOperation const * bop)
	{
		char op = bop->get_op();
		if(op == '+' || op == '-') 
			cout << '(';
		Expression const * left = bop->get_left();
		left->visit(this);
		cout << op;
		Expression const * right = bop->get_right();
		right->visit(this);
		if(op == '+' || op == '-') 
			cout << ')';
	}
};

int main() {
	// сначала создаём объекты для подвыражения 4.5 * 5
	Expression * sube = new BinaryOperation(new Number(4.5), '*', new Number(5));
	// потом используем его в выражении для +
	Expression * expr = new BinaryOperation(new Number(3), '+', sube);

	PrintVisitor * pv = new PrintVisitor();
	expr->visit(pv);

	return 0;
}
