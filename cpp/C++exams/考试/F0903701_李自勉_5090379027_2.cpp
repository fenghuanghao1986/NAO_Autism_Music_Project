//F0903701 5090379027 李自勉
#include < iostream >
#include < string >
using namespace std;
int min ( int a, int b,int c );

int main()
{
    cout << "Input:" << endl;
    string str1,str2;
    int mod[50][50];
    cin >> str1 >> str2;
    int size1 = str1.size(),size2 = str2.size();
    //编辑距离，求最少步骤 
    for ( int i = size1;i >= 0;i-- )
    mod[i][size2] = size1 - i;
    for ( int j = size2;j >= 0;j-- )
    mod[size1][j] = size2 - j;
    int cost;
    for ( int i = size1 - 1;i >= 0;i-- )
    {
        for ( int j = size2 - 1;j >= 0;j-- )
		{
			if ( str1[i] == str2[j] )
				cost = 0;
			else
				cost = 1;
			mod[i][j] = min( mod[i+1][j+1] + cost,mod[i+1][j] + 1,mod[i][j+1] + 1 );
		}
	}
    //分情况对字符串进行编辑   
    cout << "Output:" << endl;
    cout << str1 <<endl;
    for ( int i = 0,j = 0;( i < size1 ) || ( j < size2 ); )
    {
		if ( str1[i] == str2[j] )
				cost = 0;
			else
				cost = 1;
        if ( ( i < size1 ) && ( j < size2 ) && ( mod[i][j] == mod[i+1][j+1] + cost ) )
        {
           i++;
           j++;
           if ( str1[i - 1] == str2[j - 1])
           continue;
        }
        else if ( ( j == size2 ) || ( i < size1 - 1 ) && ( mod[i][j] == mod[i+1][j] + 1 ) )
             i++;
        else if ( ( i == size1 ) || ( j < size2 - 1 ) && ( mod[i][j] == mod[i][j+1] + 1 ) )
             j++; 
        for ( int k = 0;k < j;k++ )
        cout << str2[k];
        for ( int k = i;k < size1;k++ )
        cout << str1[k];
        cout << endl;
    }

    return 0;
}

int min ( int a,int b,int c )
{
    int minn;
    minn = a;   
    if ( b < minn ) 
       minn = b;
	if ( c < minn )
		minn = c;
    return minn; 
} 















