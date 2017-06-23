// 
//TODO fails at 83 test

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cassert>
#include <tuple>
#include <sstream>
#include <iterator>
#include <limits>

struct Node {
	Node * p = nullptr;
	Node * l = nullptr;
	Node * r = nullptr;
	long long key = -1;
	long long sum = 0;

	Node(long long k) :
		key(k), sum(k), p(nullptr), l(nullptr), r(nullptr) {
	}

	void refresh_sum(bool updateParents = true) {
		sum = key;
		sum += (l != nullptr ? l->sum : 0);
		sum += (r != nullptr ? r->sum : 0);
		if (updateParents && p)
			p->refresh_sum();
	}
};


class BstOfSum {
	long long _lastsum = 0;
	Node * _root = nullptr;

public:
	BstOfSum() { }
	void add(long long v) {
		long fv = _f(v);
		_add(fv);
	}
	void remove_item(long long v) {
		long fv = _f(v);
		_delete(fv);
	}
	bool find(long long  v) {
		long fv = _f(v);
		Node * found = _find(_root, fv);
		return found != nullptr;
	}
	long long sum(long long l, long long r) {
		long l2 = _f(l);
		long r2 = _f(r);
		long long s = _sum(l2, r2);
		_lastsum = s;
		return s;
	}

	std::string* get_str() {
		auto t = _get_preorder(_root, 0);
		auto s = new std::string("(last sum:" + std::to_string(_lastsum) + ")\n");
		s->append(*t);
		delete t;
		return s;
	}

private:
	std::string* _get_preorder(Node * t, int level) {
		auto s = new std::string("");
		if (t == nullptr)
			return s;
		if (t->l != nullptr) {
			auto tl = _get_preorder(t->l, level + 1);
			s->append(*tl);
			delete tl;
		}
		for (int i = 0; i < level; i++)
			s->append(" ");
		s->append(std::to_string(t->key) + "(" + std::to_string(t->sum) + ")");
		s->append("\n");
		if (t->r != nullptr) {
			auto tr = _get_preorder(t->r, level + 1);
			s->append(*tr);
			delete tr;
		}
		return s;
	}

	long _f(long long v) {
		const long long mod_const = 1000000001;
		return (_lastsum + v) % mod_const;
	}

	long long _sum(long l, long r) {
		if (_root == nullptr)
			return 0;
		long long rootsum = _root->sum;
		auto t1_t2 = _split(_root, l - 1);
		Node * t1 = std::get<0>(t1_t2);
		Node * t2 = std::get<1>(t1_t2);
		auto t3_t4 = _split(t2, r);
		Node * t3 = std::get<0>(t3_t4);
		Node * t4 = std::get<1>(t3_t4);

		long long res = 0;
		if(t3 != nullptr) 
			res = t3->sum;

		t2 = _merge(t3, t4);
		_root = _merge(t1, t2);
		return res;
	}

	std::tuple<Node*, Node*> _split(Node * v, long k) {
		if(v == nullptr) 
			return std::make_tuple(nullptr, nullptr);
		Node * u = v;
		while (true) {
			if (u->key == k) {
				break;
			}
			else if (u->key < k) {
				if (u->r == nullptr)
					break;
				u = u->r;
			}
			else {
				if (u->l == nullptr)
					break;
				u = u->l;
			}
		}
		_splay(u);
		assert(u->p == nullptr);

		if (u->key <= k) {
			Node * ur = u->r;
			if (ur != nullptr) {
				ur->p = nullptr;
				u->r = nullptr;
				u->refresh_sum();
			}
			return std::make_tuple(u, ur);
		}
		else {
			Node * ul = u->l;
			if (ul != nullptr) {
				ul->p = nullptr;
				u->l = nullptr;
				u->refresh_sum();
			}
			return std::make_tuple(ul, u);
		}
	}

	Node * _find(Node * v, long k) {
		while (v != nullptr) {
			if (v->key == k)
				break;
			else if (v->key < k)
				v = v->r;
			else
				v = v->l;
		}
		if (v == nullptr || v->key != k)
			return nullptr;
		else {
			_splay(v);
			_root = v;
			return v;
		}
	}

	bool _delete(long k) {
		Node * v = _root; 
		while (v != nullptr) {
			if (v->key == k)
				break;
			else if (v->key < k)
				v = v->r;
			else
				v = v->l;
		}
		if (v == nullptr || v->key != k)
			return false;
		_splay(v);  // to make v at top
		assert(v->p == nullptr);

		Node* vl = v->l;
		Node* vr = v->r;
		if (vl != nullptr)
			vl->p = nullptr;
		if (vr != nullptr)
			vr->p = nullptr;
		delete v;  // to remove from free memory
		_root = _merge(vl, vr);
		return true;
	}

	void _add(long k) {
		Node * z = new Node(k);
		if (_root == nullptr) {
			_root = z;
		}
		else {
			Node * v = _root;
			while (1) {
				if (v->key == k) {
					v->refresh_sum();  // to get sum of parents back
					delete z;  // not to be added
					z = v;
					break;
				}
				else if (v->key < k) {
					v->sum += k;
					if (v->r == nullptr) {
						v->r = z;
						z->p = v;
						break;
					}
					v = v->r;
				}
				else {
					v->sum += k;
					if (v->l == nullptr) {
						v->l = z;
						z->p = v;
						break;
					}
					v = v->l;
				}
			}
			if (z != nullptr) {
				_splay(z);
				_root = z;
			}
		}
	}

	Node * _get_max(Node * v) {
		while (v != nullptr && v->r != nullptr)
			v = v->r;
		return v;
	}

	Node* _merge(Node* t1, Node* t2) {
		Node * t = nullptr;
		if (t1 == nullptr && t2 == nullptr) {
			// return nothing below
		} else if (t1 == nullptr && t2 != nullptr)
			t = t2;
		else if (t1 != nullptr && t2 == nullptr)
			t = t1;
		else {
			assert(t1->p == nullptr);
			assert(t2->p == nullptr);
			Node * t1_max = _get_max(t1);
			_splay(t1_max);
			assert(t1_max->p == nullptr);
			assert(t1_max->r == nullptr);
			t1_max->r = t2;
			t2->p = t1_max;
			t1_max->refresh_sum();
			t = t1_max;
		}
		return t;
	}

	void _transplant(Node* u, Node* v) {
		if (u->p != nullptr) {
			if (u->p->r == u)
				u->p->r = v;
			else
				u->p->l = v;
		}
		if (v != nullptr)
			v->p = u->p;
		u->p = nullptr;
	}

	void _left_rotate(Node * u) {
		Node * v = u->r;
		u->r = v->l;
		if (u->r != nullptr)
			u->r->p = u;
		_transplant(u, v);
		v->l = u;
		v->l->p = v;
		v->l->refresh_sum(false);
		v->refresh_sum(false);
	}

	void _right_rotate(Node * u) {
		Node * v = u->l;
		u->l = v->r;
		if (u->l != nullptr)
			u->l->p = u;
		_transplant(u, v);
		v->r = u;
		v->r->p = v;
		v->r->refresh_sum(false);
		v->refresh_sum(false);
	}

	void _splay(Node * u) {
		if (u == nullptr || u->p == nullptr)
			return;
		while (u->p != nullptr) {
			if (u->p->p == nullptr) {
				if (u == u->p->l)
					_right_rotate(u->p);
				else if (u == u->p->r)
					_left_rotate(u->p);
				else
					throw std::exception();
			}
			else {
				// zig-zig:
				if (u == u->p->l && u->p == u->p->p->l) {
					_right_rotate(u->p->p);
					_right_rotate(u->p);
				}
				else if (u == u->p->r && u->p == u->p->p->r) {
					_left_rotate(u->p->p);
					_left_rotate(u->p);
				}
				// zig-zag:
				else if (u == u->p->l && u->p == u->p->p->r) {
					_right_rotate(u->p);
					_left_rotate(u->p);
				}
				else if (u == u->p->r && u->p == u->p->p->l) {
					_left_rotate(u->p);
					_right_rotate(u->p);
				}
				else {
					throw std::exception();
				}
			}
		}
	}

};

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
	int n = 0;
	std::cin >> n;
	// to ignore '\n'. See http://en.cppreference.com/w/cpp/string/basic_string/getline
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	BstOfSum bst;
	for (int i = 0; i < n; i++) {
		std::string command;
		std::getline(std::cin, command);

		//std::cout << command << std::endl;
		if (command.size() == 0)
			continue;
		std::vector<std::string> v = split(command, ' ');
		if (v[0] ==  "+") {
			bst.add(std::stoi(v[1]));
		}
		else if (v[0] == "-") {
			bst.remove_item(stoi(v[1]));
		}
		else if (v[0] == "?") {
			if (bst.find(stoi(v[1])))
				std::cout << "Found\n";
			else
				std::cout << "Not found\n";
		}
		else if (v[0] == "s") {
			std::cout << bst.sum(stoi(v[1]), stoi(v[2])) << std::endl;
		}
		//std::string* tree_str = bst.get_str();
		//std::cout << "Tree:" << std::endl;
		//std::cout << *tree_str << std::endl;
		//delete tree_str;
	}

	return 0;
}
