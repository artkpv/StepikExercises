struct Expression;
struct Number;
struct BinaryOperation;

struct ScopedPtr
{
    explicit ScopedPtr(Expression *ptr = 0) {
		_ptr = ptr;
	}

    ~ScopedPtr() {
		if(_ptr != 0) {
			delete _ptr;
		}
	}

    Expression* get() const { 
		return _ptr;
	}

    Expression* release() {
		if(_ptr != 0) {
			Expression * t = _ptr;
			_ptr = 0;
			return t;
		}
		return 0;
	}

    void reset(Expression *ptr = 0) {
		if(_ptr != 0) {
			delete _ptr;
		}
		_ptr = ptr;
	}

    Expression& operator*() const {
		return *_ptr;
	}

    Expression* operator->() const {
		if(_ptr != 0) return _ptr;
		return 0;
	}


private:
	Expression * _ptr;
    // запрещаем копирование ScopedPtr
    ScopedPtr(const ScopedPtr&);
    ScopedPtr& operator=(const ScopedPtr&);

    Expression *ptr_;
};
