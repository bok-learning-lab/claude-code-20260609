function [r] = Matt_Bouchard(N, history, lw, lc, y)

i = 0;
persistent CNT
if isempty(CNT)
   CNT = 1;
else
    CNT = CNT + 1;
end

if CNT < 100
    r = 2;       
end

if CNT >= 100
  lw = lw/CNT;
  i = 1;
  min = 0;
  
  while i < 20 && min == 0
      if lw(i) <= 1.5
          min = i;
      end
  i = i + 1;
  end
end

x = rand;
if x >= 0 && x <= 0.6
r = i; 
end

if x>0.6 && x <=0.70
    r = i + 1;
end

if x>0.70 && x <= 0.85
    r = i + 2;
end
 if x> 0.85 && x<=1
     r = i + 3;
 end 
end
        
