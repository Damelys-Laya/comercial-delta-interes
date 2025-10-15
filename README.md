# 📊 Proyecto: Cálculo de Interés Financiero – Comercial Delta S.A.

Este proyecto simula un caso empresarial donde se automatiza el cálculo de interés sobre operaciones financieras en Comercial Delta S.A., una empresa dedicada a la venta de productos tecnológicos. El objetivo es evaluar el impacto financiero de sus modalidades de pago: crédito, mora y pasivo.

---

## 🎯 Objetivos del proyecto

- Automatizar el cálculo de interés según tipo de operación
- Evaluar el impacto financiero de cada modalidad
- Generar reportes claros para decisiones gerenciales
- Aplicar lógica condicional y lectura de datos con Python
- Comunicar resultados con enfoque consultivo y estratégico

---

## 🧠 Tipos de interés considerados

- **Crédito**: interés activo (ganancia por financiar al cliente)
- **Pasivo**: interés pasivo (costo por endeudarse)
- **Mora**: penalización por pagos atrasados (simulada como 3 meses acumulados)

---

## 📁 Estructura de los datos

Los datos se encuentran en `datos.txt` y tienen el siguiente formato:

```txt
$1,200.00,credito
$3,500.00,mora
$2,000.00,pasivo
$4,750.00,credito
$1,800.00,mora
```

## 🐍 Lógica del script en Python

El archivo `calculo_interes.py` lee los datos desde un archivo `.txt`, identifica el tipo de operación financiera y calcula el interés correspondiente.  
Utiliza estructuras condicionales (`if`, `elif`) y formateo de texto para presentar los resultados de forma clara y profesional.

---

## ▶️ Cómo ejecutar el proyecto

Desde el terminal, dentro de la carpeta del proyecto:

```bash
python calculo_interes.py
```

📊 Reporte de cálculo de interés – Comercial Delta S.A.

Interés sobre $1,200.00 (credito): $60.00

Interés sobre $3,500.00 (mora): $525.00

Interés sobre $2,000.00 (pasivo): $100.00

Interés sobre $4,750.00 (credito): $237.50

Interés sobre $1,800.00 (mora): $270.00

## 📈 Análisis gerencial y estratégico

Este proyecto permite interpretar los resultados con visión de negocio:

- La **mora** representa el mayor costo financiero, lo que sugiere revisar políticas de cobro y ofrecer incentivos por pronto pago.
- El **crédito** genera ingresos por financiamiento, pero requiere control del riesgo de impago.
- El **pasivo** implica costos por endeudamiento, útil para evaluar decisiones de financiamiento externo.

Este tipo de análisis permite a la gerencia:

- Rediseñar condiciones de pago para mejorar flujo de caja y reducir exposición a mora
- Identificar oportunidades de mejora en la gestión financiera y operativa
- Priorizar estrategias de cobranza, financiamiento o renegociación según el perfil de impacto
- Simular escenarios de riesgo ante cambios en tasas, políticas o comportamiento del cliente


## 🚀 Ideas para expansión

Este proyecto puede evolucionar hacia soluciones más robustas:

- 📊 Lectura desde Excel o CSV para mayor flexibilidad
- 📈 Visualización de resultados con `matplotlib` o Excel
- 🧾 Generación de reportes automáticos en `.txt`, `.pdf` o `.xlsx`
- 🏥 Adaptación a otros sectores: clínicas, subsidios, trámites administrativos
- 🔍 Análisis de tendencias y riesgos según los datos procesados

---

## ✨ Autor

**Damelys Laya**  
Analista de Datos en formación con enfoque consultivo y estratégico en inteligencia de negocios.  
Integra automatización, análisis y comunicación profesional en cada proyecto.
