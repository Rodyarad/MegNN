k = 0;

F1 = fopen('Paths.txt','wt');
F2 = fopen('Dipoles.txt', 'wt');
F3 = fopen('Conection.txt', 'wt');
   
tic
for j = 1:15002
        childs(k, j, act_dip, Vertices, F3);
end
toc

function [] = childs(k, dip,act_dip,Vertices, F3)

    act_dip(end+1) = dip;

    if  k == 4
        fprintf(F3,'\n');
        return
    else
        k = k+1;
    end
    
    R = 7;
    n = 15002;
    n_neigh = 0;
    Neigh = [];
    ps = 0;
    p =[];
    dist = [];
    n_child = 1;
    for z = 1:n
        if z == dip
            continue
        end
        R1 = sqrt((Vertices(dip,1)*1000 - Vertices(z,1)*1000).^2 + (Vertices(dip,2)*1000 - Vertices(z,2)*1000).^2 + (Vertices(dip,3)*1000 - Vertices(z,3)*1000).^2);
        if R1 < R
            %R1 = sqrt((Vertices(dip,1)*100 - Vertices(z,1)*100).^2 + (Vertices(dip,2)*100 - Vertices(z,2)*100).^2 + (Vertices(dip,3)*100 - Vertices(z,3)*100).^2);
            dist(end+1) = R1;
            n_neigh = n_neigh + 1;
            Neigh(end+1) = z;
        end
    end
    
    alpha = var(dist);
    fprintf('%d\n',alpha);
    fprintf('До нормализации\n');
    for i = 1:n_neigh
        %p(end+1) = 1/(alpha*(2*pi.^2).^(1/2))*exp((-dist(i).^2)/(2*alpha));
        p(end+1) = exp((-dist(i).^2)/alpha);
        fprintf('p = %d\n',p(end));
        ps = ps + p(end);
    end
    
    for i = 1:n_neigh
        p(i) = p(i)/ps;
    end
    fprintf('Вероятности\n');
    for i = 1:n_neigh
        fprintf('p = %d\n',p(i));
    end
    fprintf('Соседи\n');
    for i = 1:n_neigh
        fprintf('%d\n',Neigh(i));
    end

    %x = randi([1, 100]);
    %if x <= 10
        %child = 0;
    %end    
    %if x>10 & x<=100
        %child = n_child;
    %end
    
    
    r = rand();
    i_neigh = sum(r>= cumsum([0, p]));

    
    %fprintf('child = %d\n',child);
    fprintf(F3,'%d ', dip);
    
    %if child ~= 0
        %for z = 1:child
    childs(k, Neigh(i_neigh), act_dip, Vertices,F3);
        %end
    %end
end