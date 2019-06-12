// kingProblem.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

int main()
{
	int i, j;
	for (i = 1; i <= 9; i++)
	{
		for (j = 1; j <= 9; j++)
		{
			if ((j % 3) != (i % 3))
				cout << "A = " << i << ", "
				<< "B = " << j << ";" << endl;
		}
	}
	system("pause");
}

