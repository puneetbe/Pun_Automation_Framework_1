import moment

x = moment.now()
x = moment.now().strftime("%d-%m-%Y %Hhr/%Mmin/%Ssec")
print(x)