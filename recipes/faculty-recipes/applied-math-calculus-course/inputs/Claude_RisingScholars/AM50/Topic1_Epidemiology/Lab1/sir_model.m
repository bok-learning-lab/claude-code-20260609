function [dydt] =sir_model(t,y)

N=1000;

%1/N people get sick per hour
beta=1/N;
%Recovery people is two weeks
gamma=1/(24*14); 

S=y(1);
I=y(2);
R=y(3);

dydt(1)=-beta*S*I;
dydt(2)=beta*S*I-gamma*I;
dydt(3)=gamma*I;

dydt=dydt';

end

