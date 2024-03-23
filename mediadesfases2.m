R4=[];
F=[];

todo=[];

for ka=0:1:20
file_name=strcat('desfase',num2str(ka),'diasal.txt');
load (file_name);
F(:,:,ka+1)=E;
endfor

for i=1:1:ne
for j=1:1:ne
vec=[];
for m=1:1:ne
vec=[vec,F(i,j,m)];
endfor
R4=[R4;i,j,vec];

endfor
endfor

