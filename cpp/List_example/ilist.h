#pragma once
#include <iostream>
using namespace std;

class ilist_item
{
public:
	//...
	//void display(ostream &os = cout);
	ilist_item(int value, ilist_item* item_to_link_to = 0);
	int value() { return _value; }
	ilist_item* next() { return _next; }

	void next(ilist_item* link) { _next = link; }
	void value(int new_value) { _value = new_value; }
private:
	int _value;
	ilist_item* _next;
};

inline
ilist_item::
ilist_item(int value, ilist_item* item)
	:_value(value)
{
	if (!item)
		_next = 0;
	else
	{
		_next = item->_next;
		item->_next = this;
	}
}


class ilist {
public:
	//default constructor
	
	ilist() : _at_front(0),
		_at_end(0), _size(0) {};
		
	// ...
	// definitions not shown
	//ilist();
	int size();
	inline void bump_up_size() { ++_size; };
	inline void bump_down_size() { --_size; };
	inline void insert(ilist_item* ptr, int value)
	{
		if (!ptr)
			insert_front(value);
		else
		{
			bump_up_size();
			new ilist_item(value, ptr);
		}
	};
	inline void insert_front(int value)
	{
		ilist_item* ptr = new ilist_item(value);
		if (!_at_front)
			_at_front = _at_end = ptr;
		else
		{
			ptr->next(_at_front);
			_at_front = ptr;
		}
		bump_up_size();
	};
	inline void insert_end(int value)
	{
		if (!_at_end)
			_at_end = _at_front = new ilist_item(value);
		else
			_at_end = new ilist_item(value, _at_end);
		bump_up_size();
	};
	ilist_item* find(int value)
	{
		ilist_item* ptr = _at_front;
		while (ptr)
		{
			if (ptr->value() == value)
				break;
			ptr = ptr->next();
		}
		return ptr;
	};

	void display(ostream& os = cout)
	{
		os << "\n(" << _size << ")(";
		ilist_item* ptr = _at_front;
		while (ptr)
		{
			os << ptr->value() << "";
			ptr = ptr->next();
		}
		os << ")\n";
	};
	
	inline void remove_front()
	{
		if (_at_front)
		{
			ilist_item* ptr = _at_front;
			_at_front = _at_front->next();

			bump_down_size();
			delete ptr;
		}
	};
	void remove_all()
	{
		while (_at_front)
			remove_front();

		_size = 0;
		_at_front = _at_end = 0;
	};
	int remove(int value)
	{
		ilist_item* plist = _at_front;
		int elem_cnt = 0;

		while (plist && plist->value() == value)
		{
			plist = plist->next();
			remove_front();
			++elem_cnt;
		}

		if (!plist)
			return elem_cnt;

		ilist_item* prev = plist;
		plist = plist->next();

		while (plist)
		{
			if (plist->value() == value)
			{
				prev->next(plist->next());
				delete plist;
				++elem_cnt;
				bump_down_size();
				plist = prev->next();
				if (!plist)
				{
					_at_end = prev;
					return elem_cnt;
				}
			}
			else
			{
				prev = plist;
				plist = plist->next();
			}
		}
		return elem_cnt;
	}

private:
	
	ilist_item* _at_front;
	ilist_item* _at_end;
	int _size;


	// prohibiting assignment and initialization
	// of one ilist object with another
	ilist(const ilist&);
	ilist& operator=(const ilist&);

};

















