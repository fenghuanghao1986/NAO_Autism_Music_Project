// zeroInFactorial.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <math.h>
using namespace std;

double countZero(int n)
{
	int x = 0, result = 0;
	while (true)
	{
		x = n % 5;
		n = n / 5;
		result = result + n;
		if (x != 0)
			break;
	}
	return result;
}

int main()
{
	int n, N;
	cout << "Please input an interger: " << endl;
	cin >> n;
	N = countZero(n);
	cout << "Result for " << n << " factorial contains "
		<< N << " zeros at the end." << endl;
	system("pause");
}

