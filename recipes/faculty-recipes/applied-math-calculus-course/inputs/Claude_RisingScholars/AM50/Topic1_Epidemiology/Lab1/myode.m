function [ dydt ] = myode(t, y )
%input variables are y and t, output variable is dy/dt as defined by the
%differential equation.

% dydt = y;
dydt = cos(t);

end

