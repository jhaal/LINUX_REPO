// Calculation of Fuel (Uranium Oxide) conductivity coefficient (kf)

#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;
int main ()
{
  ofstream outputFile;
  outputFile.open("Coolant_Temp");
  /*
  string filename;
  cout<<"\n Enter a file name for Temperature output:";
  getline (cin, filename);
  outputFile.open( filename.c_str() );
  */
  ///////////////////////////////////////////////// Calculation of fuel conductivity /////////////////////////////////////
  
            double t, D, LHR, cool;
	    const double k1=40.4;
	    const double k2=464;
	    const double k3=1.216e-4;
	    const double k4=1.867e-3;
	    const double k5=0.0191;
	    const double k6=0.58e-3;
	    const double pi=3.1415926;
	    float a,b,c,d,e,f,g,h,i,j,k,l,m,B;
  
	    cout<<"\n Input fuel temperature (in Deg-Celsius):";
	    cin>>t;
	    cout<<"\n Input fuel density (in percentage fraction):";
	    cin>>D;
	    cout<<"\n Input Linear Heat Rating of the Fuel (in W cm-1):";
	    cin>>LHR;
	    cout<<"\n Input Coolant Flow Rate (in Kg/Sec):";
	    cin>>cool;
	    
 
  if (0<t && 2840>t){
        if(t<1650){
	  B= 2.58-(k6*t);
	  a= B*(1-D);
	  b= 1-a;
	  c= B*(1-0.95);
	  d= 1-c;
	  e= (b/d);
	  f= k1/(k2+t);
	  g= exp(k4*t);
	  h= k3*g;
	  i=e*(f+h);
	  k=(8*pi*i);
	  l=(LHR/k);
	  m=(t-l);
	  //	  cout<<"Fuel conductivity (W cm-1 Deg-C-1) is= "<<i<<"\n";
	  //	  cout<<"Temperature at fuel pellet surface is= "<<m<<"\n";
	}
	if(1650<t){ 
	  B= 2.58-(k6*t);
	  a= B*(1-D);
	  b= 1-a;
	  c= B*(1-0.95);
	  d= 1-c;
	  e= (b/d);
	  f= k1/(k2+t);
	  g= exp(k4*t);
	  h= k3*g;
	  j=e*(k5+h);
	  k=(8*pi*j);
	  l=(LHR/k);
	  m=(t-l);
	  //	  cout<<"Fuel conductivity (W cm-1 Deg-C-1) is= "<<j<<"\n";
	  //	  cout<<"Temperature at fuel pellet surface is= "<<m<<"\n";
	}
  }
  else{
    cout<<"Fuel temeprature outside calculation range""\n";
  }
  
 ////////////////////////////// Write the results in file for fuel data ///////////////////////////////////////
  
                             string radius, temperature;
			     const double rad1=0.00;
			     const double rad2=0.61;
			     outputFile <<"#radius"<<"\t\t";
			     outputFile <<"temperature"<<"\n";
			     outputFile <<rad1<<"\t\t";
			     outputFile <<t<<"\n";
			     outputFile <<rad2<<"\t\t";
			     outputFile <<m<<"\n"; 
			     
///////////////////////////// Calculation of conductivity coefficient of Gap /////////////////////////////////////

  const double geq=10e-4; //He
  const double Const=2.5;
  const double phixehe=0.3843;// von Ubisch
  const double phihexe=3.4284;// von Ubisch
  const double He=0.90;
  const double Xe=0.10;
  const double lambdaXe=10.4e-5;
  const double lambdaHe=252.4e-5;
  const double km=0.075;
  const double a0=0.5;
  const double r1=2.3e-4;
  const double r2=2.3e-5;
  const double H=6.9e3;
  const double P=100;
  double a1,c1,d1,e1,f1,kmix,keqgp,keqs,ktot,r3,r4,t1,v1;

  //Gap Gas Conductance with gap mixture approximation from Saksena & Saxena

  a1=(Const*(r1+r2))+geq;   // Ross & Stoute
  
  //kmix from Saksena & Saxena 

  c1=phixehe*(He/Xe);
  d1=phihexe*(Xe/He);
  e1=lambdaXe/(1+c1);
  f1=lambdaHe/(1+d1);
  kmix=e1+f1;
  keqgp=kmix/a1;

  //Gap Solid Conductance

  r3=pow(r1,2)+pow (r2,2);
  r4=0.5*r3;
  t1=pow (r4 , 0.25);
  v1=a0*t1*H;
  keqs=((km*P)/v1);

  // Equivqlent Conductance

  ktot=keqs+keqgp;

  // Temperature drop across Gap

  float aa1,aa2,aa3, gap_dia;
  const double gap_thick = 0.0025;
  gap_dia = rad2+gap_thick;
  for (double gapd = gap_dia ; gapd > rad2 ; gapd = gapd-0.0001)
    {
      
      for (double gapd1 = rad2 ; gapd1 < gap_dia ; gapd1 = gapd1+0.0001)
	{
	  aa1=2*pi*gapd*ktot;
	  aa2=LHR/aa1;
	  aa3=m-aa2;
	  outputFile <<gapd1<<"\t\t";
	  outputFile <<aa3<<"\n";
	}
    }
  
  
//////////////////////////////////////////////////// Calculation of conductivity coefficient of Zircalloy ////////////////////////////////////////////

  double ee2,ff2,gg2,tK,zirconk;
  const double aaa=7.51;
  const double bbb=0.029;
  const double ccc=1.45e-5;
  const double ddd=7.67e-9;

  // Zircalloy Conductivity

  tK = aa3+273.15;
  ee2=bbb*tK;
  ff2=ccc* pow (tK,2);
  gg2=ddd* pow (tK,3);
  zirconk=aaa+ee2-ff2+gg2;
  
  /*
  cout<<"a="<<a<<"\n";
  cout<<"e="<<e<<"\n";
  cout<<"f="<<f<<"\n";
  cout<<"g="<<g<<"\n";
  */

  // Fuel Pencil Surface Temperature

  double aaaa1,aaaa2,aaaa3,aaaa4;
  const double cladt = 0.0415;
  float sheath_thick;
  sheath_thick = gap_dia+cladt;
  
  for (double cladr = sheath_thick ; cladr > gap_dia ; cladr = cladr-0.0001)
    {
      for (double cladr1 = gap_dia ; cladr1 < sheath_thick ; cladr1 = cladr1+0.0001)
	{
	  
	  aaaa1=LHR*cladt;
	  aaaa2=2*pi*cladr*(zirconk/100);
	  aaaa3=aaaa1/aaaa2;
	  aaaa4=aa3-aaaa3;
	  outputFile <<cladr1<<"\t\t";
	  outputFile <<aaaa4<<"\n";
	}
    }
  // outputFile.close();
  //cout<<"Done!\n";

  /////////////////////////////////////////// Coolant equivalent  conductivity calculation////////////////////////////////////////////////
  
  const double mu=93.6e-6;
  const double cond=0.595;
  const double cp=5.518;
  const double coolant_rad = 6.5; 
  
  float eqcon0, eqcon1, eqcon2, eqcon3, eqcon4, eqcon5 , eqcon6, eqcon7 , temp1 , temp2;
  
  eqcon0 = (2.0/3.0);
  eqcon1 = (cond/(cp*mu));
  eqcon2 = pow (eqcon1 , eqcon0);
  eqcon3 = 0.023*cp*cool*eqcon2;
  eqcon4 = (coolant_rad*cool)/mu;
  eqcon5 = -0.2;
  eqcon6 = pow (eqcon4 , eqcon5);
  eqcon7 = eqcon3*eqcon6;

  // Coolant Temperature calculation

  for ( float Rco = coolant_rad ; Rco > sheath_thick ; Rco = Rco-0.01)
    {
      for (float Rco1 = sheath_thick ; Rco1 < coolant_rad ; Rco1=Rco1+0.1)
	{
	temp1 = LHR/(2*pi*Rco*eqcon7);
        temp2 = aaaa4 - temp1;
	outputFile << Rco1 << "\t\t";
	outputFile << temp2 << "\n";
	}
    }
  
  outputFile.close();
  cout<<"Done Writing!\n";

  return 0;
}
