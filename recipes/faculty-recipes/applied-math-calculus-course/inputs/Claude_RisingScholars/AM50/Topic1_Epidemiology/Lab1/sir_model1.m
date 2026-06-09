function [dydt] =sir_model1(t,y)

N=11000;

%1/N people get sick per hour
beta=24*7/N; %beta has units of 1/(people*time)
%Recovery people is two weeks
gamma=24*7/(24*14); %gamma has units 1/time

S=y(1);
I=y(2);
R=y(3);

dydt(1)=-beta*S*I;
dydt(2)=beta*S*I-gamma*I;
dydt(3)=gamma*I;

dydt=dydt';

end

