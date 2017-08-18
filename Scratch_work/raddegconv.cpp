#include <iostream>
#include<iomanip>
using namespace std;
long double res1(long double deg); // function prototype
long double res2(long double rad); // function prototype
const double pi=3.141592;
int main(void)
    {
cout<<setfill('*')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(60)<<"Degree to Radian and Radian to Degree Converter "<<setfill(' ')<<setw(20)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(50)<<"Alok Jha ; alokjha@npcil.co.in"<<setfill(' ')<<setw(30)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(52)<<"NUCLEAR POWER CORPORATION OF INDIA"<<setfill(' ')<<setw(28)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<setfill('*')<<setw(80)<<"*"<<endl;
// option declaration
    int user ;
    bool cal = true ;
    while (cal != false)
        {
            cout << "\n\nPlease select option for degree to radian OR radian to degree conversion: " << endl ;
            cout << "1. Radian To Degree Conversion" << endl ;
            cout << "2. Degree To Radian Conversion" << endl ;
            cout << "3. Exit" << endl ;
            cout << "Make selection and press return: \n" << endl ;
            cin >> user ;

    switch (user)
    {
    case 1:
    cout<< "Enter value in Radian(s)";
    long double inrad;
    cin >> inrad;
    long double outdeg = res1(inrad); // function call
    cout<<"\n" << inrad << "  Radian(s) is  "; 
    cout << outdeg << "  Degree(s)\n";
    break;
    
    case 2:
    cout<< "Enter value in Degree(s)";
    long double indeg;
    cin >> indeg;
    long double outrad = res2(indeg); // function call
    cout << "\n" << indeg << "  Degree(s) is  ";
    cout<< outrad << "  Radian(s) \n"; 
    break;
    
    case 3:
    cout<<"Bye!!";
    cal = false;
    break;
    
    default :
    cout << "Make valid choice \n" ;
    cin >> user ;
    break ;
    }
    }
    return 0;
    }
long double res1(long double inrad) // function specification
{
    long double result = ((360/(2*pi))*inrad);
    return result;
}
long double res2(long double indeg) // function specification
{
    long double result1 = (((2*pi)/360)*indeg);
    return result1;
}
