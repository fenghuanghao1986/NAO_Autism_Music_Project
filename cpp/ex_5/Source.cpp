#include <iostream>
using namespace std;

bool compare1(char str1[], int len1, char str2[], int len2)
{
	int i, j;
	char a, b;
	if (len1 != len2)
		return false;

	if (len1 == len2)
	{
		for (i = 0; i < len1; i++)
		{
			a = toupper(str1[i]);
			b = toupper(str2[i]);

			if (a != b)
				return false;
			else
				continue;
		}
		return true;
	}
	
}



int main()
{
	int i, j, len1, len2;
	char str1[255], str2[255];
	cout << "Please input one set of chars until you hit enter: " << endl;
	
}