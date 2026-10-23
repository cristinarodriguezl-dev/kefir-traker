# Kefir Tracker

Aplicación de consola en Python para llevar el registro de las fermentaciones de kéfir de leche. Proyecto educativo para practicar la POO con un problema real.

## Qué hace

- **Registrar fermentaciones:** gránulos (g), leche (ml), horas y resultado.
- **Consultar el historial:** lista de todo lo registrado.
- **Eliminar fermentaciones:** con confirmación antes de borrar.
- **Ver estadísticas:** total, resultados por tipo y porcentaje de éxito, con una sugerencia según el resultado que más se repite.
- **Calcular la leche necesaria:** a partir de los gramos de gránulos, usando la proporción media de las 3 últimas fermentaciones buenas (hacen falta al menos 3).
- **Guardar los datos:** el historial se guarda en un archivo JSON, así que no se pierde al cerrar el programa.

## Tipos de resultado

Cada fermentación termina en uno de estos resultados, y cada uno tiene su propio mensaje con consejos:

| Resultado | Cuándo ocurre |
|---|---|
| Buena | La fermentación salió como se esperaba. |
| Sobrefermentada | Demasiado tiempo, poca leche o temperatura alta. |
| Insuficiente | Poco tiempo, demasiada leche o temperatura baja. |
| Dañado | Contaminación o exceso de horas. Los gránulos se desechan. |

## Requisitos

- Python 3.10 o superior
- Git (opcional, también se puede descargar el ZIP desde GitHub)

## Instalación

**1. Descargar el proyecto**

```bash
git clone https://github.com/cristinarodriguezl-dev/kefir-traker.git
cd kefir-traker
```

**2. Crear el entorno virtual**

```bash
python -m venv .venv
```

**3. Activarlo**

Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows (CMD):

```bat
.venv\Scripts\activate.bat
```

macOS y Linux:

```bash
source .venv/bin/activate
```

**4. Instalar las dependencias**

```bash
python -m pip install -r requirements.txt
```

**5. Ejecutar**

```bash
python main.py
```

Aparecerá el menú principal y se navega con las flechas del teclado y Enter.

## Estructura

```text
kefir-traker/
├── main.py
├── requirements.txt
├── data/
│   └── history.json
└── src/
    ├── menu.py
    ├── kefir_tracker.py
    ├── models.py
    ├── calculations.py
    ├── validations.py
    └── storage.py
```

| Archivo | Para qué sirve |
|---|---|
| `main.py` | Punto de entrada. |
| `menu.py` | Menú interactivo con `questionary`. |
| `kefir_tracker.py` | Lógica principal: historial, estadísticas y recomendación de leche. |
| `models.py` | Clase `Fermentation` y una subclase por cada tipo de resultado. |
| `calculations.py` | Cálculo de la leche y de la proporción media. |
| `validations.py` | Validación de los datos que se escriben. |
| `storage.py` | Lectura y escritura del historial en JSON. |

La carpeta `data/` se crea sola al guardar la primera fermentación. Está en el `.gitignore`, así que el historial de cada persona se queda en su ordenador.

## Cómo se calcula la leche

1. Se cogen las 3 últimas fermentaciones con resultado "Buena".
2. De cada una se calcula la proporción de leche por gramo de gránulos (`milk_ml / grains_weight`).
3. Se hace la media de esas 3 proporciones.
4. Se multiplica la media por los gramos de gránulos que se hayan escrito.

El resultado es una estimación basada en el propio historial. Cuantas más fermentaciones buenas haya, más se ajusta a las condiciones de cada casa.

## Qué se practica en el proyecto

- Clases, objetos y herencia (`Fermentation` y sus subclases).
- `super()` para reutilizar el constructor de la clase padre.
- Polimorfismo: `describe_result()` devuelve un mensaje distinto según el tipo.
- Separación del código en módulos con una responsabilidad cada uno.
- Validación de datos de entrada.
- Persistencia con JSON.
- Menús interactivos con `questionary`.

## Ideas para más adelante

- Filtrar el historial por fecha o por resultado.
- Guardar la temperatura ambiente de cada fermentación.
- Mostrar la evolución de los resultados con gráficas.

