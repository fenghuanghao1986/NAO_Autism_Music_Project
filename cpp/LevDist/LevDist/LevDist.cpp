// LevDist.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int myMin(int num1, int num2, int num3)
{
	int temp1, temp2;

	if (num1 <= num2)
		temp1 = num1;
	else
		temp1 = num2;

	if (num2 <= num3)
		temp2 = num2;
	else
		temp2 = num3;

	if (temp1 <= temp2)
		return temp1;
	else
		return temp2;
}

float levDist(string str1, string str2)
{
	
	float sim;
	int a, b, i, j, cost;
	a = str1.length();
	b = str2.length();
	int** ld = new int* [a];
	for (int k = 0; k < a; k++)
	{
		ld[k] = new int[b];
	}

	for (i = 0; i < a; i++)
	{
		for (j = 0; j < b; j++)
		{
			ld[i][j] = 0;
		}
	}

	for (i = 0; i < a; i++)
	{
		ld[i][0] = i;
	}

	for (j = 0; j < b; j++)
	{
		ld[0][j] = j;
	}

	for (i = 1; i < a; i++)
	{
		for (j = 1; j < b; j++)
		{
			if (str1[i-1] == str2[j-1])
				cost = 0;
			else
				cost = 1;

			ld[i][j] = myMin(ld[i][j - 1] + 1,
				ld[i - 1][j] + 1,
				ld[i - 1][j - 1] + cost);
		}
	}
	return ld[a - 1][b - 1];
}

int main()
{
	string str1, str2;
	float sim;
	float d;
	cout << "Pleae input first word: " << endl;
	cin >> str1;
	cout << "Pleset input second word: " << endl;
	cin >> str2;
	d = levDist(str1, str2);
	sim = 1 / (1 + d);
	cout << "The similarity for both words is: " << sim << endl;
	system("pause");

}
