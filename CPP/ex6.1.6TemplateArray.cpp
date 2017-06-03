#include <cstddef>

template <typename T>
class Array
{
	public:
    //   конструктор класса, который создает
    //   Array размера size, заполненный значениями
    //   value типа T. Считайте что у типа T есть
    //   конструктор, который можно вызвать без
    //   без параметров, либо он ему не нужен.
    explicit Array(size_t size = 0, const T& value = T()) {
		_array = new T[size];
		_size = size;
		for(size_t i = 0; i < size; i++) {
			_array[i] = value;
		}
	}

    //   конструктор копирования, который создает
    //   копию параметра. Считайте, что для типа
    //   T определен оператор присваивания.
    Array(const Array & a) : _array(new T[a._size]), _size(a._size) {
		for(size_t i = 0; i < _size; i++)
			_array[i] = a._array[i];
	}

    //   деструктор, если он вам необходим.
    ~Array() {
		delete [] _array;
	}

    //   оператор присваивания.
    Array& operator=(const Array & a) { 
		if(this != &a) {
			delete [] _array;
			_size = a._size;
			_array = new T[_size];
			for(size_t i = 0; i < _size; i++)
				_array[i] = a._array[i];
		}
		return *this;
	}
  
    //   возвращает размер массива (количество
    //                              элементов).
    size_t size() const {
		return _size;
	}

    //   две версии оператора доступа по индексу.
    T& operator[](size_t i) {
		return _array[i];
	}

    const T& operator[](size_t i) const {
		return _array[i];
	}

	private:
	T * _array;
	size_t _size;
};

int main () {
}
