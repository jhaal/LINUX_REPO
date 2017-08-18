#include <iostream>
#include<iomanip>
using namespace std;
long double res1(long double cel); // function prototype
long double res2(long double far); // function prototype
long double res3(long double kel); // function prototype
float res4(float cel); // function prototype
const float Kelvin=273.15;

int main(void)
    {
cout<<setfill('*')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(80)<<"*"<<endl;
cout<<"*"<<setfill(' ')<<setw(49)<<"Temperature Scale Converter "<<setfill(' ')<<setw(31)<<"*"<<endl;
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
            cout << "1. Celsius To Fahreheit Conversion" << endl ;
            cout << "2. Fahrenheit To Celsius Conversion" << endl ;
            cout << "3. Celsius to Kelvin Conversion" << endl ;
            cout << "4. Kelvin to Celsius Conversion" << endl ;
            cout << "5. Exit" << endl ;
            cout << "Make selection and press return: \n" << endl ;
            cin >> user ;

    switch (user)
    {
    case 1:
    cout<< "Enter value in Celsius ";
    long double incel;
    cin >> incel;
    long double outfar = res1(incel); // function call
    cout<<"\n" << incel << "  Celsius is  "; 
    cout << outfar << "  Fahrenheit\n";
    break;
    
    case 2:
    cout<< "Enter value in Fahrenheit ";
    long double infar1;
    cin >> infar1;
    long double outcel1 = res2(infar1); // function call
    cout << "\n" << infar1 << "  Fahrenheit is  ";
    cout<< outcel1 << "  Celsius \n"; 
    break;
    
    case 3:
    cout<< "Enter value in Celsius ";
    long double incel2;
    cin >> incel2;
    long double outkel2 = res3(incel2); // function call
    cout << "\n" << incel2 << "  Celsius is  ";
    cout<< outkel2 << "  Kelvin \n"; 
    break;

    case 4:
    cout<< "Enter value in Kelvin ";
    float inkel3;
    cin >> inkel3;
    float outcel3 = res4(inkel3); // function call
    cout << "\n" << inkel3 << "  Kelvin is  ";
    cout<< outcel3 << "  Celsius \n"; 
    break;
    
    case 5:
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
long double res1(long double incel) // function specification
{
    long double result = (((9.0/5.0)*incel)+32);
    return result;
}
long double res2(long double infar) // function specification
{
    long double result1 = ((5.0/9.0)*(infar-32));
    return result1;
}
long double res3(long double incel) // function specification
{
    long double result1 = (incel+Kelvin);
    return result1;
}
float res4(float inkel) // function specification
{
    float result1 = (inkel-Kelvin);
    return result1;
}