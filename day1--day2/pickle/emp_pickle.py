import emp, pickle

f = open('emp.csv', 'wb')
n = int(input("How many employees?"))
for i in range(n):
    id = int(input("Enter id :"))
    name = input("Enter name :")
    sal = float(input("Enter salary :"))

    e = emp.Emp(id,name,sal)
    x = pickle.dump(e,f)
f.close()