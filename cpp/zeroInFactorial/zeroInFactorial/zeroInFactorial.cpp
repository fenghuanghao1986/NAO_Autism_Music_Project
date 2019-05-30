// zeroInFactorial.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <math.h>
using namespace std;

int countZero(int n)
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

int countOne(int n)
{
	int x = 0, result = 0;
	while (true)
	{
		x = n % 2;
		n = n / 2;
		result = result + n;
		if (x != 0)
			break;
	}
	result = result + 1;
	return result;
}

int main()
{
	int n, N, M;
	cout << "Please input an interger: " << endl;
	cin >> n;
	N = countZero(n);
	M = countOne(n);
	cout << "Result for " << n << " factorial contains "
		<< N << " zeros at the end." << endl;

	cout << "The position of the first one occurs in the result of " << n << " factorial is "
		<< M << " ." << endl;
	system("pause");
}

