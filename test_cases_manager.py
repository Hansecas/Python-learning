# Gestor simple de Test Cases

# Variables para un test case
test_case_id = "TC-001"
test_name = "Login - Credenciales validas"
status = "Not Executed"

print("=" * 50) 
print("TEST CASE MANAGER")
print("="*50)

print(f"\nID: {test_case_id}")
print(f"Nombre: {test_name}")
print(f"Estado {status}")

# Simulamos ejecutar el test

print("\n[Ejecutando test...]")
status = "Pass"
print(f"Resultado: {status}")

#Guardamos resultado
resultado = f"""
TEST CASE REPORT
ID: {test_case_id}
Nombre: {test_name}
Resultado: {status}
Fecha: 2026-07-28
"""

print(resultado)

# Test cases (copia y modifica)
test_case_1 = "TC-001: Login valido"
test_case_2 = "TC-002: Login contraseña invalida"
test_case_3 = "TC-003: Login usuario no existe"

#Simula ejecutarlos
tests = [test_case_1, test_case_2, test_case_3]
results = ["Pass", "Fail", "Fail"]

#Imprime reporte (Cambiamos las llaves por la variable 'tests' que ya creaste)
for i, (test, result) in enumerate(zip(tests, results)):
    print(f"{test} → {result}")

#Calcula porcentaje (Cambiamos las llaves {} por corchetes [] para contar sobre una lista)
pass_count = len([r for r in results if r == "Pass"])
total = len(results)
percentage = (pass_count / total) * 100

print(f"\n✓ Test Pasados: {pass_count}/{total} ({percentage}%)")



# Valida que email sea valido
email = "test@example.com"
if "@" in email and "." in email:
    print(f"✓ Email Valido: {email}")
else:
    print(f"✗ Email invalido: {email}")

# Valida contraseña
password = "MyPassword123!"
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(C.isdigit() for C in password)
is_long = len(password) >=8
if has_upper and has_lower and has_digit and is_long:
    print(f"✓ Contraseña fuerte")
else:
    print(f"✗ Contraseña debil")