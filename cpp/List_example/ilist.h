#pragma once
class ilist_item;

class ilist {
public:
	//default constructor
	ilist() : _at_front(0),
		_at_end(0), _size(0) {}

	inline int ilist::size() {
		return _size;
	}
	// ...

private:
	ilist_item *_at_front;
	ilist_item* _at_end;
	int _size;
};