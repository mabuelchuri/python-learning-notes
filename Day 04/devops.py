def cpu_status(cpu):
if cpu > 80:
return "High CPU"
return "Normal"

print(cpu_status(85))
