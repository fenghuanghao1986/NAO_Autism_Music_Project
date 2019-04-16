#include <iostream>
using namespace std;

int main()
{
	char a = 'b';
	int c = 10, d = 10u, e = 10ul, f = 032, g = 0xC;
	cout << a << "\n"
		<< c << "\n"
		<< d << "\n"
		<< e << "\n"
		<< f << "\n";
	double h = 3.14, i = 3.14f, j = 3.14L;
	cout << h << "\n"
		<< i << "\n"
		<< j << "\n";
	return 0;
}