#include <iostream>
using namespace std;

int pow(int val, int exp)
{
	int res;
	for (res = 1; exp > 0; --exp)
		res = res * val;
	return res;
}

int main()
{
	int val = 2;
	int exp = 15;

	cout << "The Powers of 2\n";
	for (int cnt = 0; cnt <= exp; ++cnt)
		cout << cnt << ": "
		<< pow(val, cnt) << endl;
	system("PAUSE");
	return 0;
}