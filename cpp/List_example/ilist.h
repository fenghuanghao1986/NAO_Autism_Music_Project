#pragma once
#include <iostream>
class ilist_item
{
public:
	//...
	void display(ostream &os = cout);
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
	/*
	ilist() : _at_front(0),
		_at_end(0), _size(0) {}
		*/
	// ...
	// definitions not shown
	ilist();
	int size();

private:
	
	ilist_item* _at_front;
	ilist_item* _at_end;
	int _size;


	// prohibiting assignment and initialization
	// of one ilist object with another
	ilist(const ilist&);
	ilist& operator=(const ilist&);

};

inline void ilist::bump_up_size() { ++_size; }
inline void ilist::bump_down_size() { --_size; }

inline void
ilist::
insert(ilist_item* ptr, int value)
{
	if (!ptr)
		insert_front(value);
	else
	{
		bump_up_size();
		new ilist_item(value, ptr);
	}
}

inline void
ilist::
insert_front(int value)
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
}

inline void
ilist::
insert_end(int value)
{
	if (!_at_end)
		_at_end = _at_front = new ilist_item(value);
	else
		_at_end = new ilist_item(value, _at_end);
	bump_up_size();
}

ilist_item*
ilist::
find(int value)
{
	ilist_item* ptr = _at_front;
	while (ptr)
	{
		if (ptr->value() == value)
			break;
		ptr = ptr->next();
	}
	return ptr;
}

void
ilist::
diplay(ostream &os)
{
	os << "\n(" << _size << ")(";
	ilist_item* ptr = _at_front;
	while (ptr)
	{
		os << ptr->value() << "";
		ptr = ptr->next();
	}
	os << ")\n";
}