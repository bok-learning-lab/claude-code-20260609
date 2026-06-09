load 'c1.gnuplot'
set term epslatex color solid header "\\usepackage[T1]{fontenc}\n\\usepackage{cmbright}\n\\renewcommand*\\familydefault{\\sfdefault}" standalone
set output 'lec2_1.tex'

set key bottom spacing 1.2
set ylabel 'Probability' offset 1.5,0
set xlabel '$p$'
plot [0.5:1] x*x*(3-2*x) t '$S(p,3)$', x t '$S(p,1)$'
set output
!epstopdf lec2_1-inc.eps
!pdflatex lec2_1.tex
