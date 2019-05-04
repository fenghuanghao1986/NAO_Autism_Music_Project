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
/*
#include <iostream>
#include <string>
using namespace std;

string input()
{
	string str;
	cin >> str;
	cout << str.size() << endl;
	return str;
}

void output(string result)
{
	cout << result << endl;
}


// define time conversion function
string convertTime(string inTime)
{
	int i, j, k;
	int h, m;
	string tempH, tempM;
	string outTime;

	for (i = 0; i < inTime.size(); i++)
	{
		if (inTime[i] == ':')
			cout << i << endl;
			break;
	}

	for (j = 0; j < i; j++)
	{
		cout << j << endl;
		tempH.append(inTime, j);
	}

	for (k = i; k < inTime.size(); k++)
	{
		cout << k << endl;
		tempM.append(inTime, k);
	}

	h = atoi(tempH.c_str());

	if (h > 12 && h <= 24)
	{ 
		h = h - 12;
		tempH = to_string(h);
		outTime = tempH + ":" + tempM + "P.M.";
		return outTime;
	}
	else if (h == 12)
	{
		outTime = tempH + ":" + tempM + "P.M.";
		return outTime;
	}
	else if (h == 0)
	{
		h = 12;
		tempH = to_string(h);
		outTime = tempH + ":" + tempM + "A.M.";
		return outTime;
	}
	else
	{ 
		outTime = tempH + ":" + tempM + "A.M.";
		return outTime;
	}
		
}

// define main function
int main()
{
	string inTime, outTime;

	cout << "Please enter current time in 24hr notation, "
		<< "follow this format 01:23: " << endl;

	inTime = input();
	outTime = convertTime(inTime);
	output(outTime);

	system("pause");

}
*/


