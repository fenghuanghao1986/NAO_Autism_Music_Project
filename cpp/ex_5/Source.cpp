/*
// Q1
#include <iostream>
#include <array>
using namespace std;

bool compareWithCase(char str1[], int len1, char str2[], int len2)
{
	int i;

	if (len1 != len2)
		return false;

	for (i = 0; i < len1; i++)
	{
		if (str1[i] != str2[i])
			return false;
		else
			continue;
	}
	return true;
	
}

bool compareIgnoreCase(char str1[], int len1, char str2[], int len2)
{
	int i;

	if (len1 != len2)
		return false;

	for (i = 0; i < len1; i++)
	{
		if (toupper(str1[i]) != toupper(str2[i]))
			return false;
		else
			continue;
	}
	return true;
}

int main()
{
	int len1, len2;
	char str1[255], str2[255];

	cout << "Please input one set of chars until you hit enter twice: " << endl;
	cin >> str1;
	len1 = sizeof(str1);
	cout << "Please input another set of chars until you hit enter twice: " << endl;
	cin >> str2;
	len2 = sizeof(str2);

	cout << str1 << endl;
	cout << str2 << endl;

	cout << compareWithCase(str1, len1, str2, len2) << endl;
	cout << compareIgnoreCase(str1, len1, str2, len2) << endl;

	system("pause");
	return 0;
}
*/


/*
// Q2
#include<iostream>
using namespace std;
int main(int argc, char* argv[]) {
	for (int i = 1; i < argc; i++)
		cout << argv[i];
}
*/


/*Write a program that converts from 24-
hour notation to 12-hour notation. For example, it should convert 14:25 to 2:25 P.M. The input is given
as two integers. There should be at least three functions: one for input, one to do the conversion, and
one for output. Record the A.M./P.M. information as a value of type char, ¡¯A¡¯ for A.M. and ¡¯P¡¯
for P.M. Thus, the function for doing the conversions will have a call-by-reference formal parameter of
type char to record whether it is A.M. or P.M. (The function will have other parameters as well.)
Include a loop that lets the user repeat this computation for new input values again and again until the
user says he or she wants to end the program.*/
//
#include <iostream>
#include <string.h>
using namespace std;

// define input function
string setTime(int len)
{
	
}

// define output function
char getTime(char str[])
{

}

// define time conversion function
char convertTime(char str[])
{
	char A = 'A.M.', P = 'P.M.';
	
}

// define main function
int main()
{
	char tOf24[5], tOf12[10];
	cout << "Please enter current time in 24hr notation, "
		<< "follow this format 01:23: " << endl;

	tOf24 = setTime();
}