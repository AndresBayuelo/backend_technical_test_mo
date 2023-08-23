# Despliegue local
## Requisitos
1. Docker
2. Visual Studio Code
2. Remote Development Extension Pack (ms-vscode-remote.vscode-remote-extensionpack)
## Pasos
1. Clonar el repositorio
2. Abrir el proyecto en Visual Studio Code
3. Abrir la paleta de comandos (Ctrl+Shift+P) y seleccionar la opción "Remote-Containers: Reopen in Container"
4. Esperar a que se descarguen las dependencias y se compile el proyecto
5. Abrir el terminal (Ctrl+Shift+ñ) y ejecutar el comando `source /workspaces/backend_technical_test_mo/venv/bin/activate`
6. Ejecutar el comando `python manage.py makemigrations`
7. Ejecutar el comando `python manage.py migrate`
8. Ejecutar el comando `python manage.py runserver`
9. Abrir el navegador en la dirección http://localhost:8000 para validar que el proyecto se ejecuta correctamente
# Orden de ejecución de endpoints
## Autenticación
1. Crear un usuario con el endpoint `http://localhost:8000/api-auth/signup/` con el método POST. El resultado de la petición incluirá el token de autenticación.
2. Iniciar sesión con el endpoint `http://localhost:8000/api-auth/login/` con el método POST. El resultado de la petición incluirá el token de autenticación.
3. Probar el token de autenticación con el endpoint `http://localhost:8000/api-auth/test_token/` con el método GET. El resultado de la petición incluirá el token de autenticación.
## Clientes
1. Crear un cliente con el endpoint `http://localhost:8000/api/customers/` con el método POST. El resultado de la petición incluirá el external_id del cliente.
2. Listar los clientes con el endpoint `http://localhost:8000/api/customers/` con el método GET. El resultado de la petición incluirá los clientes.
3. Obtener un cliente con el endpoint `http://localhost:8000/api/customers/<external_id>/` con el método GET. El resultado de la petición incluirá el cliente.
4. Para obtener el balance de un cliente se debe ejecutar el endpoint `http://localhost:8000/api/customers/<external_id>/get_balance/` con el método GET. El resultado de la petición incluirá el balance del cliente.
## Préstamos
1. Crear un préstamo con el endpoint `http://localhost:8000/api/loans/` con el método POST. El resultado de la petición incluirá el id del préstamo.
2. Para modificar su estado se debe ejecutar el endpoint `http://localhost:8000/api/loans/<external_id>/update_status/` con el método PATCH. El resultado de la petición incluirá el préstamo.
3. Listar los préstamos con el endpoint `http://localhost:8000/api/loans/` con el método GET. El resultado de la petición incluirá los préstamos.
4. Obtener un préstamo con el endpoint `http://localhost:8000/api/loans/<external_id>/` con el método GET. El resultado de la petición incluirá el préstamo.
5. Para obtener los préstamos de un cliente se debe ejecutar el endpoint `http://localhost:8000/api/customers/get_by_customer?customer_external_id=<external_id>` con el método GET. El resultado de la petición incluirá los préstamos del cliente.
## Pagos
1. Crear un pago con el endpoint `http://localhost:8000/api/payments/` con el método POST. El resultado de la petición incluirá el pago y los detalles con que ha sido creado.
2. Para modificar su estado se debe ejecutar el endpoint `http://localhost:8000/api/payments/<external_id>/update_status/` con el método PATCH. El resultado de la petición incluirá el pago y los detalles con que ha sido creado.
3. Listar los pagos con el endpoint `http://localhost:8000/api/payments/` con el método GET. El resultado de la petición incluirá los pagos y los detalles con que ha sido creado.
4. Obtener un pago con el endpoint `http://localhost:8000/api/payments/<external_id>/` con el método GET. El resultado de la petición incluirá el pago y los detalles con que ha sido creado.
5. Para obtener los pagos de uns cliente se debe ejecutar el endpoint `http://localhost:8000/api/payments/get_by_customer?customer_external_id=<external_id>` con el método GET. El resultado de la petición incluirá los pagos y los detalles con que ha sido creado.
