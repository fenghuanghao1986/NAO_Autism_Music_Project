// countOne.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <math.h>
using namespace std;

int countOne(int i, int orgNum, int preResult, int curResult)
{
	int remainder, ones;
	int result[2];

	remainder = preResult % 10;

	if (remainder > 1)
		ones = (curResult + 1) * pow(10, i);
	else
		ones = curResult * pow(10, i) + (orgNum - preResult * pow(10, i) + 1) * remainder;


	return ones;
}

int main()
{
	int n, i, num, preResult, curResult, ones, sum = 0;

	cout << "Please input a interger less than 9 digits: ";
	cin >> num;

	preResult = num;
	n = floor(log10(num));

	for (i = 0; i < n + 1; i++)
	{
		curResult = preResult / 10;
		ones = countOne(i, num, preResult, curResult);
		preResult = curResult;
		sum = sum + ones;
	}

	cout << "There is " << sum << " 1s accurred from 1 to " << num << endl;
	system("pause");
}