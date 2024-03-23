Matriz=sign(Matriz4);

for m=1:1:20
  E=zeros(ne,ne);
    for i=1:1:ne
      for j=1:1:ne
        D=sign(Matriz(1:731-m,:,i))+sign(Matriz(m+1:731,:,j));
        E(i,j)=rows(find(D==2));
      endfor
    endfor

  for pr=1:1:ne
    E(pr,pr)=0;
  endfor

file_name=strcat('desfase',num2str(m),'diasal.txt');   
save nombre E
rename ('nombre', [file_name])    
endfor
