set style line 1 lc rgbcolor "#ff0000" lw 2
set style line 2 lc rgbcolor "#222266" lw 2
set style line 3 lc rgbcolor "#11cccc" lw 2
set style line 4 lc rgbcolor "#ff6600" lw 2
set style line 5 lc rgbcolor "#777777" lw 2
set style line 6 lc rgbcolor "#22aa88" lw 2
set style increment user
set size 0.7,0.7

set term epslatex color solid header "\\usepackage[T1]{fontenc}\n\\usepackage{cmbright}\n\\renewcommand*\\familydefault{\\sfdefault}" standalone
set output 'lec2_2.tex'

set size 1,1

set key bottom spacing 1.2
set ylabel 'Probability' offset 1.5,0
set xlabel '$p$'
plot [0.5:1] x**7+7*x**6*(1-x)+21*x**5*(1-x)**2+35*x**4*(1-x)**3 t '$S(p,7)$', x**5+5*x**4*(1-x)+10*x**3*(1-x)**2 t '$S(p,5)$', x*x*(3-2*x) t '$S(p,3)$', x t '$S(p,1)$'
set output
!epstopdf lec2_2-inc.eps
!pdflatex lec2_2.tex
