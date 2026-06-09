function [dydt] =sir_model(t,y)
 
T = 4;
 R = 3;
 S = 2;
 P = 1;

a11 = -1;
a12 = -10;
a21 = 0;
a22 =-7;

p=y(1);
q=y(2);

P1 = p*a11 + q*a12;
P2 = p*a21 + q*a22;
Pbar = p*P1 + q*P2;


dydt(1)=p*(P1 - Pbar);
dydt(2)=q*(P2 - Pbar);


dydt=dydt';

end

