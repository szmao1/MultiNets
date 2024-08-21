clc;clearvars;close all

dataset = load("data.mat");
x = dataset.data;

date = x{:,1}; carbon = x{:,2}; 

oil = x{:,3}; coal = x{:,4};gas = x{:,5};%enenry
stoxx = x{:,6}; GSCI =x{:,7}; rate = x{:,8};%economic


% figure(1)
% set(gcf, 'unit', 'centimeters', 'position', [5 20 30 15]);
% plot(date, carbon,LineWidth=1.25);
% datetick('x','mmm yyyy','keepticks')
% ylim([0 80])
% ylabel('Carbon price')
% xlabel('Time')
%annotation('textbox',[0.3,0.15,0.11,0.05],'LineStyle','-')


figure(2)
set(gcf, 'unit', 'centimeters', 'position', [5 5 25 18]);
subplot(3,2,3);
plot(date, oil,LineWidth=0.75);
title('Oil')

subplot(3,2,5);
plot(date, coal,LineWidth=1);
title('Coal')

subplot(3,2,1);
plot(date, gas,LineWidth=0.75);
title('Gas')

subplot(3,2,6);
plot(date, stoxx,LineWidth=0.75);
title('STOXX')

subplot(3,2,4);
plot(date, rate,LineWidth=0.75);
title('EURUSD')

subplot(3,2,2);
plot(date, GSCI,LineWidth=0.75);
title('GSCI')