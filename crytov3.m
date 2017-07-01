clear

fileID = fopen('/home/aitor/E. Avalancha/ran');
A = fscanf(fileID,'%d');
[a,b]=hist(A,unique(A));
hold on
bar(b,a,'FaceColor',[.5 .5 .5])
%plot(b,a, 'bo')
fileID1 = fopen('/home/aitor/E. Avalancha/hammingv3');
A1 = fscanf(fileID1,'%d');
[a1,b1]=hist(A1,unique(A1));
bar(b1,a1,0.4,'FaceColor',[0 .5 .5])
%plot(b,a, 'ro')
title('PBKDF1 prueba 3 vs Funcion Aleatoria')
xlabel('Distancias de Hamming')
ylabel('Ocurrencias')
legend('Funcion Aleatoria','PBKDF1')

% Stadistics
mean_rand = mean(A)
mean_pb = mean(A1)
median_rand = median(A)
median_pb = median(A1)
mode_rand = mode(A)
mode_pb = mode(A1)
var_rand = var(A)
var_pb = var(A1)
std_rand = std(A)
std_pb = std(A1)
stderr_rand = std(A)/sqrt(length(A))
stderr_pb = std(A1)/sqrt(length(A1))
skewness_rand = (sum((A-mean(A)).^3)./length(A)) ./ (var(A,1).^1.5)
skewness_pb = (sum((A1-mean(A1)).^3)./length(A1)) ./ (var(A1,1).^1.5)
kurtosis_rand = (sum((A-mean(A)).^4)./length(A)) ./ (var(A,1).^2)
Kurtosis_pb = (sum((A1-mean(A1)).^4)./length(A1)) ./ (var(A1,1).^2)
range_rand = max(A)-min(A)
range_pb = max(A1)-min(A1)
max_rand = max(A)
max_pb = max(A1)
min_rand = min(A)
min_pb = min(A1)
sum_rand = sum(A)
sum_pb = sum(A1)

%Chi cuadrado de Pearson
chi2 = sum(((A1-A).^2)\A)