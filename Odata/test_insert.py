# Odata/test_insert.py

import asyncio
from app.core.database import SessionLocal
from app.models.M_Student import Estudiante

async def insertar_estudiante():
    async with SessionLocal() as db:
        nuevo = Estudiante(nombre="Carlos", apellido="Ruiz", correo="carlos.ruiz@example.com")  # El correo es requerido
        db.add(nuevo)
        await db.commit()
        await db.refresh(nuevo)
        print(f"ID generado: {nuevo.id}")  # Debería imprimir un número entero

# Ejecutar la función asincrónica
asyncio.run(insertar_estudiante())
