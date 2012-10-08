from numpy import loadtxt, zeros
from pylab import *
# from matplotlib import rc

fname_base = '-v-span_24-bispar-fullSW'
savefig_flag = True

# rc('font', size=12.0)  # make fonts bigger, for readable presentation slides
figw = 8
figh = 4
close('all')

z = zeros(24)

figure(figsize=(figw,figh))
component = 's_11'
data = loadtxt(component + fname_base + '.txt')
ticklabel_format(scilimits=(-3, 3))
# ylim([-5e+6,4e+6])
plot(data[:,1],data[:,2],'ro-')
plot(data[:,1],data[:,3],'bs--')
plot(data[:,1],data[:,4],'rx-')
plot(data[:,1],data[:,5],'b+--')
plot(data[:,1],z,'k:')
xlabel('span [m]')
ylabel(component + ' [N/m^2]')
if savefig_flag: savefig(component + fname_base + '.png')

figure(figsize=(figw,figh))
component = 's_13'
data = loadtxt(component + fname_base + '.txt')
ticklabel_format(scilimits=(-3, 3))
# ylim([-5e+6,4e+6])
plot(data[:,1],data[:,2],'ro-')
plot(data[:,1],data[:,3],'bs--')
plot(data[:,1],z,'k:')
xlabel('span [m]')
ylabel(component + ' [N/m^2]')
if savefig_flag: savefig(component + fname_base + '.png')

figure(figsize=(figw,figh))
component = 'e_11'
data = loadtxt(component + fname_base + '.txt')
ticklabel_format(scilimits=(-3, 3))
# ylim([-4e+6,3e+6])
plot(data[:,1],data[:,2],'ro-')
plot(data[:,1],data[:,3],'bs--')
plot(data[:,1],z,'k:')
xlabel('span [m]')
ylabel(component + ' [N/m^2]')
if savefig_flag: savefig(component + fname_base + '.png')

figure(figsize=(figw,figh))
component = '2e_13'
data = loadtxt(component + fname_base + '.txt')
ticklabel_format(scilimits=(-3, 3))
# ylim([-4e+6,3e+6])
plot(data[:,1],data[:,2],'ro-')
plot(data[:,1],data[:,3],'bs--')
plot(data[:,1],z,'k:')
xlabel('span [m]')
ylabel(component + ' [N/m^2]')
if savefig_flag: savefig(component + fname_base + '.png')

show()