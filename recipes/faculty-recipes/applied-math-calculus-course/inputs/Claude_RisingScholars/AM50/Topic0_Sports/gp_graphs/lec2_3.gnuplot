load 'c1.gnuplot'
set term epslatex color solid header "\\usepackage[T1]{fontenc}\n\\usepackage{cmbright}\n\\renewcommand*\\familydefault{\\sfdefault}" standalone
set output 'lec2_3.tex'


unset key
set ylabel '$A$' offset 1.5,0
set xlabel '$p$'
plot [0.5:1] 4*x*(1-x)*(1+2*x*(1-x)+5*x*x*(1-x)*(1-x))
set output
!epstopdf lec2_3-inc.eps
!pdflatex lec2_3.tex
