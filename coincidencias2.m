Matriz=sign(Matriz4);
E=zeros(ne,ne);

for i=1:1:ne
  for j=i:1:ne
    D=sign(Matriz(:,:,i))+sign(Matriz(:,:,j));
    F=min(Matriz(:,:,i),Matriz(:,:,j));
    E(i,j)=rows(find(D==2));
    E(j,i)=rows(find(D==2));
  endfor
endfor

for pr=1:1:ne
  E(pr,pr)=0;
endfor

    save desfase0diasal.txt E
