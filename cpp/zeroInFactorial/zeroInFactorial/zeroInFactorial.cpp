// zeroInFactorial.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <math.h>
using namespace std;

double countZero(double n)
{
	double x, N = 0;
	while (x >= 5)
	{
		N = n / 5;
		x = n % 5;
	}
	return N;
}

int main()
{
	double n, N;
	cout << "Please input an interger: " << endl;
	cin >> n;
	N = countZero(n);
	cout << "Result for " << n << " factorial contains "
		<< N << " zeros at the end." << endl;
	system("pause");
}

